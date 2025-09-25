#!/usr/bin/env python3
"""
Real-time Sensor Monitoring Example

This example demonstrates continuous monitoring of multiple radar sensors
connected to a DXM controller. It shows real-time data acquisition patterns
and professional data presentation techniques.

Educational Focus:
- Real-time data acquisition in industrial environments
- Multi-sensor monitoring strategies
- Data presentation and visualization patterns
- Performance considerations for continuous monitoring
- Error resilience in production monitoring systems

Prerequisites:
- DXM controller accessible at configured IP
- One or more IO-Link radar sensors connected
- Stable network connection for continuous monitoring

Run this example:
    python monitor_sensors.py
"""

import sys
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

# Add parent directory to path to import our toolkit
sys.path.insert(0, str(Path(__file__).parent.parent))

from dxm_toolkit import DXMClient, SensorReading, SensorStatus, DXMConnectionError


class SensorMonitor:
    """
    Professional sensor monitoring class with data logging and analysis.

    Educational Note:
    This class demonstrates how to structure a monitoring application
    for industrial environments. It includes features commonly needed
    in production systems: data logging, statistics, and error handling.
    """

    def __init__(self, dxm_ip: str = "192.168.0.1"):
        """
        Initialize the sensor monitor.

        Args:
            dxm_ip: IP address of the DXM controller
        """
        self.dxm_ip = dxm_ip
        self.client = None
        self.monitoring = False
        self.sensor_data_history = {}  # Store reading history per sensor
        self.error_counts = {}  # Track errors per sensor
        self.start_time = None

    def connect(self):
        """Establish connection to DXM controller."""
        print(f"Connecting to DXM at {self.dxm_ip}...")
        self.client = DXMClient(host=self.dxm_ip, debug=False)
        self.client.connect()
        print("✓ Connected successfully")

    def disconnect(self):
        """Disconnect from DXM controller."""
        if self.client:
            self.client.disconnect()
            print("✓ Disconnected from DXM")

    def discover_sensors(self) -> List[int]:
        """
        Discover all available sensors.

        Educational Note:
        Discovery is often performed once at startup to identify
        the sensor topology. This avoids repeatedly probing
        non-existent sensors during monitoring.

        Returns:
            List of discovered unit IDs
        """
        print("Discovering connected sensors...")
        if not self.client:
            raise RuntimeError("Not connected to DXM")

        sensors = self.client.discover_sensors()
        print(f"✓ Found {len(sensors)} sensors: {sensors}")
        return sensors

    def start_monitoring(self, unit_ids: List[int], duration: float = 60.0, interval: float = 1.0):
        """
        Start continuous monitoring of specified sensors.

        Educational Note:
        This method demonstrates the main monitoring loop pattern
        used in industrial applications. It handles timing, error
        recovery, and data collection efficiently.

        Args:
            unit_ids: List of sensor unit IDs to monitor
            duration: Total monitoring time in seconds
            interval: Time between readings in seconds
        """
        if not self.client:
            raise RuntimeError("Not connected to DXM")

        self.monitoring = True
        self.start_time = datetime.now()
        end_time = self.start_time + timedelta(seconds=duration)

        print(f"\nStarting monitoring of {len(unit_ids)} sensors")
        print(f"Duration: {duration}s, Interval: {interval}s")
        print(f"Start time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 80)

        # Initialize data structures
        for unit_id in unit_ids:
            self.sensor_data_history[unit_id] = []
            self.error_counts[unit_id] = 0

        reading_count = 0

        try:
            while self.monitoring and datetime.now() < end_time:
                cycle_start = time.time()

                # Read all sensors for this cycle
                readings = {}
                for unit_id in unit_ids:
                    try:
                        reading = self.client.read_sensor(unit_id)
                        readings[unit_id] = reading
                        self.sensor_data_history[unit_id].append(reading)
                    except Exception as e:
                        print(f"Error reading sensor {unit_id}: {e}")
                        self.error_counts[unit_id] += 1
                        readings[unit_id] = None

                # Display current readings
                self.display_readings(readings, reading_count)

                reading_count += 1

                # Calculate sleep time to maintain interval
                cycle_time = time.time() - cycle_start
                sleep_time = max(0, interval - cycle_time)

                if cycle_time > interval:
                    print(f"Warning: Cycle time ({cycle_time:.2f}s) exceeded interval ({interval}s)")

                if sleep_time > 0:
                    time.sleep(sleep_time)

        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
        finally:
            self.monitoring = False

        print(f"\nMonitoring completed - {reading_count} cycles")
        self.show_statistics(unit_ids)

    def display_readings(self, readings: Dict[int, Optional[SensorReading]], cycle: int):
        """
        Display current sensor readings in a formatted table.

        Educational Note:
        Good data presentation is crucial for monitoring applications.
        This method shows how to create clean, readable real-time displays.

        Args:
            readings: Dictionary of current readings
            cycle: Current cycle number
        """
        # Clear previous display (simple approach)
        if cycle > 0:
            print("\n" + "=" * 80)

        current_time = datetime.now()
        elapsed = (current_time - self.start_time).total_seconds()

        print(f"Cycle {cycle + 1:3d} | {current_time.strftime('%H:%M:%S')} | "
              f"Elapsed: {elapsed:6.1f}s")
        print("-" * 80)

        # Table header
        print(f"{'Unit':4} | {'Status':12} | {'Distance':10} | {'Signal':6} | {'Connected':9}")
        print("-" * 80)

        # Display each sensor
        for unit_id in sorted(readings.keys()):
            reading = readings[unit_id]

            if reading is None:
                print(f"{unit_id:4} | {'ERROR':12} | {'N/A':10} | {'N/A':6} | {'No':9}")
                continue

            # Format status with visual indicators
            if reading.status == SensorStatus.NORMAL:
                status_str = "NORMAL ✓"
            elif reading.status == SensorStatus.OUT_OF_RANGE:
                status_str = "OUT_RANGE ⚠"
            else:
                status_str = "ERROR ✗"

            # Format distance
            if reading.distance_mm is not None:
                distance_str = f"{reading.distance_mm:4d} mm"
            elif reading.distance_raw == 0:
                distance_str = "DISCONN"
            else:
                distance_str = "OUT_RANGE"

            # Connection status
            conn_str = "Yes" if reading.connected else "No"

            print(f"{unit_id:4} | {status_str:12} | {distance_str:10} | "
                  f"{reading.signal_quality:6} | {conn_str:9}")

    def show_statistics(self, unit_ids: List[int]):
        """
        Display monitoring statistics and analysis.

        Educational Note:
        Post-monitoring analysis helps identify patterns, issues,
        and system performance characteristics. This is valuable
        for system optimization and troubleshooting.

        Args:
            unit_ids: List of monitored unit IDs
        """
        print("\nMonitoring Statistics")
        print("=" * 50)

        for unit_id in unit_ids:
            readings = self.sensor_data_history.get(unit_id, [])
            error_count = self.error_counts.get(unit_id, 0)

            print(f"\nSensor Unit {unit_id}:")
            print(f"  Total readings:     {len(readings)}")
            print(f"  Communication errors: {error_count}")

            if readings:
                # Calculate success rate
                success_rate = (len(readings) / (len(readings) + error_count)) * 100
                print(f"  Success rate:       {success_rate:.1f}%")

                # Status distribution
                status_counts = {}
                for reading in readings:
                    status = reading.status.name
                    status_counts[status] = status_counts.get(status, 0) + 1

                print("  Status distribution:")
                for status, count in status_counts.items():
                    percentage = (count / len(readings)) * 100
                    print(f"    {status}: {count} ({percentage:.1f}%)")

                # Distance statistics (valid readings only)
                valid_distances = [r.distance_mm for r in readings
                                 if r.distance_mm is not None]

                if valid_distances:
                    print("  Distance statistics:")
                    print(f"    Valid measurements: {len(valid_distances)}")
                    print(f"    Min distance:       {min(valid_distances)} mm")
                    print(f"    Max distance:       {max(valid_distances)} mm")
                    print(f"    Average distance:   {sum(valid_distances)/len(valid_distances):.1f} mm")

                # Signal quality statistics
                signals = [r.signal_quality for r in readings]
                if signals:
                    print("  Signal quality:")
                    print(f"    Min signal:         {min(signals)}")
                    print(f"    Max signal:         {max(signals)}")
                    print(f"    Average signal:     {sum(signals)/len(signals):.1f}")

    def export_data(self, filename: str = None):
        """
        Export collected data to JSON file.

        Educational Note:
        Data export capabilities are important for further analysis,
        reporting, and integration with other systems.

        Args:
            filename: Output filename (auto-generated if None)
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"sensor_data_{timestamp}.json"

        export_data = {
            'monitoring_session': {
                'start_time': self.start_time.isoformat() if self.start_time else None,
                'dxm_ip': self.dxm_ip,
                'sensor_count': len(self.sensor_data_history)
            },
            'sensors': {}
        }

        # Export data for each sensor
        for unit_id, readings in self.sensor_data_history.items():
            sensor_data = []
            for reading in readings:
                sensor_data.append(reading.to_dict())

            export_data['sensors'][str(unit_id)] = {
                'readings': sensor_data,
                'error_count': self.error_counts.get(unit_id, 0)
            }

        try:
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            print(f"✓ Data exported to {filename}")
        except Exception as e:
            print(f"✗ Failed to export data: {e}")


def main():
    """
    Main function demonstrating comprehensive sensor monitoring.
    """
    print("DXM Radar Toolkit - Real-time Sensor Monitoring Example")
    print("=" * 60)

    # Configuration
    DXM_IP = "192.168.0.1"
    MONITOR_DURATION = 30.0  # seconds
    MONITOR_INTERVAL = 1.0   # seconds

    # Create monitor instance
    monitor = SensorMonitor(DXM_IP)

    try:
        # Connect and discover sensors
        monitor.connect()
        sensors = monitor.discover_sensors()

        if not sensors:
            print("No sensors found. Please check DXM configuration.")
            return

        # Start monitoring
        print(f"\nPress Ctrl+C to stop monitoring early")
        monitor.start_monitoring(
            unit_ids=sensors,
            duration=MONITOR_DURATION,
            interval=MONITOR_INTERVAL
        )

        # Export data
        monitor.export_data()

    except DXMConnectionError as e:
        print(f"Connection error: {e}")
        print("\nTroubleshooting:")
        print("- Check DXM IP address and network connectivity")
        print("- Verify DXM is powered and operational")
        print("- Ensure Modbus TCP is enabled on DXM")

    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user")

    except Exception as e:
        print(f"Monitoring error: {e}")

    finally:
        monitor.disconnect()


def demonstrate_advanced_monitoring():
    """
    Demonstrate advanced monitoring features.

    Educational Note:
    This function shows more sophisticated monitoring patterns
    including conditional monitoring, alert generation, and
    adaptive timing based on sensor behavior.
    """
    print("\n" + "=" * 60)
    print("Advanced Monitoring Features Demo")
    print("=" * 60)

    DXM_IP = "192.168.0.1"

    try:
        with DXMClient(host=DXM_IP) as client:
            print("✓ Connected for advanced monitoring demo")

            sensors = client.discover_sensors()
            if not sensors:
                print("No sensors available for advanced demo")
                return

            print(f"Demonstrating advanced features with {len(sensors)} sensors")

            # Feature 1: Adaptive monitoring interval
            print("\n1. Adaptive Monitoring Interval:")
            print("   (Faster updates when distance is changing rapidly)")

            previous_distances = {}
            base_interval = 1.0

            for cycle in range(10):
                cycle_start = time.time()
                max_change = 0

                for unit_id in sensors:
                    try:
                        reading = client.read_sensor(unit_id)
                        current_distance = reading.distance_mm or 0

                        if unit_id in previous_distances:
                            change = abs(current_distance - previous_distances[unit_id])
                            max_change = max(max_change, change)

                        previous_distances[unit_id] = current_distance

                        print(f"   Unit {unit_id}: {current_distance:4d} mm, "
                              f"Signal: {reading.signal_quality:3d}")

                    except Exception as e:
                        print(f"   Unit {unit_id}: Error - {e}")

                # Adaptive interval: faster when things are changing
                if max_change > 50:  # Significant change threshold
                    interval = base_interval * 0.5  # Speed up
                    print(f"   → Fast monitoring (change: {max_change} mm)")
                else:
                    interval = base_interval
                    print(f"   → Normal monitoring (change: {max_change} mm)")

                # Maintain timing
                cycle_time = time.time() - cycle_start
                sleep_time = max(0, interval - cycle_time)
                if sleep_time > 0:
                    time.sleep(sleep_time)

            # Feature 2: Alert generation
            print("\n2. Alert Generation:")
            print("   (Generating alerts for specific conditions)")

            for unit_id in sensors:
                try:
                    reading = client.read_sensor(unit_id)

                    # Generate alerts based on conditions
                    if not reading.connected:
                        print(f"   🚨 ALERT: Sensor {unit_id} disconnected!")
                    elif reading.signal_quality < 10:
                        print(f"   ⚠️  WARNING: Sensor {unit_id} weak signal ({reading.signal_quality})")
                    elif reading.distance_mm and reading.distance_mm < 100:
                        print(f"   📍 INFO: Sensor {unit_id} close object detected ({reading.distance_mm} mm)")
                    else:
                        print(f"   ✅ OK: Sensor {unit_id} normal operation")

                except Exception as e:
                    print(f"   ❌ ERROR: Sensor {unit_id} communication failed - {e}")

        print("\n✓ Advanced monitoring demo completed")

    except Exception as e:
        print(f"Advanced demo error: {e}")


if __name__ == "__main__":
    main()
    demonstrate_advanced_monitoring()

    print("\n" + "=" * 60)
    print("Educational Summary:")
    print("- Real-time monitoring requires careful timing management")
    print("- Error resilience is critical in industrial monitoring")
    print("- Data presentation affects usability significantly")
    print("- Statistics and analysis provide valuable insights")
    print("- Export capabilities enable integration with other systems")
    print("- Adaptive monitoring can optimize performance")
    print("=" * 60)