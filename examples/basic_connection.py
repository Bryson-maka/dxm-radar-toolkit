#!/usr/bin/env python3
"""
Basic DXM Connection Example

This example demonstrates the fundamental concepts of connecting to a
Banner DXM controller and reading sensor data via Modbus TCP.

Educational Focus:
- Basic Modbus TCP connection establishment
- Simple sensor data reading
- Error handling patterns
- Connection lifecycle management

Prerequisites:
- DXM controller accessible at 192.168.0.1 (or modify IP)
- At least one IO-Link radar sensor connected to the DXM
- Network connectivity from this computer to the DXM

Run this example:
    python basic_connection.py
"""

import sys
import time
from pathlib import Path

# Add parent directory to path to import our toolkit
sys.path.insert(0, str(Path(__file__).parent.parent))

from dxm_toolkit import DXMClient, DXMConnectionError, DXMCommunicationError


def main():
    """
    Main function demonstrating basic DXM connection and sensor reading.

    Educational Note:
    This function shows the complete workflow for industrial sensor
    data acquisition: connection, reading, error handling, and cleanup.
    """
    print("DXM Radar Toolkit - Basic Connection Example")
    print("=" * 50)

    # Configuration - modify these values for your setup
    DXM_IP = "192.168.0.1"  # Default DXM IP address
    SENSOR_UNIT_ID = 1      # Unit ID of the sensor to read

    print(f"Connecting to DXM at {DXM_IP}")
    print(f"Reading sensor at Unit ID {SENSOR_UNIT_ID}")
    print()

    # Create DXM client instance
    # Educational Note: The DXMClient handles all Modbus TCP communication
    # details, providing a clean interface for sensor interaction
    client = DXMClient(
        host=DXM_IP,
        port=502,           # Standard Modbus TCP port
        timeout=5.0,        # Connection timeout in seconds
        retry_attempts=3,   # Number of retries for failed operations
        debug=False         # Set to True for detailed logging
    )

    try:
        # Step 1: Establish connection
        print("Step 1: Establishing connection to DXM...")
        client.connect()
        print("✓ Connected successfully!")

        # Step 2: Test basic communication
        print("\nStep 2: Testing Modbus communication...")
        test_results = client.test_connection()

        if test_results['modbus_communication']:
            print("✓ Modbus communication working")
            if test_results['latency_ms']:
                print(f"  Connection latency: {test_results['latency_ms']:.1f} ms")
        else:
            print("✗ Modbus communication failed")
            print("  Check DXM network configuration and sensor connections")
            return

        # Step 3: Read raw sensor registers
        print(f"\nStep 3: Reading raw registers from Unit {SENSOR_UNIT_ID}...")
        try:
            registers = client.read_sensor_registers(SENSOR_UNIT_ID, register_count=4)

            print("✓ Raw register values:")
            print(f"  Register 0 (Status):     {registers[0]} (0x{registers[0]:04X})")
            print(f"  Register 1 (BDC States): {registers[1]} (0x{registers[1]:04X})")
            print(f"  Register 2 (Distance):   {registers[2]} mm")
            print(f"  Register 3 (Signal):     {registers[3]}")

        except DXMCommunicationError as e:
            print(f"✗ Failed to read registers: {e}")
            print("  Possible causes:")
            print("  - No sensor at this Unit ID")
            print("  - Sensor not properly configured")
            print("  - IO-Link communication issues")
            return

        # Step 4: Read interpreted sensor data
        print(f"\nStep 4: Reading interpreted sensor data...")
        try:
            reading = client.read_sensor(SENSOR_UNIT_ID)

            print("✓ Interpreted sensor reading:")
            print(f"  Status:          {reading.status.name} ({reading.status_raw})")
            print(f"  Distance:        {reading.distance_mm} mm" if reading.distance_mm else "  Distance:        No valid reading")
            print(f"  Signal Quality:  {reading.signal_quality}")
            print(f"  Connected:       {'Yes' if reading.connected else 'No'}")
            print(f"  Timestamp:       {reading.timestamp}")

            # Interpret special conditions
            if reading.status.name == "OUT_OF_RANGE":
                print("\n📋 Note: Sensor indicates target is out of range")
                print("   This is normal if no object is within sensor range")
            elif not reading.connected:
                print("\n⚠️  Warning: Sensor appears disconnected")
                print("   Check IO-Link cable connections")
            elif reading.distance_mm and reading.distance_mm > 0:
                print(f"\n📏 Measurement: Object detected at {reading.distance_mm} mm")

        except DXMCommunicationError as e:
            print(f"✗ Failed to read sensor: {e}")
            return

        # Step 5: Multiple readings demonstration
        print(f"\nStep 5: Taking multiple readings (5 samples)...")
        print("Timestamp        | Status    | Distance | Signal")
        print("-" * 50)

        for i in range(5):
            try:
                reading = client.read_sensor(SENSOR_UNIT_ID)

                # Format distance for display
                if reading.distance_mm:
                    distance_str = f"{reading.distance_mm:4d} mm"
                elif reading.distance_raw == 0:
                    distance_str = "DISC    "
                else:
                    distance_str = "OOR     "

                print(f"{reading.timestamp.strftime('%H:%M:%S.%f')[:-3]} | "
                      f"{reading.status.name:9} | "
                      f"{distance_str} | "
                      f"{reading.signal_quality:3d}")

                time.sleep(0.5)  # Wait 500ms between readings

            except DXMCommunicationError as e:
                print(f"Sample {i+1} failed: {e}")

        print("\n✓ Basic connection example completed successfully!")

    except DXMConnectionError as e:
        print(f"✗ Connection failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Verify DXM IP address is correct")
        print("2. Check network connectivity (can you ping the DXM?)")
        print("3. Ensure DXM is powered on and operational")
        print("4. Verify Modbus TCP is enabled on the DXM")

    except KeyboardInterrupt:
        print("\n\nExample stopped by user (Ctrl+C)")

    except Exception as e:
        print(f"✗ Unexpected error: {e}")

    finally:
        # Step 6: Clean up connection
        print("\nStep 6: Cleaning up connection...")
        client.disconnect()
        print("✓ Disconnected from DXM")


