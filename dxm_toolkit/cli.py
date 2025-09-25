#!/usr/bin/env python3
"""
Command Line Interface for DXM Radar Toolkit

CLI for interacting with Banner DXM wireless controllers and radar sensors.
"""

import os
import sys
import time
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any

import click
from tabulate import tabulate

# Import our DXM toolkit modules
from .dxm_client import DXMClient, DXMConnectionError, DXMCommunicationError
from .sensor_decoder import SensorReading, SensorStatus
from .utils import (
    validate_ip_address, colorize_text, format_timestamp,
    validate_unit_id
)


# Global configuration object
class Config:
    """Configuration container for CLI application."""

    def __init__(self):
        self.config_file = None
        self.settings = self._load_default_config()

    def _load_default_config(self) -> Dict[str, Any]:
        """Load default configuration values."""
        return {
            'network': {
                'dxm_ip': '192.168.0.1',
                'modbus_port': 502,
                'timeout': 5.0,
                'retry_attempts': 3
            },
            'sensors': {
                'max_modules': 8,
                'base_unit_id': 1,
                'monitor_interval': 1.0,
                'distance_unit': 'mm'
            },
            'display': {
                'use_colors': True,
                'table_format': 'grid',
                'distance_precision': 1,
                'show_timestamps': True
            },
            'advanced': {
                'modbus_debug': False
            }
        }

    def load_from_file(self, config_path: str) -> None:
        """Load configuration from YAML file."""
        try:
            config_file = Path(config_path)
            if not config_file.exists():
                click.echo(f"Warning: Config file {config_path} not found, using defaults")
                return

            with open(config_file, 'r') as f:
                file_config = yaml.safe_load(f)

            # Merge file configuration with defaults
            self._merge_config(self.settings, file_config)
            self.config_file = config_path

        except Exception as e:
            click.echo(f"Error loading config file: {e}", err=True)
            click.echo("Using default configuration")

    def _merge_config(self, base: Dict, override: Dict) -> None:
        """Recursively merge configuration dictionaries."""
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value

    def get(self, key_path: str, default=None):
        """
        Get configuration value using dot notation.

        Example: config.get('network.dxm_ip') returns '192.168.0.1'
        """
        keys = key_path.split('.')
        value = self.settings

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value


# Global configuration instance
config = Config()


def find_config_file() -> Optional[str]:
    """Find configuration file in standard locations."""
    search_paths = [
        './config.yaml',  # Current directory
        os.path.expanduser('~/.dxm-toolkit/config.yaml'),  # User home
        '/etc/dxm-toolkit/config.yaml'  # System-wide
    ]

    for path in search_paths:
        if os.path.isfile(path):
            return path

    return None


def setup_client(ip: Optional[str] = None, debug: bool = False) -> DXMClient:
    """Create and configure DXM client instance."""
    # Use provided IP or fall back to configuration
    dxm_ip = ip or config.get('network.dxm_ip')

    if not validate_ip_address(dxm_ip):
        raise click.ClickException(f"Invalid IP address: {dxm_ip}")

    return DXMClient(
        host=dxm_ip,
        port=config.get('network.modbus_port'),
        timeout=config.get('network.timeout'),
        retry_attempts=config.get('network.retry_attempts'),
        debug=debug or config.get('advanced.modbus_debug')
    )


