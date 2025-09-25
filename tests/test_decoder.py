#!/usr/bin/env python3
"""
Unit tests for the SensorDecoder module.

This test suite validates the sensor decoder functionality including
register interpretation, data validation, and error handling.

Educational Focus:
- Unit testing patterns for industrial applications
- Data validation and edge case testing
- Mock testing for hardware-dependent code
- Test-driven development principles

Run tests with:
    python -m pytest tests/test_decoder.py -v
    python tests/test_decoder.py  # Direct execution
"""

import unittest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

import sys
from pathlib import Path

# Add parent directory to path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from dxm_toolkit.sensor_decoder import SensorDecoder, SensorReading, SensorStatus


class TestSensorDecoder(unittest.TestCase):
    """
    Test cases for the SensorDecoder class.

    Educational Note:
    This test class demonstrates comprehensive testing patterns
    for data interpretation modules in industrial applications.
    """

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.decoder = SensorDecoder()

    def test_decoder_initialization(self):
        """Test that decoder initializes correctly."""
        self.assertIsInstance(self.decoder, SensorDecoder)
        self.assertEqual(self.decoder.STATUS_REGISTER, 0)
        self.assertEqual(self.decoder.BDC_REGISTER, 1)
        self.assertEqual(self.decoder.DISTANCE_REGISTER, 2)
        self.assertEqual(self.decoder.SIGNAL_QUALITY_REGISTER, 3)

    def test_decode_normal_operation(self):
        """Test decoding of normal sensor operation."""
        # Test data representing normal operation
        unit_id = 1
        registers = [303, 0, 1250, 45]  # Normal status, no BDC, 1250mm, signal 45

        reading = self.decoder.decode_registers(unit_id, registers)

        # Verify basic attributes
        self.assertEqual(reading.unit_id, unit_id)
        self.assertEqual(reading.status, SensorStatus.NORMAL)
        self.assertEqual(reading.status_raw, 303)
        self.assertEqual(reading.bdc_states, 0)
        self.assertEqual(reading.distance_raw, 1250)
        self.assertEqual(reading.distance_mm, 1250)
        self.assertEqual(reading.signal_quality, 45)
        self.assertTrue(reading.connected)
        self.assertTrue(reading.valid)

        # Verify timestamp is recent
        time_diff = datetime.now() - reading.timestamp
        self.assertLess(time_diff.total_seconds(), 1.0)

    def test_decode_out_of_range(self):
        """Test decoding of out-of-range condition."""
        unit_id = 2
        registers = [271, 0, 65535, 12]  # Out of range status

        reading = self.decoder.decode_registers(unit_id, registers)

        self.assertEqual(reading.status, SensorStatus.OUT_OF_RANGE)
        self.assertEqual(reading.distance_raw, 65535)
        self.assertIsNone(reading.distance_mm)  # Should be None for out of range
        self.assertTrue(reading.connected)  # Sensor connected but no target

    def test_decode_disconnected_sensor(self):
        """Test decoding of disconnected sensor."""
        unit_id = 3
        registers = [0, 0, 0, 0]  # All zeros indicate disconnected

        reading = self.decoder.decode_registers(unit_id, registers)

        self.assertEqual(reading.status, SensorStatus.ERROR)
        self.assertEqual(reading.distance_raw, 0)
        self.assertIsNone(reading.distance_mm)
        self.assertFalse(reading.connected)

    def test_decode_unknown_status(self):
        """Test handling of unknown status codes."""
        unit_id = 4
        registers = [999, 0, 1000, 30]  # Unknown status code

        reading = self.decoder.decode_registers(unit_id, registers)

        self.assertEqual(reading.status, SensorStatus.UNKNOWN)
        self.assertEqual(reading.status_raw, 999)
        self.assertEqual(reading.distance_mm, 1000)  # Distance should still be valid

    def test_decode_with_bdc_states(self):
        """Test decoding with BDC diagnostic states."""
        unit_id = 5
        registers = [303, 0x0007, 1500, 55]  # Normal with BDC flags

        reading = self.decoder.decode_registers(unit_id, registers)

        self.assertEqual(reading.status, SensorStatus.NORMAL)
        self.assertEqual(reading.bdc_states, 0x0007)
        self.assertEqual(reading.distance_mm, 1500)

    def test_decode_insufficient_registers(self):
        """Test error handling for insufficient register data."""
        unit_id = 6
        registers = [303, 0, 1250]  # Only 3 registers instead of 4

        with self.assertRaises(ValueError) as context:
            self.decoder.decode_registers(unit_id, registers)

        self.assertIn("Expected at least 4 registers", str(context.exception))

    def test_decode_empty_registers(self):
        """Test error handling for empty register list."""
        unit_id = 7
        registers = []

        with self.assertRaises(ValueError) as context:
            self.decoder.decode_registers(unit_id, registers)

        self.assertIn("Expected at least 4 registers", str(context.exception))

    def test_decode_single_register(self):
        """Test single register decoding functionality."""
        # Test status register
        status_result = self.decoder.decode_single_register(0, 303)
        self.assertEqual(status_result['register_name'], 'Status')
        self.assertEqual(status_result['interpretation'], 'NORMAL')

        # Test BDC register
        bdc_result = self.decoder.decode_single_register(1, 0x0003)
        self.assertEqual(bdc_result['register_name'], 'BDC States')

        # Test distance register
        distance_result = self.decoder.decode_single_register(2, 1500)
        self.assertEqual(distance_result['register_name'], 'Distance')
        self.assertIn('1500', distance_result['interpretation'])

        # Test signal quality register
        signal_result = self.decoder.decode_single_register(3, 45)
        self.assertEqual(signal_result['register_name'], 'Signal Quality')

        # Test unknown register
        unknown_result = self.decoder.decode_single_register(10, 123)
        self.assertEqual(unknown_result['interpretation'], 'Unknown register')

    def test_validate_reading_normal(self):
        """Test validation of normal sensor reading."""
        reading = SensorReading(
            unit_id=1,
            timestamp=datetime.now(),
            status=SensorStatus.NORMAL,
            status_raw=303,
            bdc_states=0,
            distance_raw=1250,
            signal_quality=45
        )

        issues = self.decoder.validate_reading(reading)
        self.assertEqual(len(issues), 0)  # Should have no validation issues

    def test_validate_reading_issues(self):
        """Test validation of problematic sensor readings."""
        # Test unknown status
        reading_unknown_status = SensorReading(
            unit_id=1,
            timestamp=datetime.now(),
            status=SensorStatus.UNKNOWN,
            status_raw=999,
            bdc_states=0,
            distance_raw=1250,
            signal_quality=45
        )

        issues = self.decoder.validate_reading(reading_unknown_status)
        self.assertGreater(len(issues), 0)
        self.assertTrue(any("Unknown status code" in issue for issue in issues))

        # Test invalid signal quality
        reading_bad_signal = SensorReading(
            unit_id=1,
            timestamp=datetime.now(),
            status=SensorStatus.NORMAL,
            status_raw=303,
            bdc_states=0,
            distance_raw=1250,
            signal_quality=-5  # Invalid negative signal
        )

        issues = self.decoder.validate_reading(reading_bad_signal)
        self.assertTrue(any("Invalid signal quality" in issue for issue in issues))

        # Test future timestamp
        reading_future_time = SensorReading(
            unit_id=1,
            timestamp=datetime.now() + timedelta(hours=1),
            status=SensorStatus.NORMAL,
            status_raw=303,
            bdc_states=0,
            distance_raw=1250,
            signal_quality=45
        )

        issues = self.decoder.validate_reading(reading_future_time)
        self.assertTrue(any("timestamp is in the future" in issue for issue in issues))

    def test_get_register_info(self):
        """Test register information retrieval."""
        register_info = self.decoder.get_register_info()

        self.assertIsInstance(register_info, dict)
        self.assertIn(0, register_info)  # Status register
        self.assertIn(1, register_info)  # BDC register
        self.assertIn(2, register_info)  # Distance register
        self.assertIn(3, register_info)  # Signal quality register

        # Check status register info
        status_info = register_info[0]
        self.assertEqual(status_info['name'], 'Status')
        self.assertIn('description', status_info)
        self.assertIn('values', status_info)

    def test_analyze_register_pattern_empty(self):
        """Test pattern analysis with no readings."""
        analysis = self.decoder.analyze_register_pattern([])
        self.assertIn('error', analysis)

    def test_analyze_register_pattern_single_reading(self):
        """Test pattern analysis with single reading."""
        reading = SensorReading(
            unit_id=1,
            timestamp=datetime.now(),
            status=SensorStatus.NORMAL,
            status_raw=303,
            bdc_states=0,
            distance_raw=1250,
            signal_quality=45
        )

        analysis = self.decoder.analyze_register_pattern([reading])

        self.assertEqual(analysis['reading_count'], 1)
        self.assertIn('status_distribution', analysis)
        self.assertIn('NORMAL', analysis['status_distribution'])
        self.assertEqual(analysis['connection_stability'], 100.0)

    def test_analyze_register_pattern_multiple_readings(self):
        """Test pattern analysis with multiple readings."""
        base_time = datetime.now()
        readings = []

        # Create test readings with variations
        for i in range(10):
            reading = SensorReading(
                unit_id=1,
                timestamp=base_time + timedelta(seconds=i),
                status=SensorStatus.NORMAL if i < 8 else SensorStatus.OUT_OF_RANGE,
                status_raw=303 if i < 8 else 271,
                bdc_states=0,
                distance_raw=1250 + i * 10,  # Varying distance
                signal_quality=45 - i  # Decreasing signal quality
            )
            readings.append(reading)

        analysis = self.decoder.analyze_register_pattern(readings)

        self.assertEqual(analysis['reading_count'], 10)
        self.assertAlmostEqual(analysis['time_span'], 9.0, places=1)
        self.assertIn('NORMAL', analysis['status_distribution'])
        self.assertIn('OUT_OF_RANGE', analysis['status_distribution'])

        # Check distance statistics
        self.assertIn('distance_stats', analysis)
        distance_stats = analysis['distance_stats']
        self.assertEqual(distance_stats['min'], 1250)
        self.assertEqual(distance_stats['max'], 1320)  # 1250 + 7*10 (last normal reading)

        # Check signal quality statistics
        self.assertIn('signal_quality_stats', analysis)
        signal_stats = analysis['signal_quality_stats']
        self.assertEqual(signal_stats['min'], 36)  # 45 - 9
        self.assertEqual(signal_stats['max'], 45)


