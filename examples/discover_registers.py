#!/usr/bin/env python3
"""
Register Discovery and Analysis Example

This example demonstrates techniques for discovering and analyzing Modbus
registers in DXM controllers. It's an educational tool for understanding
how IO-Link sensor data is mapped to Modbus registers.

Educational Focus:
- Systematic register scanning and discovery
- Data pattern analysis and interpretation
- Register mapping documentation techniques
- Diagnostic and troubleshooting methodologies
- Understanding IO-Link to Modbus data bridges

WARNING: This example performs extensive scanning and may impact DXM performance.
Use carefully on production systems and consider limiting scan ranges.

Run this example:
    python discover_registers.py
"""

import sys
import time
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Add parent directory to path to import our toolkit
sys.path.insert(0, str(Path(__file__).parent.parent))

from dxm_toolkit import DXMClient, SensorDecoder, DXMConnectionError, DXMCommunicationError


class RegisterDiscovery:
    """
    Professional register discovery and analysis tool.

    Educational Note:
    This class demonstrates systematic approaches to understanding
    unknown industrial devices. It's a common task when integrating
    new sensors or reverse-engineering communication protocols.
    """

    def __init__(self, dxm_ip: str = "192.168.0.1"):
        """Initialize the register discovery tool."""
        self.dxm_ip = dxm_ip
        self.client = None
        self.decoder = SensorDecoder()
        self.discovered_data = {}

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

    def scan_unit_ids(self, max_units: int = 8) -> List[int]:
        """
        Scan for responsive unit IDs.

        Educational Note:
        Before scanning registers, we need to identify which unit IDs
        are active. This prevents wasting time on non-existent devices.

        Args:
            max_units: Maximum unit ID to scan

        Returns:
            List of responsive unit IDs
        """
        if not self.client:
            raise RuntimeError("Not connected to DXM")

        print(f"Scanning for active unit IDs (1-{max_units})...")
        active_units = []

        for unit_id in range(1, max_units + 1):
            try:
                # Try reading a minimal register set
                result = self.client.read_sensor_registers(unit_id, 1)
                if result:
                    active_units.append(unit_id)
                    print(f"  ✓ Unit {unit_id}: Active")
            except DXMCommunicationError:
                print(f"  ✗ Unit {unit_id}: No response")
            except Exception as e:
                print(f"  ? Unit {unit_id}: Error - {e}")

            # Brief delay to avoid overwhelming the DXM
            time.sleep(0.1)

        print(f"Found {len(active_units)} active unit IDs: {active_units}")
        return active_units

    def scan_registers(self, unit_id: int, max_registers: int = 20) -> Dict[int, Any]:
        """
        Scan individual registers for a specific unit.

        Educational Note:
        This method demonstrates systematic register exploration.
        We read each register individually to build a complete
        picture of the device's register map.

        Args:
            unit_id: Unit ID to scan
            max_registers: Maximum register address to scan

        Returns:
            Dictionary mapping register addresses to values and metadata
        """
        if not self.client:
            raise RuntimeError("Not connected to DXM")

        print(f"\nScanning registers for Unit {unit_id} (addresses 0-{max_registers-1})...")

        register_data = {}

        for reg_addr in range(max_registers):
            try:
                # Read single register
                result = self.client._client.read_holding_registers(
                    address=reg_addr,
                    count=1,
                    unit=unit_id
                )

                if not result.isError():
                    value = result.registers[0]

                    # Decode using our known register interpretations
                    decoded = self.decoder.decode_single_register(reg_addr, value)

                    register_data[reg_addr] = {
                        'value': value,
                        'hex': f"0x{value:04X}",
                        'binary': f"0b{value:016b}",
                        'decoded': decoded,
                        'accessible': True
                    }

                    print(f"  Reg {reg_addr:2d}: {value:5d} (0x{value:04X}) - {decoded.get('interpretation', 'Unknown')}")

                else:
                    register_data[reg_addr] = {
                        'accessible': False,
                        'error': str(result)
                    }
                    print(f"  Reg {reg_addr:2d}: Error - {result}")

            except Exception as e:
                register_data[reg_addr] = {
                    'accessible': False,
                    'error': str(e)
                }
                print(f"  Reg {reg_addr:2d}: Exception - {e}")

            # Small delay to be gentle on the DXM
            time.sleep(0.05)

        return register_data

    def analyze_register_patterns(self, unit_id: int, duration: float = 10.0) -> Dict[str, Any]:
        """
        Analyze register patterns over time to understand data behavior.

        Educational Note:
        Static register scans only show current values. Dynamic analysis
        reveals which registers contain live data, counters, status flags,
        or configuration values.

        Args:
            unit_id: Unit ID to analyze
            duration: Analysis duration in seconds

        Returns:
            Analysis results with pattern information
        """
        if not self.client:
            raise RuntimeError("Not connected to DXM")

        print(f"\nAnalyzing register patterns for Unit {unit_id} over {duration}s...")

        # First, determine which registers are accessible
        print("  Determining accessible registers...")
        accessible_regs = []

        for reg_addr in range(10):  # Scan first 10 registers
            try:
                result = self.client._client.read_holding_registers(reg_addr, 1, unit=unit_id)
                if not result.isError():
                    accessible_regs.append(reg_addr)
            except:
                pass

        if not accessible_regs:
            print("  No accessible registers found")
            return {}

        print(f"  Found {len(accessible_regs)} accessible registers: {accessible_regs}")

        # Collect data over time
        print("  Collecting time-series data...")
        samples = []
        start_time = time.time()
        sample_interval = 0.2  # 200ms intervals

        while (time.time() - start_time) < duration:
            sample_time = time.time()
            sample = {'timestamp': sample_time, 'registers': {}}

            for reg_addr in accessible_regs:
                try:
                    result = self.client._client.read_holding_registers(reg_addr, 1, unit=unit_id)
                    if not result.isError():
                        sample['registers'][reg_addr] = result.registers[0]
                except:
                    pass

            samples.append(sample)
            time.sleep(sample_interval)

        # Analyze patterns
        print("  Analyzing patterns...")
        analysis = {
            'unit_id': unit_id,
            'sample_count': len(samples),
            'duration': duration,
            'registers': {}
        }

        for reg_addr in accessible_regs:
            values = []
            for sample in samples:
                if reg_addr in sample['registers']:
                    values.append(sample['registers'][reg_addr])

            if values:
                analysis['registers'][reg_addr] = {
                    'min_value': min(values),
                    'max_value': max(values),
                    'unique_values': len(set(values)),
                    'most_common': max(set(values), key=values.count),
                    'changes': sum(1 for i in range(1, len(values)) if values[i] != values[i-1]),
                    'pattern_type': self._classify_pattern(values)
                }

        return analysis

    def _classify_pattern(self, values: List[int]) -> str:
        """
        Classify the pattern type of a register's values.

        Educational Note:
        Different register types exhibit characteristic patterns:
        - Static: Configuration or constant values
        - Variable: Live sensor data
        - Counter: Incrementing values
        - Status: Few discrete states
        """
        if not values:
            return "empty"

        unique_count = len(set(values))
        change_count = sum(1 for i in range(1, len(values)) if values[i] != values[i-1])

        if unique_count == 1:
            return "static"
        elif unique_count <= 5:
            return "status/enum"
        elif change_count > len(values) * 0.7:
            return "highly_variable"
        elif all(values[i] >= values[i-1] for i in range(1, len(values))):
            return "monotonic_increasing"
        elif all(values[i] <= values[i-1] for i in range(1, len(values))):
            return "monotonic_decreasing"
        else:
            return "variable"

    def compare_known_mappings(self, unit_id: int) -> Dict[str, Any]:
        """
        Compare discovered registers with known DXM mappings.

        Educational Note:
        This method demonstrates how to validate discoveries against
        known documentation. It helps identify which registers match
        expected patterns and which might be new or unusual.

        Args:
            unit_id: Unit ID to analyze

        Returns:
            Comparison results
        """
        if not self.client:
            raise RuntimeError("Not connected to DXM")

        print(f"\nComparing Unit {unit_id} registers with known mappings...")

        # Get current register values
        try:
            registers = self.client.read_sensor_registers(unit_id, 4)
            current_reading = self.decoder.decode_registers(unit_id, registers)
        except Exception as e:
            print(f"  Error reading registers: {e}")
            return {}

        # Known register mappings from our research
        known_mappings = self.decoder.get_register_info()

        comparison = {
            'unit_id': unit_id,
            'timestamp': time.time(),
            'current_values': {i: registers[i] for i in range(len(registers))},
            'known_mappings': {},
            'validation_results': {}
        }

        print("  Register comparison:")
        print("  Addr | Current | Expected | Status | Description")
        print("  " + "-" * 60)

        for reg_addr, info in known_mappings.items():
            if reg_addr < len(registers):
                current_value = registers[reg_addr]
                expected_desc = info['description']

                comparison['known_mappings'][reg_addr] = info

                # Validate against expected patterns
                valid = True
                status = "✓ OK"

                if reg_addr == 0:  # Status register
                    if current_value not in [303, 271, 0]:
                        valid = False
                        status = "? Unknown status"
                elif reg_addr == 2:  # Distance register
                    if current_value > 30000 and current_value != 65535:
                        valid = False
                        status = "? Unusual distance"

                comparison['validation_results'][reg_addr] = {
                    'valid': valid,
                    'status': status
                }

                print(f"  {reg_addr:4d} | {current_value:7d} | {expected_desc[:12]:12} | {status:8} | {info['name']}")

        return comparison

    def generate_register_map(self, unit_ids: List[int]) -> Dict[str, Any]:
        """
        Generate comprehensive register map documentation.

        Educational Note:
        This method demonstrates how to create professional documentation
        of register mappings. Such documentation is essential for
        system integration and maintenance.

        Args:
            unit_ids: List of unit IDs to document

        Returns:
            Complete register map documentation
        """
        print(f"\nGenerating comprehensive register map for units: {unit_ids}")

        register_map = {
            'generation_time': time.time(),
            'dxm_ip': self.dxm_ip,
            'units': {},
            'summary': {
                'total_units': len(unit_ids),
                'accessible_registers': set(),
                'common_patterns': {}
            }
        }

        for unit_id in unit_ids:
            print(f"\n  Processing Unit {unit_id}...")

            unit_data = {
                'unit_id': unit_id,
                'registers': {},
                'patterns': {},
                'validation': {}
            }

            try:
                # Scan registers
                register_data = self.scan_registers(unit_id, max_registers=10)
                unit_data['registers'] = register_data

                # Analyze patterns
                pattern_analysis = self.analyze_register_patterns(unit_id, duration=5.0)
                unit_data['patterns'] = pattern_analysis

                # Compare with known mappings
                comparison = self.compare_known_mappings(unit_id)
                unit_data['validation'] = comparison

                # Update summary
                for reg_addr in register_data:
                    if register_data[reg_addr].get('accessible', False):
                        register_map['summary']['accessible_registers'].add(reg_addr)

                register_map['units'][unit_id] = unit_data

            except Exception as e:
                print(f"    Error processing Unit {unit_id}: {e}")
                unit_data['error'] = str(e)
                register_map['units'][unit_id] = unit_data

        # Convert set to list for JSON serialization
        register_map['summary']['accessible_registers'] = \
            sorted(list(register_map['summary']['accessible_registers']))

        return register_map

    def export_discoveries(self, data: Dict[str, Any], filename: str = None):
        """Export discovery results to JSON file."""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"register_discovery_{timestamp}.json"

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            print(f"✓ Discovery results exported to {filename}")
        except Exception as e:
            print(f"✗ Failed to export results: {e}")