def demonstrate_context_manager():
    """
    Demonstrate using the DXM client as a context manager.

    Educational Note:
    Context managers ensure proper resource cleanup even if
    exceptions occur. This is the recommended pattern for
    production code.
    """
    print("\n" + "=" * 50)
    print("Bonus: Context Manager Usage Example")
    print("=" * 50)

    DXM_IP = "192.168.0.1"

    try:
        # Using 'with' statement automatically handles connection/disconnection
        with DXMClient(host=DXM_IP) as client:
            print("✓ Connected using context manager")

            # Discover all available sensors
            sensors = client.discover_sensors()
            print(f"✓ Found {len(sensors)} sensors: {sensors}")

            # Read from each discovered sensor
            for unit_id in sensors:
                try:
                    reading = client.read_sensor(unit_id)
                    print(f"  Unit {unit_id}: {reading.status.name}, "
                          f"{reading.distance_mm or 'N/A'} mm")
                except Exception as e:
                    print(f"  Unit {unit_id}: Error - {e}")

        print("✓ Connection automatically closed by context manager")

    except Exception as e:
        print(f"✗ Context manager example failed: {e}")


if __name__ == "__main__":
    main()
    demonstrate_context_manager()

    print("\n" + "=" * 50)
    print("Educational Summary:")
    print("- DXM controllers bridge IO-Link sensors to Modbus TCP")
    print("- Each sensor gets a unique Modbus unit ID (1-8 typically)")
    print("- Register 0 = Status, Register 1 = BDC, Register 2 = Distance, Register 3 = Signal")
    print("- Always use proper error handling in industrial applications")
    print("- Context managers ensure clean resource management")
    print("=" * 50)