class TestSensorReading(unittest.TestCase):
    """
    Test cases for the SensorReading dataclass.

    Educational Note:
    Testing dataclass behavior and methods demonstrates
    proper testing of data structures in industrial applications.
    """

    def setUp(self):
        """Set up test reading."""
        self.reading = SensorReading(
            unit_id=1,
            timestamp=datetime.now(),
            status=SensorStatus.NORMAL,
            status_raw=303,
            bdc_states=0,
            distance_raw=1250,
            signal_quality=45
        )

    def test_sensor_reading_creation(self):
        """Test basic SensorReading creation."""
        self.assertEqual(self.reading.unit_id, 1)
        self.assertEqual(self.reading.status, SensorStatus.NORMAL)
        self.assertEqual(self.reading.distance_mm, 1250)
        self.assertTrue(self.reading.connected)
        self.assertTrue(self.reading.valid)

    def test_post_init_disconnected(self):
        """Test post-init processing for disconnected sensor."""
        reading = SensorReading(
            unit_id=2,
            timestamp=datetime.now(),
            status=SensorStatus.ERROR,
            status_raw=0,
            bdc_states=0,
            distance_raw=0,  # Zero indicates disconnected
            signal_quality=0
        )

        self.assertFalse(reading.connected)
        self.assertIsNone(reading.distance_mm)

    def test_post_init_out_of_range(self):
        """Test post-init processing for out-of-range condition."""
        reading = SensorReading(
            unit_id=3,
            timestamp=datetime.now(),
            status=SensorStatus.OUT_OF_RANGE,
            status_raw=271,
            bdc_states=0,
            distance_raw=65535,  # 65535 indicates out of range
            signal_quality=20
        )

        self.assertTrue(reading.connected)  # Sensor connected but no target
        self.assertIsNone(reading.distance_mm)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        reading_dict = self.reading.to_dict()

        self.assertIsInstance(reading_dict, dict)
        self.assertEqual(reading_dict['unit_id'], 1)
        self.assertEqual(reading_dict['status'], 'NORMAL')
        self.assertEqual(reading_dict['distance_mm'], 1250)
        self.assertEqual(reading_dict['connected'], True)
        self.assertIn('timestamp', reading_dict)

    def test_format_for_display(self):
        """Test display formatting."""
        # Test normal formatting
        display_text = self.reading.format_for_display()
        self.assertIn("Unit 1", display_text)
        self.assertIn("NORMAL", display_text)
        self.assertIn("1250", display_text)

        # Test with different unit
        display_cm = self.reading.format_for_display(distance_unit="cm")
        self.assertIn("125.0 cm", display_cm)

        # Test without colors
        display_no_color = self.reading.format_for_display(use_colors=False)
        self.assertIsInstance(display_no_color, str)


