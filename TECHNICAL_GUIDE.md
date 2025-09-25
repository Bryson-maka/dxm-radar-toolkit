# DXM Radar Technical Guide

## Overview

Banner DXM controllers communicate via Modbus TCP on port 502. They bridge IO-Link sensors to Ethernet networks, mapping sensor data to standardized Modbus registers.

## Connection Setup

### Network Configuration
- Default DXM IP: `192.168.0.1`
- Modbus TCP Port: `502`
- Protocol: Modbus TCP (no authentication)

### Connection Pattern
```python
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(host='192.168.0.1', port=502, timeout=5.0)
client.connect()
result = client.read_holding_registers(0, 4, unit=1)  # Read 4 registers from unit 1
client.close()
```

## Register Map

Each connected sensor uses the same 4-register layout:

| Register | Address | Name | Type | Description |
|----------|---------|------|------|-------------|
| 0 | 0x0000 | Status | UINT16 | Sensor operational status |
| 1 | 0x0001 | BDC | UINT16 | Binary Diagnostic Codes |
| 2 | 0x0002 | Distance | UINT16 | Distance measurement (mm) |
| 3 | 0x0003 | Signal Quality | UINT16 | Signal strength |

### Status Values (Register 0)
- `303` = Normal operation
- `271` = Out of range (no target detected)
- `0` = Error/disconnected

### Distance Values (Register 2)
- `0` = Sensor disconnected
- `1-30000` = Valid distance in millimeters
- `65535` = Out of range

### Signal Quality (Register 3)
- `0` = No signal
- `1-9` = Weak signal
- `10-49` = Good signal
- `50+` = Strong signal

## CLI Usage

### Installation
```bash
pip install -r requirements.txt
pip install -e .
```

### Basic Commands
```bash
# Test connection
dxm test --ip 192.168.0.1

# Discover sensors
dxm discover

# Read single sensor
dxm read 1

# Monitor all sensors
dxm monitor --interval 1.0

# Monitor specific sensors
dxm monitor --units 1,2,3
```

## Troubleshooting

### Connection Issues
1. **Connection refused**: Check DXM power, network connectivity, IP address
2. **Timeout**: Increase timeout, check network latency
3. **No sensors found**: Verify IO-Link connections, check sensor power

### Network Diagnostics
```bash
# Test connectivity
ping 192.168.0.1

# Test port access
telnet 192.168.0.1 502
```

### Data Validation
- Status=0 + Distance=0 = Sensor disconnected
- Status=271 + Distance=65535 = Normal out-of-range
- Status=303 + Distance>0 = Valid measurement

### Common Register Patterns
- All zeros = Modbus communication failure
- Status varies, Distance=0 = IO-Link communication issue
- Good status, Signal=0 = Possible sensor problem

## Configuration

### DXM Setup
- Configure IP address using Banner's configuration software
- Enable IO-Link ports where sensors are connected
- Assign unit IDs (typically 1-8)

### Sensor Assignment
Each IO-Link port gets a Modbus unit ID:
- Port 1 → Unit ID 1
- Port 2 → Unit ID 2
- etc.

## Performance Notes

- Typical response time: <100ms
- Sensor update rate: 1-10 Hz
- Read all 4 registers together for consistency
- Don't poll faster than sensor updates