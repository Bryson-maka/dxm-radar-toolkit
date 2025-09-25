#!/usr/bin/env python3
"""
Sensor Decoder for DXM Radar Toolkit

This module handles the interpretation of raw Modbus register data from
DXM-connected radar sensors. It translates low-level register values
into meaningful sensor readings and status information.

Educational Focus:
- Modbus register interpretation patterns
- IO-Link to Modbus data mapping concepts
- Industrial sensor data structures
- Status code interpretation and error handling
"""

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Dict, List, Optional, Any, Union
from datetime import datetime

from .utils import format_distance, format_signal_quality, format_bdc_states


class SensorStatus(IntEnum):
    """
    Enumeration of possible sensor status values.

    Educational Note:
    These values are derived from actual DXM radar sensor behavior.
    Understanding these status codes is crucial for proper sensor
    integration and diagnostics.

    Based on our discoveries:
    - 303 (0x012F): Normal operation
    - 271 (0x010F): Out of range condition
    """
    NORMAL = 303          # Sensor operating normally
    OUT_OF_RANGE = 271    # Target beyond sensor range
    ERROR = 0             # General error condition
    UNKNOWN = -1          # Unrecognized status code


@dataclass
class SensorReading:
    """
    Complete sensor reading data structure.

    Educational Note:
    This dataclass demonstrates how to structure complex sensor data
    in a way that's both programmatically useful and human-readable.
    The dataclass decorator automatically generates __init__, __repr__,
    and __eq__ methods.

    Attributes:
        unit_id: Modbus unit ID of the sensor
        timestamp: When the reading was taken
        status: Current sensor operational status
        status_raw: Raw status register value (for debugging)
        bdc_states: Binary Diagnostic Code states
        distance_mm: Distance measurement in millimeters
        distance_raw: Raw distance register value
        signal_quality: Signal quality (excess gain)
        connected: Whether sensor is connected and responding
        valid: Whether the reading contains valid data
    """
    unit_id: int
    timestamp: datetime
    status: SensorStatus
    status_raw: int
    bdc_states: int
    distance_mm: Optional[int]
    distance_raw: int
    signal_quality: int
    connected: bool = True
    valid: bool = True

    def __post_init__(self):
        """
        Post-initialization processing to derive additional fields.

        Educational Note:
        __post_init__ is called after dataclass initialization,
        allowing for computed fields and validation logic.
        """
        # Determine connection status from distance reading
        if self.distance_raw == 0:
            self.connected = False
            self.distance_mm = None
        elif self.distance_raw == 65535:
            self.connected = True
            self.distance_mm = None  # Out of range, but sensor is connected
        else:
            self.connected = True
            self.distance_mm = self.distance_raw

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert reading to dictionary format.

        Educational Note:
        Dictionary serialization is useful for JSON export,
        logging, and data analysis applications.

        Returns:
            Dict containing all reading data
        """
        return {
            'unit_id': self.unit_id,
            'timestamp': self.timestamp.isoformat(),
            'status': self.status.name,
            'status_raw': self.status_raw,
            'bdc_states': self.bdc_states,
            'distance_mm': self.distance_mm,
            'distance_raw': self.distance_raw,
            'signal_quality': self.signal_quality,
            'connected': self.connected,
            'valid': self.valid
        }

    def format_for_display(self, distance_unit: str = "mm", use_colors: bool = True) -> str:
        """
        Format reading for human-readable display.

        Args:
            distance_unit: Unit for distance display
            use_colors: Enable colored output

        Returns:
            Formatted string representation
        """
        from .utils import colorize_text

        # Format status with appropriate color
        if self.status == SensorStatus.NORMAL:
            status_text = colorize_text("NORMAL", "green", use_colors)
        elif self.status == SensorStatus.OUT_OF_RANGE:
            status_text = colorize_text("OUT OF RANGE", "yellow", use_colors)
        else:
            status_text = colorize_text("ERROR", "red", use_colors)

        # Format distance
        distance_text = format_distance(self.distance_raw, distance_unit)
        if not self.connected:
            distance_text = colorize_text(distance_text, "red", use_colors)
        elif self.distance_mm is None:
            distance_text = colorize_text(distance_text, "yellow", use_colors)

        # Format signal quality
        signal_text = format_signal_quality(self.signal_quality)

        return (f"Unit {self.unit_id}: {status_text} | "
                f"Distance: {distance_text} | "
                f"Signal: {signal_text}")


class SensorDecoder:
    """
    Main class for decoding DXM sensor register data.

    Educational Note:
    This class encapsulates all the knowledge about how DXM controllers
    map IO-Link sensor data to Modbus registers. Understanding this mapping
    is essential for integrating any IO-Link device with DXM systems.

    Register Mapping (based on our research):
    - Register 0: Status (303=Normal, 271=Out of Range)
    - Register 1: BDC States (Binary Diagnostic Codes)
    - Register 2: Distance (0=Disconnected, 65535=Out of Range)
    - Register 3: Signal Quality (Excess Gain)
    """

    # Define register addresses as class constants for clarity
    STATUS_REGISTER = 0
    BDC_REGISTER = 1
    DISTANCE_REGISTER = 2
    SIGNAL_QUALITY_REGISTER = 3

    # Minimum number of registers required for a complete reading
    MIN_REGISTERS = 4

    def __init__(self):
        """
        Initialize the sensor decoder.

        Educational Note:
        The decoder maintains no persistent state, making it thread-safe
        and suitable for concurrent use across multiple sensor connections.
        """
        self._status_map = self._build_status_map()

    def _build_status_map(self) -> Dict[int, SensorStatus]:
        """
        Build mapping of raw status values to SensorStatus enum.

        Educational Note:
        This demonstrates the factory pattern for creating lookup tables.
        As we discover more status codes through testing, we can easily
        extend this mapping.

        Returns:
            Dictionary mapping raw values to SensorStatus
        """
        return {
            303: SensorStatus.NORMAL,
            271: SensorStatus.OUT_OF_RANGE,
            0: SensorStatus.ERROR,
        }

    def decode_registers(self, unit_id: int, registers: List[int]) -> SensorReading:
        """
        Decode raw Modbus register data into structured sensor reading.

        Educational Note:
        This is the core decoding function that transforms low-level
        Modbus register values into meaningful sensor data. The function
        demonstrates error handling patterns for industrial data processing.

        Args:
            unit_id: Modbus unit ID of the sensor
            registers: List of register values (must be at least 4 values)

        Returns:
            SensorReading object with decoded data

        Raises:
            ValueError: If insufficient register data provided
        """
        if len(registers) < self.MIN_REGISTERS:
            raise ValueError(f"Expected at least {self.MIN_REGISTERS} registers, "
                           f"got {len(registers)}")

        # Extract raw register values
        status_raw = registers[self.STATUS_REGISTER]
        bdc_states = registers[self.BDC_REGISTER]
        distance_raw = registers[self.DISTANCE_REGISTER]
        signal_quality = registers[self.SIGNAL_QUALITY_REGISTER]

        # Decode status using our mapping
        status = self._status_map.get(status_raw, SensorStatus.UNKNOWN)

        # Create reading object
        reading = SensorReading(
            unit_id=unit_id,
            timestamp=datetime.now(),
            status=status,
            status_raw=status_raw,
            bdc_states=bdc_states,
            distance_raw=distance_raw,
            signal_quality=signal_quality
        )

        return reading

    def decode_single_register(self, register_address: int, value: int) -> Dict[str, Any]:
        """
        Decode a single register value with interpretation.

        Educational Note:
        This function is useful for debugging and exploratory analysis.
        It provides detailed interpretation of individual register values.

        Args:
            register_address: Modbus register address
            value: Raw register value

        Returns:
            Dictionary with decoded information
        """
        result = {
            'address': register_address,
            'raw_value': value,
            'hex_value': f"0x{value:04X}",
            'interpretation': 'Unknown register'
        }

        if register_address == self.STATUS_REGISTER:
            status = self._status_map.get(value, SensorStatus.UNKNOWN)
            result.update({
                'register_name': 'Status',
                'interpretation': status.name,
                'description': self._get_status_description(status)
            })

        elif register_address == self.BDC_REGISTER:
            result.update({
                'register_name': 'BDC States',
                'interpretation': format_bdc_states(value),
                'description': 'Binary Diagnostic Code states'
            })

        elif register_address == self.DISTANCE_REGISTER:
            result.update({
                'register_name': 'Distance',
                'interpretation': format_distance(value),
                'description': 'Distance measurement in millimeters'
            })

        elif register_address == self.SIGNAL_QUALITY_REGISTER:
            result.update({
                'register_name': 'Signal Quality',
                'interpretation': format_signal_quality(value),
                'description': 'Excess gain indicating signal strength'
            })

        return result

    def _get_status_description(self, status: SensorStatus) -> str:
        """
        Get human-readable description of sensor status.

        Args:
            status: SensorStatus enum value

        Returns:
            Descriptive text explaining the status
        """
        descriptions = {
            SensorStatus.NORMAL: "Sensor operating normally with valid readings",
            SensorStatus.OUT_OF_RANGE: "Target beyond sensor measurement range",
            SensorStatus.ERROR: "Sensor error or communication failure",
            SensorStatus.UNKNOWN: "Unrecognized status code - check sensor documentation"
        }
        return descriptions.get(status, "Unknown status condition")

    def validate_reading(self, reading: SensorReading) -> List[str]:
        """
        Validate sensor reading and return list of issues found.

        Educational Note:
        Data validation is crucial in industrial applications where
        invalid readings can lead to incorrect decisions. This function
        demonstrates comprehensive validation patterns.

        Args:
            reading: SensorReading to validate

        Returns:
            List of validation issues (empty if valid)
        """
        issues = []

        # Check for unknown status
        if reading.status == SensorStatus.UNKNOWN:
            issues.append(f"Unknown status code: {reading.status_raw}")

        # Validate distance reading consistency
        if reading.distance_raw == 0 and reading.connected:
            issues.append("Distance indicates disconnected but sensor shows connected")

        # Check signal quality range
        if reading.signal_quality < 0:
            issues.append(f"Invalid signal quality: {reading.signal_quality}")

        # Validate timestamp
        if reading.timestamp > datetime.now():
            issues.append("Reading timestamp is in the future")

        # Check for impossible distance values (sensor-specific limits)
        if (reading.distance_mm is not None and
            (reading.distance_mm < 0 or reading.distance_mm > 30000)):
            issues.append(f"Distance value outside expected range: {reading.distance_mm}mm")

        return issues

    def get_register_info(self) -> Dict[int, Dict[str, str]]:
        """
        Get information about all known registers.

        Educational Note:
        This method provides metadata about the register mapping,
        useful for documentation and debugging tools.

        Returns:
            Dictionary with register information
        """
        return {
            self.STATUS_REGISTER: {
                'name': 'Status',
                'description': 'Sensor operational status',
                'values': '303=Normal, 271=Out of Range, 0=Error'
            },
            self.BDC_REGISTER: {
                'name': 'BDC States',
                'description': 'Binary Diagnostic Code states',
                'values': 'Bitfield indicating diagnostic conditions'
            },
            self.DISTANCE_REGISTER: {
                'name': 'Distance',
                'description': 'Distance measurement in millimeters',
                'values': '0=Disconnected, 65535=Out of Range, 1-65534=Distance in mm'
            },
            self.SIGNAL_QUALITY_REGISTER: {
                'name': 'Signal Quality',
                'description': 'Signal strength indicator (excess gain)',
                'values': '0=No signal, >0=Signal strength level'
            }
        }

    def analyze_register_pattern(self, readings: List[SensorReading]) -> Dict[str, Any]:
        """
        Analyze patterns in multiple sensor readings.

        Educational Note:
        Pattern analysis helps identify sensor behavior trends,
        calibration issues, and environmental factors affecting
        sensor performance.

        Args:
            readings: List of SensorReading objects to analyze

        Returns:
            Dictionary with pattern analysis results
        """
        if not readings:
            return {'error': 'No readings provided'}

        analysis = {
            'reading_count': len(readings),
            'time_span': None,
            'status_distribution': {},
            'distance_stats': {},
            'signal_quality_stats': {},
            'connection_stability': 0.0
        }

        # Time span analysis
        if len(readings) > 1:
            timestamps = [r.timestamp for r in readings]
            time_span = max(timestamps) - min(timestamps)
            analysis['time_span'] = time_span.total_seconds()

        # Status distribution
        status_counts = {}
        for reading in readings:
            status_name = reading.status.name
            status_counts[status_name] = status_counts.get(status_name, 0) + 1
        analysis['status_distribution'] = status_counts

        # Distance statistics
        valid_distances = [r.distance_mm for r in readings if r.distance_mm is not None]
        if valid_distances:
            analysis['distance_stats'] = {
                'min': min(valid_distances),
                'max': max(valid_distances),
                'avg': sum(valid_distances) / len(valid_distances),
                'count': len(valid_distances)
            }

        # Signal quality statistics
        signal_qualities = [r.signal_quality for r in readings]
        analysis['signal_quality_stats'] = {
            'min': min(signal_qualities),
            'max': max(signal_qualities),
            'avg': sum(signal_qualities) / len(signal_qualities)
        }

        # Connection stability (percentage of connected readings)
        connected_count = sum(1 for r in readings if r.connected)
        analysis['connection_stability'] = connected_count / len(readings) * 100

        return analysis