class TestSensorDecoderEdgeCases(unittest.TestCase):
    """
    Test edge cases and error conditions for SensorDecoder.

    Educational Note:
    Edge case testing is crucial for industrial applications
    where unexpected conditions must be handled gracefully.
    """

    def setUp(self):
        """Set up test decoder."""
        self.decoder = SensorDecoder()

    def test_large_register_values(self):
        """Test handling of maximum register values."""
        unit_id = 1
        registers = [65535, 65535, 65535, 65535]  # Maximum 16-bit values

        reading = self.decoder.decode_registers(unit_id, registers)

        self.assertEqual(reading.status_raw, 65535)
        self.assertEqual(reading.distance_raw, 65535)
        self.assertIsNone(reading.distance_mm)  # Should interpret as out of range

    def test_negative_values_as_unsigned(self):
        """Test that negative values are handled as unsigned 16-bit."""
        # Note: In practice, Modbus registers are unsigned 16-bit
        unit_id = 1
        registers = [303, 0, 1250, 32768]  # 32768 = 0x8000

        reading = self.decoder.decode_registers(unit_id, registers)

        self.assertEqual(reading.signal_quality, 32768)  # Should be treated as positive

    def test_mixed_valid_invalid_conditions(self):
        """Test mixed valid/invalid register combinations."""
        # Valid distance but error status
        unit_id = 1
        registers = [0, 0, 1250, 0]  # Error status but distance present

        reading = self.decoder.decode_registers(unit_id, registers)
        issues = self.decoder.validate_reading(reading)

        # Should flag this as inconsistent
        self.assertGreater(len(issues), 0)

    def test_boundary_distance_values(self):
        """Test boundary conditions for distance values."""
        test_cases = [
            (1, "Minimum valid distance"),
            (30000, "Maximum typical range"),
            (65534, "Just below out-of-range marker"),
            (65535, "Out-of-range marker")
        ]

        for distance_value, description in test_cases:
            with self.subTest(distance=distance_value, desc=description):
                registers = [303, 0, distance_value, 45]
                reading = self.decoder.decode_registers(1, registers)

                if distance_value == 65535:
                    self.assertIsNone(reading.distance_mm)
                else:
                    self.assertEqual(reading.distance_mm, distance_value)


