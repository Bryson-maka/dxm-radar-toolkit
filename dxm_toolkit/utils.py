#!/usr/bin/env python3
"""
Utility functions for DXM Radar Toolkit

This module provides helper functions for data formatting, validation,
and common operations used throughout the toolkit.

Educational Focus:
- Data formatting and presentation patterns
- Input validation techniques
- Unit conversion implementations
- Color-coded terminal output
"""

import re
import socket
import struct
from typing import Union, Optional, Tuple
from datetime import datetime

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)  # Initialize colorama for cross-platform color support
    COLORS_AVAILABLE = True
except ImportError:
    # Gracefully handle missing colorama dependency
    COLORS_AVAILABLE = False
    # Create dummy color constants
    class _DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Back = Style = _DummyColor()


def validate_ip_address(ip: str) -> bool:
    """
    Validate IPv4 address format.

    Educational Note:
    This function demonstrates input validation patterns commonly used
    in industrial networking applications. Proper validation prevents
    runtime errors and improves user experience.

    Args:
        ip (str): IP address string to validate

    Returns:
        bool: True if valid IPv4 address, False otherwise

    Example:
        >>> validate_ip_address("192.168.0.1")
        True
        >>> validate_ip_address("256.1.1.1")
        False
    """
    try:
        # Use socket.inet_aton for robust IP validation
        # This handles edge cases better than regex-only approaches
        socket.inet_aton(ip)

        # Additional check for proper dotted decimal notation
        parts = ip.split('.')
        if len(parts) != 4:
            return False

        # Ensure each octet is within valid range (0-255)
        for part in parts:
            if not (0 <= int(part) <= 255):
                return False

        return True
    except (socket.error, ValueError):
        return False


def format_distance(distance_raw: int, unit: str = "mm", precision: int = 1) -> str:
    """
    Format distance reading with appropriate unit conversion.

    Educational Note:
    Industrial sensors often provide raw data that needs conversion
    for human-readable display. This function demonstrates unit
    conversion patterns and handles special cases like disconnected
    sensors or out-of-range readings.

    Args:
        distance_raw (int): Raw distance value from sensor (in mm)
        unit (str): Target unit ("mm", "cm", "m", "in", "ft")
        precision (int): Number of decimal places

    Returns:
        str: Formatted distance string with unit

    Special Values:
        0: Sensor disconnected
        65535: Out of range (OOR)
    """
    # Handle special sensor states
    if distance_raw == 0:
        return "DISCONNECTED"
    elif distance_raw == 65535:
        return "OUT OF RANGE"

    # Convert from mm to target unit
    conversions = {
        "mm": 1.0,
        "cm": 0.1,
        "m": 0.001,
        "in": 0.0393701,  # mm to inches
        "ft": 0.00328084  # mm to feet
    }

    if unit not in conversions:
        unit = "mm"  # Default fallback

    converted = distance_raw * conversions[unit]
    return f"{converted:.{precision}f} {unit}"


def format_signal_quality(excess_gain: int) -> str:
    """
    Format signal quality (excess gain) with interpretation.

    Educational Note:
    Radar sensors provide signal quality metrics that help assess
    measurement reliability. Excess gain indicates how much signal
    strength is available beyond the minimum required for detection.

    Args:
        excess_gain (int): Raw excess gain value from sensor

    Returns:
        str: Formatted signal quality with interpretation
    """
    if excess_gain == 0:
        return "No Signal (0)"
    elif excess_gain < 10:
        return f"Weak Signal ({excess_gain})"
    elif excess_gain < 50:
        return f"Good Signal ({excess_gain})"
    else:
        return f"Strong Signal ({excess_gain})"


def format_bdc_states(bdc_value: int) -> str:
    """
    Format BDC (Binary Diagnostic Code) states into human-readable form.

    Educational Note:
    BDC states provide diagnostic information about sensor operation.
    Each bit in the BDC value represents a specific diagnostic condition.
    This demonstrates bit-level data interpretation common in industrial
    protocols.

    Args:
        bdc_value (int): Raw BDC value from sensor

    Returns:
        str: Human-readable BDC interpretation
    """
    if bdc_value == 0:
        return "No Diagnostics"

    # Common BDC bit interpretations (these may vary by sensor model)
    diagnostics = []
    if bdc_value & 0x01:
        diagnostics.append("Configuration Error")
    if bdc_value & 0x02:
        diagnostics.append("Temperature Warning")
    if bdc_value & 0x04:
        diagnostics.append("Voltage Warning")
    if bdc_value & 0x08:
        diagnostics.append("Signal Quality Warning")

    if diagnostics:
        return " | ".join(diagnostics) + f" (0x{bdc_value:04X})"
    else:
        return f"Unknown Diagnostic (0x{bdc_value:04X})"