def format_reading_table(readings: List[SensorReading], show_timestamps: bool = True) -> str:
    """Format sensor readings as a table."""
    if not readings:
        return "No sensor readings available"

    # Prepare table headers
    headers = ['Unit', 'Status', 'Distance', 'Signal', 'Connected']
    if show_timestamps:
        headers.append('Timestamp')

    # Prepare table rows
    rows = []
    use_colors = config.get('display.use_colors')
    distance_unit = config.get('sensors.distance_unit')

    for reading in readings:
        # Format status with color
        if reading.status == SensorStatus.NORMAL:
            status_text = colorize_text("NORMAL", "green", use_colors)
        elif reading.status == SensorStatus.OUT_OF_RANGE:
            status_text = colorize_text("OUT_OF_RANGE", "yellow", use_colors)
        else:
            status_text = colorize_text("ERROR", "red", use_colors)

        # Format distance
        if reading.distance_mm is not None:
            if distance_unit == "mm":
                distance = f"{reading.distance_mm} mm"
            elif distance_unit == "cm":
                distance = f"{reading.distance_mm / 10:.1f} cm"
            elif distance_unit == "m":
                distance = f"{reading.distance_mm / 1000:.3f} m"
            else:
                distance = f"{reading.distance_mm} mm"
        else:
            if reading.distance_raw == 0:
                distance = colorize_text("DISCONNECTED", "red", use_colors)
            else:
                distance = colorize_text("OUT_OF_RANGE", "yellow", use_colors)

        # Format connection status
        connected = colorize_text("Yes", "green", use_colors) if reading.connected else colorize_text("No", "red", use_colors)

        # Build row
        row = [
            reading.unit_id,
            status_text,
            distance,
            reading.signal_quality,
            connected
        ]

        if show_timestamps:
            row.append(reading.timestamp.strftime("%H:%M:%S"))

        rows.append(row)

    # Generate table
    table_format = config.get('display.table_format')
    return tabulate(rows, headers=headers, tablefmt=table_format)


@click.group()
@click.option('--config', '-c', help='Configuration file path')
@click.option('--debug', is_flag=True, help='Enable debug output')
@click.pass_context
def cli(ctx, config_file, debug):
    """
    DXM Radar Toolkit - CLI for Banner DXM Controllers

    Tools for interacting with Banner DXM wireless controllers
    and their connected radar sensors via Modbus TCP.
    """
    # Ensure context object exists
    ctx.ensure_object(dict)

    # Load configuration
    config_path = config_file or find_config_file()
    if config_path:
        config.load_from_file(config_path)
        if debug:
            click.echo(f"Loaded configuration from: {config_path}")

    # Store debug flag in context
    ctx.obj['debug'] = debug


