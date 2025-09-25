# DXM Radar Toolkit

CLI toolkit for Banner DXM wireless controllers and radar sensors via Modbus TCP.

## Installation

```bash
git clone <repository-url>
cd dxm-radar-toolkit
pip install -r requirements.txt
pip install -e .
```

## Quick Start

```bash
# Test connection
dxm test --ip 192.168.0.1

# Find sensors
dxm discover

# Read sensor data
dxm read 1

# Monitor in real-time
dxm monitor --interval 1.0
```

## Configuration

Create `config.yaml`:
```yaml
network:
  dxm_ip: "192.168.0.1"
  modbus_port: 502
  timeout: 5.0

sensors:
  max_modules: 8
  monitor_interval: 1.0
```

## Basic Usage

### Connection
- DXM communicates via Modbus TCP on port 502
- Default IP: 192.168.0.1
- Each sensor gets a unit ID (1-8)

### Reading Data
```bash
# Single sensor
dxm read 1

# Multiple sensors
dxm monitor --units 1,2,3

# Raw register values
dxm read 1 --raw
```

### Register Layout
| Register | Description | Values |
|----------|-------------|---------|
| 0 | Status | 303=Normal, 271=Out of Range, 0=Error |
| 1 | BDC States | Diagnostic bitfield |
| 2 | Distance | 0=Disconnected, 65535=OOR, 1-65534=mm |
| 3 | Signal Quality | 0-255+ strength indicator |

## Troubleshooting

**Connection refused**: Check DXM power, IP address, network connectivity

**No sensors found**: Verify IO-Link connections and sensor power

**Timeout errors**: Increase timeout, check network latency

Run `dxm test` for comprehensive diagnostics.

## Documentation

- `TECHNICAL_GUIDE.md` - Complete technical reference
- `examples/` - Code examples
- `tests/` - Unit tests

## License

MIT License - See LICENSE file for details.