def main():
    """
    Main function demonstrating register discovery techniques.
    """
    print("DXM Radar Toolkit - Register Discovery and Analysis")
    print("=" * 60)
    print("WARNING: This tool performs extensive scanning.")
    print("Use carefully on production systems!")
    print("=" * 60)

    # Configuration
    DXM_IP = "192.168.0.1"

    # Create discovery tool
    discovery = RegisterDiscovery(DXM_IP)

    try:
        # Connect and discover active units
        discovery.connect()
        active_units = discovery.scan_unit_ids()

        if not active_units:
            print("No active units found. Check DXM configuration.")
            return

        # Demonstrate various discovery techniques
        print("\n" + "=" * 40)
        print("Discovery Techniques Demonstration")
        print("=" * 40)

        # Technique 1: Static register scanning
        print("\n1. Static Register Scanning:")
        for unit_id in active_units[:2]:  # Limit to first 2 units
            register_data = discovery.scan_registers(unit_id, max_registers=6)

        # Technique 2: Dynamic pattern analysis
        print("\n2. Dynamic Pattern Analysis:")
        for unit_id in active_units[:1]:  # Limit to first unit
            patterns = discovery.analyze_register_patterns(unit_id, duration=5.0)

            print(f"\n  Pattern Analysis Results for Unit {unit_id}:")
            for reg_addr, info in patterns.get('registers', {}).items():
                print(f"    Reg {reg_addr}: {info['pattern_type']} "
                      f"(min:{info['min_value']}, max:{info['max_value']}, "
                      f"changes:{info['changes']})")

        # Technique 3: Known mapping validation
        print("\n3. Known Mapping Validation:")
        for unit_id in active_units[:2]:
            comparison = discovery.compare_known_mappings(unit_id)

        # Generate comprehensive register map
        print("\n4. Comprehensive Register Map Generation:")
        register_map = discovery.generate_register_map(active_units)

        # Export results
        discovery.export_discoveries(register_map)

        print("\n" + "=" * 60)
        print("Discovery Summary:")
        print(f"- Scanned {len(active_units)} active units")
        print(f"- Found {len(register_map['summary']['accessible_registers'])} accessible registers")
        print("- Generated comprehensive documentation")
        print("- Exported results to JSON file")
        print("=" * 60)

    except DXMConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Discovery error: {e}")
    finally:
        discovery.disconnect()