class TestMockIntegration(unittest.TestCase):
    """
    Test decoder with mocked data sources.

    Educational Note:
    Mocking allows testing of decoder logic without requiring
    physical hardware, which is essential for automated testing
    in industrial software development.
    """

    def setUp(self):
        """Set up decoder for mock testing."""
        self.decoder = SensorDecoder()

    @patch('dxm_toolkit.sensor_decoder.datetime')
    def test_decode_with_mocked_timestamp(self, mock_datetime):
        """Test decoding with controlled timestamp."""
        # Mock datetime.now() to return fixed time
        fixed_time = datetime(2023, 10, 15, 14, 30, 25)
        mock_datetime.now.return_value = fixed_time

        registers = [303, 0, 1250, 45]
        reading = self.decoder.decode_registers(1, registers)

        self.assertEqual(reading.timestamp, fixed_time)

    def test_decode_with_simulated_sensor_data(self):
        """Test decoder with realistic simulated sensor data patterns."""
        # Simulate a sensor detecting a moving object
        time_base = datetime.now()
        distances = [2000, 1950, 1900, 1850, 1800, 1750]  # Approaching object
        signals = [30, 35, 40, 45, 50, 55]  # Improving signal

        readings = []
        for i, (distance, signal) in enumerate(zip(distances, signals)):
            registers = [303, 0, distance, signal]
            reading = self.decoder.decode_registers(1, registers)
            readings.append(reading)

        # Analyze the pattern
        analysis = self.decoder.analyze_register_pattern(readings)

        self.assertEqual(analysis['reading_count'], 6)
        self.assertEqual(analysis['distance_stats']['min'], 1750)
        self.assertEqual(analysis['distance_stats']['max'], 2000)
        self.assertEqual(analysis['signal_quality_stats']['min'], 30)
        self.assertEqual(analysis['signal_quality_stats']['max'], 55)


def run_manual_tests():
    """
    Run manual tests that require user verification.

    Educational Note:
    Some tests require human interpretation or cannot be easily automated.
    These manual tests complement automated unit tests.
    """
    print("Manual Test Suite for DXM Toolkit")
    print("=" * 40)

    decoder = SensorDecoder()

    # Test 1: Display formatting
    print("\nTest 1: Display Formatting")
    reading = SensorReading(
        unit_id=1,
        timestamp=datetime.now(),
        status=SensorStatus.NORMAL,
        status_raw=303,
        bdc_states=0,
        distance_raw=1250,
        signal_quality=45
    )

    print("With colors:", reading.format_for_display(use_colors=True))
    print("Without colors:", reading.format_for_display(use_colors=False))

    # Test 2: Register information display
    print("\nTest 2: Register Information")
    register_info = decoder.get_register_info()
    for addr, info in register_info.items():
        print(f"Register {addr}: {info['name']} - {info['description']}")

    # Test 3: Status code interpretation
    print("\nTest 3: Status Code Interpretation")
    test_statuses = [303, 271, 0, 999]
    for status_code in test_statuses:
        result = decoder.decode_single_register(0, status_code)
        print(f"Status {status_code}: {result['interpretation']}")

    print("\nManual tests completed.")


if __name__ == '__main__':
    # Run unit tests
    print("Running automated unit tests...")
    unittest.main(verbosity=2, exit=False)

    # Run manual tests
    print("\n" + "=" * 50)
    run_manual_tests()