@cli.command()
@click.option('--ip', help='DXM IP address (overrides config)')
@click.option('--max-units', default=None, type=int, help='Maximum unit IDs to scan')
@click.pass_context
def discover(ctx, ip, max_units):
    """Discover connected sensors by scanning unit IDs."""
    debug = ctx.obj.get('debug', False)
    max_scan = max_units or config.get('sensors.max_modules')

    try:
        # Setup client and connect
        with setup_client(ip, debug) as client:
            click.echo(f"Discovering sensors on DXM at {client.host}...")
            click.echo(f"Scanning unit IDs 1-{max_scan}")

            # Perform discovery
            discovered = client.discover_sensors(max_scan)

            if discovered:
                click.echo(f"\nFound {len(discovered)} sensors:")
                for unit_id in discovered:
                    click.echo(f"  Unit ID {unit_id}")

                # Try to read detailed information from each sensor
                click.echo("\nSensor Details:")
                readings = []
                for unit_id in discovered:
                    try:
                        reading = client.read_sensor(unit_id)
                        readings.append(reading)
                    except Exception as e:
                        click.echo(f"  Unit {unit_id}: Error reading details - {e}")

                if readings:
                    click.echo(f"\n{format_reading_table(readings)}")

            else:
                click.echo("No sensors found")
                click.echo("\nTroubleshooting tips:")
                click.echo("  - Verify DXM IP address and network connectivity")
                click.echo("  - Check that sensors are properly connected to DXM")
                click.echo("  - Ensure IO-Link sensors are powered and configured")

    except DXMConnectionError as e:
        click.echo(f"Connection Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Discovery Error: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--ip', help='DXM IP address (overrides config)')
@click.option('--units', help='Comma-separated unit IDs to monitor (default: discover)')
@click.option('--interval', default=None, type=float, help='Monitoring interval in seconds')
@click.option('--duration', default=None, type=float, help='Monitoring duration in seconds')
@click.option('--no-colors', is_flag=True, help='Disable colored output')
@click.pass_context
def monitor(ctx, ip, units, interval, duration, no_colors):
    """Monitor sensors in real-time with live updates."""
    debug = ctx.obj.get('debug', False)
    monitor_interval = interval or config.get('sensors.monitor_interval')

    # Temporarily disable colors if requested
    original_color_setting = config.get('display.use_colors')
    if no_colors:
        config.settings['display']['use_colors'] = False

    try:
        # Setup client and connect
        with setup_client(ip, debug) as client:
            click.echo(f"Connecting to DXM at {client.host}...")

            # Determine which units to monitor
            if units:
                unit_ids = [int(u.strip()) for u in units.split(',')]
                click.echo(f"Monitoring units: {unit_ids}")
            else:
                click.echo("Discovering sensors...")
                unit_ids = client.discover_sensors()
                if not unit_ids:
                    click.echo("No sensors found for monitoring")
                    return
                click.echo(f"Monitoring discovered units: {unit_ids}")

            # Start monitoring
            click.echo(f"\nStarting real-time monitoring (interval: {monitor_interval}s)")
            if duration:
                click.echo(f"Duration: {duration}s")
            click.echo("Press Ctrl+C to stop\n")

            reading_count = 0
            try:
                for readings_dict in client.monitor_sensors(unit_ids, monitor_interval, duration):
                    # Clear screen for live updates (optional)
                    if reading_count > 0:
                        click.echo("\n" + "="*80)

                    # Convert readings dictionary to list for table formatting
                    current_readings = [r for r in readings_dict.values() if r is not None]

                    if current_readings:
                        timestamp = format_timestamp()
                        click.echo(f"Update {reading_count + 1} - {timestamp}")
                        click.echo(format_reading_table(current_readings))
                    else:
                        click.echo("No sensor data available")

                    reading_count += 1

            except KeyboardInterrupt:
                click.echo(f"\nMonitoring stopped after {reading_count} readings")

    except DXMConnectionError as e:
        click.echo(f"Connection Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Monitoring Error: {e}", err=True)
        sys.exit(1)
    finally:
        # Restore original color setting
        config.settings['display']['use_colors'] = original_color_setting


@cli.command()
@click.argument('unit_id', type=int)
@click.option('--ip', help='DXM IP address (overrides config)')
@click.option('--raw', is_flag=True, help='Show raw register values')
@click.option('--detailed', is_flag=True, help='Show detailed register interpretation')
@click.pass_context
def read(ctx, unit_id, ip, raw, detailed):
    """Read data from a specific sensor unit."""
    debug = ctx.obj.get('debug', False)

    if not validate_unit_id(unit_id):
        click.echo(f"Error: Invalid unit ID {unit_id}. Must be 1-247.", err=True)
        sys.exit(1)

    try:
        # Setup client and connect
        with setup_client(ip, debug) as client:
            click.echo(f"Reading sensor data from unit {unit_id}...")

            # Read sensor data
            reading = client.read_sensor(unit_id)

            # Display results based on requested format
            if raw:
                # Show raw register values
                click.echo(f"\nRaw Register Values for Unit {unit_id}:")
                click.echo(f"  Register 0 (Status): {reading.status_raw} (0x{reading.status_raw:04X})")
                click.echo(f"  Register 1 (BDC): {reading.bdc_states} (0x{reading.bdc_states:04X})")
                click.echo(f"  Register 2 (Distance): {reading.distance_raw}")
                click.echo(f"  Register 3 (Signal): {reading.signal_quality}")

            elif detailed:
                # Show detailed interpretation
                click.echo(f"\nDetailed Reading for Unit {unit_id}:")
                click.echo(f"  Timestamp: {reading.timestamp}")
                click.echo(f"  Status: {reading.status.name} ({reading.status_raw})")
                click.echo(f"  BDC States: 0x{reading.bdc_states:04X}")
                click.echo(f"  Distance: {reading.distance_mm}mm (raw: {reading.distance_raw})")
                click.echo(f"  Signal Quality: {reading.signal_quality}")
                click.echo(f"  Connected: {reading.connected}")
                click.echo(f"  Valid: {reading.valid}")

            else:
                # Standard formatted output
                click.echo(f"\n{format_reading_table([reading])}")

    except DXMCommunicationError as e:
        click.echo(f"Communication Error: {e}", err=True)
        sys.exit(1)
    except DXMConnectionError as e:
        click.echo(f"Connection Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Read Error: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--ip', help='DXM IP address (overrides config)')
@click.pass_context
def test(ctx, ip):
    """Test connection to DXM controller with comprehensive diagnostics."""
    debug = ctx.obj.get('debug', False)

    try:
        # Setup client (but don't connect yet)
        client = setup_client(ip, debug)

        click.echo(f"Testing connection to DXM at {client.host}:{client.port}")
        click.echo("Running comprehensive connectivity tests...\n")

        # Run connection tests
        test_results = client.test_connection()

        # Display results
        use_colors = config.get('display.use_colors')

        # Test 1: TCP Connection
        tcp_status = colorize_text("PASS", "green", use_colors) if test_results['tcp_connection'] else colorize_text("FAIL", "red", use_colors)
        click.echo(f"TCP Connection:      {tcp_status}")

        if test_results['latency_ms']:
            click.echo(f"Connection Latency:  {test_results['latency_ms']:.1f} ms")

        # Test 2: Modbus Communication
        modbus_status = colorize_text("PASS", "green", use_colors) if test_results['modbus_communication'] else colorize_text("FAIL", "red", use_colors)
        click.echo(f"Modbus Communication: {modbus_status}")

        # Test 3: Sensor Detection
        sensor_status = colorize_text("PASS", "green", use_colors) if test_results['sensor_detection'] else colorize_text("FAIL", "red", use_colors)
        click.echo(f"Sensor Detection:    {sensor_status}")

        # Show errors if any
        if test_results['errors']:
            click.echo("\nErrors encountered:")
            for error in test_results['errors']:
                click.echo(f"  - {error}")

        # Overall assessment
        if all([test_results['tcp_connection'], test_results['modbus_communication']]):
            click.echo(f"\n{colorize_text('✓ Connection test PASSED', 'green', use_colors)}")
            click.echo("DXM is accessible and responding to Modbus requests")
        else:
            click.echo(f"\n{colorize_text('✗ Connection test FAILED', 'red', use_colors)}")
            click.echo("Check network connectivity and DXM configuration")

    except Exception as e:
        click.echo(f"Test Error: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.pass_context
def config_show(ctx):
    """Show current configuration settings."""
    click.echo("Current DXM Toolkit Configuration:")
    click.echo("=" * 40)

    # Network settings
    click.echo("\nNetwork Settings:")
    click.echo(f"  DXM IP Address:    {config.get('network.dxm_ip')}")
    click.echo(f"  Modbus Port:       {config.get('network.modbus_port')}")
    click.echo(f"  Timeout:           {config.get('network.timeout')}s")
    click.echo(f"  Retry Attempts:    {config.get('network.retry_attempts')}")

    # Sensor settings
    click.echo("\nSensor Settings:")
    click.echo(f"  Max Modules:       {config.get('sensors.max_modules')}")
    click.echo(f"  Base Unit ID:      {config.get('sensors.base_unit_id')}")
    click.echo(f"  Monitor Interval:  {config.get('sensors.monitor_interval')}s")
    click.echo(f"  Distance Unit:     {config.get('sensors.distance_unit')}")

    # Display settings
    click.echo("\nDisplay Settings:")
    click.echo(f"  Use Colors:        {config.get('display.use_colors')}")
    click.echo(f"  Table Format:      {config.get('display.table_format')}")
    click.echo(f"  Show Timestamps:   {config.get('display.show_timestamps')}")

    # Configuration file info
    if config.config_file:
        click.echo(f"\nConfiguration loaded from: {config.config_file}")
    else:
        click.echo("\nUsing default configuration (no config file loaded)")


# Make the CLI group the default when running as a script
if __name__ == '__main__':
    cli()