def colorize_text(text: str, color: str, use_colors: bool = True) -> str:
    """
    Apply color to text for terminal output.

    Educational Note:
    Color-coded output significantly improves user experience in CLI
    applications. This function demonstrates graceful degradation when
    color support is not available.

    Args:
        text (str): Text to colorize
        color (str): Color name ("red", "green", "yellow", "blue", etc.)
        use_colors (bool): Enable/disable color output

    Returns:
        str: Colorized text (or plain text if colors disabled)
    """
    if not use_colors or not COLORS_AVAILABLE:
        return text

    color_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "bright_red": Fore.LIGHTRED_EX,
        "bright_green": Fore.LIGHTGREEN_EX,
        "bright_yellow": Fore.LIGHTYELLOW_EX,
    }

    color_code = color_map.get(color.lower(), "")
    return f"{color_code}{text}{Style.RESET_ALL}"


def format_timestamp(include_time: bool = True) -> str:
    """
    Generate formatted timestamp for logging and display.

    Args:
        include_time (bool): Include time portion or date only

    Returns:
        str: Formatted timestamp
    """
    now = datetime.now()
    if include_time:
        return now.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return now.strftime("%Y-%m-%d")


def validate_unit_id(unit_id: Union[int, str]) -> bool:
    """
    Validate Modbus unit ID range.

    Educational Note:
    Modbus unit IDs must be within the valid range (1-247 for TCP).
    Unit ID 0 is reserved for broadcast messages.

    Args:
        unit_id: Unit ID to validate

    Returns:
        bool: True if valid unit ID
    """
    try:
        uid = int(unit_id)
        return 1 <= uid <= 247
    except (ValueError, TypeError):
        return False


def bytes_to_int16(byte_data: bytes, big_endian: bool = True) -> int:
    """
    Convert byte data to signed 16-bit integer.

    Educational Note:
    Modbus registers are 16-bit values, but the byte order (endianness)
    can vary between devices. This function handles both big-endian
    and little-endian interpretations.

    Args:
        byte_data (bytes): Raw byte data (2 bytes)
        big_endian (bool): True for big-endian, False for little-endian

    Returns:
        int: 16-bit signed integer value

    Raises:
        ValueError: If byte_data is not exactly 2 bytes
    """
    if len(byte_data) != 2:
        raise ValueError("Expected exactly 2 bytes for int16 conversion")

    format_char = ">h" if big_endian else "<h"
    return struct.unpack(format_char, byte_data)[0]


def int16_to_bytes(value: int, big_endian: bool = True) -> bytes:
    """
    Convert signed 16-bit integer to byte data.

    Args:
        value (int): Integer value to convert
        big_endian (bool): True for big-endian, False for little-endian

    Returns:
        bytes: 2-byte representation
    """
    format_char = ">h" if big_endian else "<h"
    return struct.pack(format_char, value)


def calculate_checksum(data: bytes) -> int:
    """
    Calculate simple checksum for data validation.

    Educational Note:
    While Modbus TCP includes its own error detection, additional
    checksums can be useful for data integrity verification in
    industrial applications.

    Args:
        data (bytes): Data to checksum

    Returns:
        int: Simple sum checksum (modulo 65536)
    """
    return sum(data) % 65536


def parse_version_string(version_str: str) -> Tuple[int, int, int]:
    """
    Parse semantic version string into components.

    Args:
        version_str (str): Version string (e.g., "1.2.3")

    Returns:
        Tuple[int, int, int]: Major, minor, patch version numbers

    Raises:
        ValueError: If version string format is invalid
    """
    pattern = r"^(\d+)\.(\d+)\.(\d+)$"
    match = re.match(pattern, version_str.strip())

    if not match:
        raise ValueError(f"Invalid version string format: {version_str}")

    return tuple(int(x) for x in match.groups())


def format_hex_dump(data: bytes, bytes_per_line: int = 16) -> str:
    """
    Format byte data as hexadecimal dump for debugging.

    Educational Note:
    Hex dumps are invaluable for debugging Modbus communications.
    This function creates a readable format showing both hex values
    and ASCII representation where applicable.

    Args:
        data (bytes): Data to format
        bytes_per_line (int): Number of bytes per line

    Returns:
        str: Formatted hex dump
    """
    lines = []
    for i in range(0, len(data), bytes_per_line):
        chunk = data[i:i + bytes_per_line]

        # Format hex values
        hex_str = " ".join(f"{b:02X}" for b in chunk)
        hex_str = hex_str.ljust(bytes_per_line * 3 - 1)

        # Format ASCII representation
        ascii_str = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)

        # Address offset
        addr_str = f"{i:04X}"

        lines.append(f"{addr_str}: {hex_str} | {ascii_str}")

    return "\n".join(lines)