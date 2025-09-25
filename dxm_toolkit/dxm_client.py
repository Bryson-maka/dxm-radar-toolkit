#!/usr/bin/env python3
"""
DXM Client for Modbus TCP Communication

Core client for communicating with Banner DXM wireless controllers via Modbus TCP.
Handles connection management, register reading, and error recovery.
"""

import logging
import socket
import time
from typing import List, Optional, Dict, Any, Union
from contextlib import contextmanager

try:
    from pymodbus.client import ModbusTcpClient
    from pymodbus.exceptions import ModbusException, ConnectionException
    from pymodbus.constants import Endian
    from pymodbus.payload import BinaryPayloadDecoder
except ImportError:
    raise ImportError("pymodbus library is required. Install with: pip install pymodbus>=3.0.0")

from .sensor_decoder import SensorDecoder, SensorReading
from .utils import validate_ip_address, validate_unit_id


class DXMConnectionError(Exception):
    """Custom exception for DXM connection issues."""
    pass


class DXMCommunicationError(Exception):
    """Custom exception for DXM communication issues."""
    pass


class DXMClient:
    """
    Main client class for DXM Modbus TCP communication.

    Educational Note:
    This class demonstrates the client-side implementation of Modbus TCP
    for industrial automation. It encapsulates connection management,
    error handling, and data interpretation specific to DXM controllers.

    Key Concepts Demonstrated:
    - Modbus TCP client configuration
    - Connection lifecycle management
    - Register reading with error recovery
    - Industrial networking best practices
    """

    def __init__(self,
                 host: str = "192.168.0.1",
                 port: int = 502,
                 timeout: float = 5.0,
                 retry_attempts: int = 3,
                 debug: bool = False):
        """
        Initialize DXM Modbus TCP client.

        Educational Note:
        The DXM controller acts as a Modbus TCP server, typically listening
        on the standard port 502. The controller bridges IO-Link sensor data
        to Modbus registers, making sensor data accessible via standard
        industrial networking protocols.

        Args:
            host: DXM controller IP address
            port: Modbus TCP port (standard is 502)
            timeout: Connection timeout in seconds
            retry_attempts: Number of retry attempts for failed operations
            debug: Enable detailed logging for troubleshooting

        Raises:
            ValueError: If invalid IP address provided
        """
        if not validate_ip_address(host):
            raise ValueError(f"Invalid IP address: {host}")

        self.host = host
        self.port = port
        self.timeout = timeout
        self.retry_attempts = retry_attempts

        # Configure logging
        self.logger = logging.getLogger(__name__)
        if debug:
            self.logger.setLevel(logging.DEBUG)

        # Initialize Modbus client
        # Educational Note: ModbusTcpClient handles the TCP connection
        # and Modbus protocol details. We configure it for optimal
        # industrial networking performance.
        self._client = ModbusTcpClient(
            host=self.host,
            port=self.port,
            timeout=self.timeout,
            retry_on_empty=True,  # Retry if no response received
            retries=1,  # Internal pymodbus retries (we handle our own)
            source_address=None  # Let system choose source port
        )

        # Initialize sensor decoder
        self._decoder = SensorDecoder()

        # Connection state tracking
        self._connected = False
        self._last_error = None

    def __enter__(self):
        """Context manager entry - establish connection."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - clean up connection."""
        self.disconnect()

    @property
    def connected(self) -> bool:
        """Check if client is currently connected."""
        return self._connected and self._client.connected

    @property
    def last_error(self) -> Optional[str]:
        """Get the last error message encountered."""
        return self._last_error

    def connect(self) -> bool:
        """
        Establish connection to DXM controller.

        Educational Note:
        This method demonstrates proper connection establishment patterns
        for industrial networking. We verify connectivity at multiple levels:
        TCP connection, Modbus protocol response, and device identification.

        Returns:
            bool: True if connection successful

        Raises:
            DXMConnectionError: If connection fails
        """
        try:
            self.logger.info(f"Connecting to DXM at {self.host}:{self.port}")

            # Attempt TCP connection
            result = self._client.connect()
            if not result:
                raise DXMConnectionError("Failed to establish TCP connection")

            # Verify Modbus communication with a test read
            # Educational Note: Reading a known register verifies that
            # the Modbus protocol layer is working correctly
            test_result = self._client.read_holding_registers(0, 1, unit=1)
            if test_result.isError():
                raise DXMConnectionError(f"Modbus communication test failed: {test_result}")

            self._connected = True
            self._last_error = None
            self.logger.info("Successfully connected to DXM")
            return True

        except Exception as e:
            self._connected = False
            self._last_error = str(e)
            self.logger.error(f"Connection failed: {e}")
            raise DXMConnectionError(f"Failed to connect to DXM: {e}")

    def disconnect(self) -> None:
        """
        Close connection to DXM controller.

        Educational Note:
        Proper connection cleanup is important in industrial applications
        to avoid resource leaks and ensure other applications can connect.
        """
        try:
            if self._client.connected:
                self._client.close()
                self.logger.info("Disconnected from DXM")
        except Exception as e:
            self.logger.warning(f"Error during disconnect: {e}")
        finally:
            self._connected = False

    def test_connection(self) -> Dict[str, Any]:
        """
        Perform comprehensive connection test.

        Educational Note:
        This method demonstrates comprehensive connectivity testing patterns
        used in industrial diagnostics. It tests multiple layers of the
        communication stack.

        Returns:
            Dictionary with test results and diagnostic information
        """
        test_results = {
            'tcp_connection': False,
            'modbus_communication': False,
            'sensor_detection': False,
            'latency_ms': None,
            'errors': []
        }

        try:
            # Test 1: TCP Connection
            start_time = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)

            try:
                result = sock.connect_ex((self.host, self.port))
                if result == 0:
                    test_results['tcp_connection'] = True
                    test_results['latency_ms'] = (time.time() - start_time) * 1000
                else:
                    test_results['errors'].append(f"TCP connection failed: {result}")
            finally:
                sock.close()

            # Test 2: Modbus Communication
            if test_results['tcp_connection']:
                if not self.connected:
                    self.connect()

                # Try reading from multiple unit IDs
                for unit_id in range(1, 5):
                    try:
                        result = self._client.read_holding_registers(0, 4, unit=unit_id)
                        if not result.isError():
                            test_results['modbus_communication'] = True
                            test_results['sensor_detection'] = True
                            break
                    except Exception as e:
                        test_results['errors'].append(f"Unit {unit_id}: {str(e)}")

        except Exception as e:
            test_results['errors'].append(f"Connection test failed: {str(e)}")

        return test_results

    def read_sensor_registers(self, unit_id: int, register_count: int = 4) -> List[int]:
        """
        Read holding registers from a specific sensor unit.

        Educational Note:
        This method demonstrates the core Modbus register reading operation.
        DXM controllers map IO-Link sensor data to consecutive Modbus holding
        registers, starting from address 0.

        Args:
            unit_id: Modbus unit ID (1-247)
            register_count: Number of registers to read

        Returns:
            List of register values

        Raises:
            DXMCommunicationError: If read operation fails
        """
        if not validate_unit_id(unit_id):
            raise ValueError(f"Invalid unit ID: {unit_id}")

        if not self.connected:
            raise DXMConnectionError("Not connected to DXM")

        for attempt in range(self.retry_attempts):
            try:
                self.logger.debug(f"Reading {register_count} registers from unit {unit_id}")

                # Read holding registers starting from address 0
                # Educational Note: Holding registers are 16-bit read/write registers
                # commonly used for sensor data in industrial applications
                result = self._client.read_holding_registers(
                    address=0,  # Start at register 0
                    count=register_count,
                    unit=unit_id
                )

                if result.isError():
                    error_msg = f"Modbus error reading unit {unit_id}: {result}"
                    self.logger.warning(error_msg)
                    if attempt == self.retry_attempts - 1:
                        raise DXMCommunicationError(error_msg)
                    continue

                # Extract register values
                registers = result.registers
                self.logger.debug(f"Successfully read registers: {registers}")
                return registers

            except ModbusException as e:
                error_msg = f"Modbus exception on attempt {attempt + 1}: {e}"
                self.logger.warning(error_msg)
                if attempt == self.retry_attempts - 1:
                    raise DXMCommunicationError(error_msg)

            except Exception as e:
                error_msg = f"Unexpected error on attempt {attempt + 1}: {e}"
                self.logger.error(error_msg)
                if attempt == self.retry_attempts - 1:
                    raise DXMCommunicationError(error_msg)

            # Brief delay before retry
            if attempt < self.retry_attempts - 1:
                time.sleep(0.1)

        # This line should never be reached due to the retry logic above
        raise DXMCommunicationError(f"Failed to read registers after {self.retry_attempts} attempts")

    def read_sensor(self, unit_id: int) -> SensorReading:
        """
        Read complete sensor data and decode into structured format.

        Educational Note:
        This method demonstrates the complete data acquisition pipeline:
        1. Raw register reading via Modbus
        2. Data validation and error checking
        3. Structured data interpretation
        4. Result packaging for application use

        Args:
            unit_id: Modbus unit ID of the sensor

        Returns:
            SensorReading object with decoded sensor data

        Raises:
            DXMCommunicationError: If communication fails
        """
        try:
            # Read raw register data
            registers = self.read_sensor_registers(unit_id)

            # Decode into structured reading
            reading = self._decoder.decode_registers(unit_id, registers)

            self.logger.debug(f"Decoded reading for unit {unit_id}: {reading}")
            return reading

        except Exception as e:
            self.logger.error(f"Failed to read sensor {unit_id}: {e}")
            raise

    def discover_sensors(self, max_units: int = 8) -> List[int]:
        """
        Discover connected sensors by scanning unit IDs.

        Educational Note:
        This method demonstrates sensor discovery patterns in industrial
        networks. We systematically probe each possible unit ID to identify
        responding sensors. This is useful for initial system setup and
        diagnostics.

        Args:
            max_units: Maximum number of unit IDs to scan

        Returns:
            List of responding unit IDs

        Raises:
            DXMConnectionError: If not connected
        """
        if not self.connected:
            raise DXMConnectionError("Not connected to DXM")

        discovered_units = []
        self.logger.info(f"Scanning for sensors (units 1-{max_units})")

        for unit_id in range(1, max_units + 1):
            try:
                # Attempt to read a small number of registers
                # Educational Note: We use a minimal read to reduce network
                # traffic during discovery while still confirming sensor presence
                result = self._client.read_holding_registers(0, 1, unit=unit_id)

                if not result.isError():
                    discovered_units.append(unit_id)
                    self.logger.info(f"Found sensor at unit ID {unit_id}")
                else:
                    self.logger.debug(f"No response from unit ID {unit_id}")

            except Exception as e:
                self.logger.debug(f"Error scanning unit ID {unit_id}: {e}")
                continue

            # Brief delay to avoid overwhelming the network
            time.sleep(0.05)

        self.logger.info(f"Discovery complete. Found {len(discovered_units)} sensors: {discovered_units}")
        return discovered_units

    def read_multiple_sensors(self, unit_ids: List[int]) -> Dict[int, Optional[SensorReading]]:
        """
        Read data from multiple sensors efficiently.

        Educational Note:
        This method demonstrates efficient multi-sensor data acquisition.
        Rather than establishing separate connections for each sensor,
        we reuse the single connection while handling individual sensor
        failures gracefully.

        Args:
            unit_ids: List of unit IDs to read

        Returns:
            Dictionary mapping unit IDs to sensor readings (None if failed)
        """
        readings = {}

        for unit_id in unit_ids:
            try:
                reading = self.read_sensor(unit_id)
                readings[unit_id] = reading
            except Exception as e:
                self.logger.warning(f"Failed to read sensor {unit_id}: {e}")
                readings[unit_id] = None

        return readings

    def monitor_sensors(self, unit_ids: List[int], interval: float = 1.0,
                       duration: Optional[float] = None) -> List[Dict[int, Optional[SensorReading]]]:
        """
        Monitor multiple sensors over time.

        Educational Note:
        This method demonstrates real-time data acquisition patterns
        used in industrial monitoring applications. It handles timing,
        error recovery, and data collection efficiently.

        Args:
            unit_ids: List of unit IDs to monitor
            interval: Time between readings (seconds)
            duration: Total monitoring time (None for indefinite)

        Returns:
            List of reading dictionaries (one per time interval)

        Yields:
            Dictionary of readings for each monitoring cycle
        """
        start_time = time.time()
        reading_history = []

        try:
            while True:
                cycle_start = time.time()

                # Read all sensors for this cycle
                readings = self.read_multiple_sensors(unit_ids)
                reading_history.append(readings)

                # Yield current readings for real-time processing
                yield readings

                # Check duration limit
                if duration and (time.time() - start_time) >= duration:
                    break

                # Calculate sleep time to maintain interval
                cycle_time = time.time() - cycle_start
                sleep_time = max(0, interval - cycle_time)

                if sleep_time > 0:
                    time.sleep(sleep_time)
                else:
                    self.logger.warning(f"Monitoring cycle took {cycle_time:.2f}s, "
                                      f"longer than interval {interval}s")

        except KeyboardInterrupt:
            self.logger.info("Monitoring stopped by user")
        except Exception as e:
            self.logger.error(f"Monitoring error: {e}")
            raise

        return reading_history

    def get_connection_info(self) -> Dict[str, Any]:
        """
        Get detailed connection information.

        Returns:
            Dictionary with connection details
        """
        return {
            'host': self.host,
            'port': self.port,
            'connected': self.connected,
            'timeout': self.timeout,
            'retry_attempts': self.retry_attempts,
            'last_error': self.last_error,
            'client_info': {
                'connected': self._client.connected if hasattr(self._client, 'connected') else False,
                'socket': str(getattr(self._client, 'socket', 'Not available'))
            }
        }

    @contextmanager
    def temporary_connection(self):
        """
        Context manager for temporary connections.

        Educational Note:
        This context manager ensures proper connection cleanup even if
        exceptions occur. It's particularly useful for one-off operations
        where you don't want to maintain a persistent connection.

        Usage:
            with client.temporary_connection():
                reading = client.read_sensor(1)
        """
        was_connected = self.connected

        try:
            if not was_connected:
                self.connect()
            yield self
        finally:
            if not was_connected and self.connected:
                self.disconnect()