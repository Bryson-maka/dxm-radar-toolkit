"""
DXM Radar Toolkit

Toolkit for Banner DXM wireless controllers and radar sensors via Modbus TCP.

Components:
- DXMClient: Modbus TCP client for DXM communication
- SensorDecoder: Interprets register data into sensor readings
- CLI: Command-line interface
- Utils: Helper functions for formatting and validation
"""

__version__ = "1.0.0"
__author__ = "Industrial Automation Engineer"
__email__ = "engineer@example.com"

# Import main classes for easy access
from .dxm_client import DXMClient
from .sensor_decoder import SensorDecoder, SensorReading, SensorStatus
from .utils import format_distance, format_signal_quality, validate_ip_address

__all__ = [
    "DXMClient",
    "SensorDecoder",
    "SensorReading",
    "SensorStatus",
    "format_distance",
    "format_signal_quality",
    "validate_ip_address"
]