def demonstrate_advanced_analysis():
    """
    Demonstrate advanced register analysis techniques.

    Educational Note:
    This function shows more sophisticated analysis methods
    including correlation analysis, data validation, and
    automated pattern recognition.
    """
    print("\n" + "=" * 60)
    print("Advanced Analysis Techniques")
    print("=" * 60)

    DXM_IP = "192.168.0.1"

    try:
        with DXMClient(host=DXM_IP) as client:
            print("✓ Connected for advanced analysis")

            # Get a sensor for analysis
            sensors = client.discover_sensors()
            if not sensors:
                print("No sensors available for advanced analysis")
                return

            unit_id = sensors[0]
            print(f"Analyzing Unit {unit_id} with advanced techniques...")

            # Advanced Technique 1: Bit-level analysis
            print("\n1. Bit-level Register Analysis:")
            try:
                registers = client.read_sensor_registers(unit_id, 4)

                for i, value in enumerate(registers):
                    print(f"   Register {i}: {value:5d} = 0x{value:04X} = 0b{value:016b}")

                    # Analyze individual bits
                    significant_bits = []
                    for bit_pos in range(16):
                        if value & (1 << bit_pos):
                            significant_bits.append(bit_pos)

                    if significant_bits:
                        print(f"      Set bits: {significant_bits}")

            except Exception as e:
                print(f"   Bit analysis failed: {e}")

            # Advanced Technique 2: Data validation
            print("\n2. Data Validation and Consistency Checking:")
            try:
                # Take multiple readings and check consistency
                readings = []
                for _ in range(5):
                    reading = client.read_sensor(unit_id)
                    readings.append(reading)
                    time.sleep(0.2)

                print("   Consistency Analysis:")
                print("   Sample | Status | Distance | Signal | Consistent")
                print("   " + "-" * 50)

                for i, reading in enumerate(readings):
                    # Check for consistency issues
                    consistent = True
                    if reading.distance_raw == 0 and reading.connected:
                        consistent = False
                    if reading.distance_mm and reading.signal_quality == 0:
                        consistent = False

                    status = "✓" if consistent else "✗"
                    print(f"   {i+1:6d} | {reading.status.name:6} | "
                          f"{reading.distance_mm or 'N/A':8} | "
                          f"{reading.signal_quality:6d} | {status:10}")

            except Exception as e:
                print(f"   Validation failed: {e}")

            # Advanced Technique 3: Change detection
            print("\n3. Change Detection and Sensitivity Analysis:")
            try:
                print("   Monitoring for 10 seconds to detect changes...")

                previous_values = None
                change_count = 0

                for cycle in range(20):  # 10 seconds at 0.5s intervals
                    current_registers = client.read_sensor_registers(unit_id, 4)

                    if previous_values:
                        changes = []
                        for i, (prev, curr) in enumerate(zip(previous_values, current_registers)):
                            if prev != curr:
                                changes.append(f"Reg{i}:{prev}→{curr}")

                        if changes:
                            change_count += 1
                            print(f"   Cycle {cycle:2d}: Changes detected: {', '.join(changes)}")

                    previous_values = current_registers
                    time.sleep(0.5)

                print(f"   Detected changes in {change_count}/20 cycles ({change_count*5:.0f}%)")

            except Exception as e:
                print(f"   Change detection failed: {e}")

        print("\n✓ Advanced analysis completed")

    except Exception as e:
        print(f"Advanced analysis error: {e}")


if __name__ == "__main__":
    main()
    demonstrate_advanced_analysis()

    print("\n" + "=" * 60)
    print("Educational Summary:")
    print("- Systematic scanning reveals register structure")
    print("- Pattern analysis identifies data types and behaviors")
    print("- Validation confirms expected behaviors")
    print("- Documentation enables future integration work")
    print("- Advanced techniques provide deep insights")
    print("- Always be respectful of production systems")
    print("=" * 60)