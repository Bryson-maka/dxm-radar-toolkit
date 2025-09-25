## IO-Link Data Reference Guide: Q90R Dual Discrete (KD Models)

## IO-Link Data Map

This document refers to the following IODD file: Banner\_Engineering-Q90R-20240124-IODD1.1.xml. The IODD file and support files can be found on www.bannerengineering.com under the download section of the product family page.

## Communication Parameters

The following communication parameters are used.

| Parameter               | Value     | Parameter              | Value   |
|-------------------------|-----------|------------------------|---------|
| IO-Link revision        | V1.1      | Port class             | A       |
| Process Data In length  | 48-bit    | SIO mode               | Yes     |
| Process Data Out length | N/A       | Smart sensor profile   | Yes     |
| Bit Rate                | 38400 bps | Block parameterization | Yes     |
| Minimum cycle time      | 3.9 ms    | Data Storage           | Yes     |
|                         |           | ISDU Supported         | Yes     |

## IO-Link Process Data In (Device to Master)

Process Data In is transmitted cyclically to the IO-Link master from the IO-Link device.

The Q90R IO-Link Process Data is 48-bits and can be configured using parameter data to include the measurement distance, the state of the stability indicator, and/or the state of both output channels. This information is sent to the IO-Link master every 3.9 ms.

## Process Data Configuration 1: Digital Measurement Sensor

| Subindex   | Subindex   | Name                       | Name                       | Name                       | Number of Bits   | Number of Bits   | Data Values                          | Data Values                          | Data Values                          |
|------------|------------|----------------------------|----------------------------|----------------------------|------------------|------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| 1          | 1          | Distance Measurement Value | Distance Measurement Value | Distance Measurement Value | 32               | 32               | 0 to 21000 (1)                       | 0 to 21000 (1)                       | 0 to 21000 (1)                       |
| 2          | 2          | Measurement Scale          | Measurement Scale          | Measurement Scale          | 8                | 8                | -3 = range shift of 10 -3            | -3 = range shift of 10 -3            | -3 = range shift of 10 -3            |
| 3          | 3          | Stability State            | Stability State            | Stability State            | 1                | 1                | 0 = no target or marginal, 1 = valid | 0 = no target or marginal, 1 = valid | 0 = no target or marginal, 1 = valid |
| 4          | 4          | BDC2 State                 | BDC2 State                 | BDC2 State                 | 1                | 1                | 0 = Inactive, 1 = Active             | 0 = Inactive, 1 = Active             | 0 = Inactive, 1 = Active             |
| 5          | 5          | BDC1 State                 | BDC1 State                 | BDC1 State                 | 1                | 1                | 0 = Inactive, 1 = Active             | 0 = Inactive, 1 = Active             | 0 = Inactive, 1 = Active             |
| Octet 0    |            |                            |                            |                            |                  |                  |                                      |                                      |                                      |
| Subindex   | 1 1        | 1 1                        |                            | 1 1                        | 1 1              | 1 1              | 1 1                                  | 1                                    | 1                                    |
| Bit offset | 47         | 47                         | 46                         | 45 44                      | 45 44            | 43 42            | 43 42                                | 41                                   | 40                                   |
| Value      | 0          | 0                          | 0                          | 0 0                        | 0 0              | 0 0              | 0 0                                  | 0                                    | 0                                    |
| Octet 1    |            |                            |                            |                            |                  |                  |                                      |                                      |                                      |
| Subindex   | 1          | 1                          | 1                          | 1 1                        | 1 1              | 1 1              | 1 1                                  | 1                                    | 1                                    |
| Bit offset | 39         | 39                         | 38                         | 37 36                      | 37 36            | 35 34            | 35 34                                | 33                                   | 32                                   |
| Value      | 0          | 0                          | 0                          | 0 0                        | 0 0              | 0 0              | 0 0                                  | 0                                    | 0                                    |
| Octet 2    |            |                            |                            |                            |                  |                  |                                      |                                      |                                      |
| Subindex   | 1          | 1                          | 1                          | 1 1                        | 1 1              | 1 1              | 1 1                                  | 1                                    | 1                                    |
| Bit offset | 31         | 31                         | 30                         | 29 28                      | 29 28            | 27 26            | 27 26                                | 25                                   | 24                                   |
| Value      | 0          | 0                          | 0                          | 0 0                        | 0 0              | 0 1              | 0 1                                  | 0                                    | 1                                    |

(1)  Measurement Value Exceptions:

· Out of range (-) = -2147483640

· Out of range (+) = 2147483640

· No measurement data = 2177483644

<!-- image -->

<!-- image -->

| Octet 3    |     |     |     |     |     |    |    |    |
|------------|-----|-----|-----|-----|-----|----|----|----|
| Subindex   | 1   | 1   | 1   | 1   | 1   | 1  | 1  | 1  |
| Bit offset | 23  | 22  | 21  | 20  | 19  | 18 | 17 | 16 |
| Value      | 1   | 0   | 0   | 1   | 0   | 1  | 1  | 0  |
| Octet 4    |     |     |     |     |     |    |    |    |
| Subindex   | 2   | 2   | 2   | 2   | 2   | 2  | 2  | 2  |
| Bit offset | 15  | 14  | 13  | 12  | 11  | 10 | 9  | 8  |
| Value      | 1   | 1   | 1   | 1   | 1   | 1  | 0  | 1  |
| Octet 5    |     |     |     |     |     |    |    |    |
| Subindex   | /   | /   | /   | /   | /   | 3  | 4  | 5  |
| Bit offset | 7   | 6   | 5   | 4   | 3   | 2  | 1  | 0  |
| Value      | N/A | N/A | N/A | N/A | N/A | 1  | 1  | 1  |

## Example with Digital Measurement Sensor

Based on the values in the Digital Measurement Sensor example:

- Measurement Value: 1430

- Measurement Scale: -3

- Stability State : Valid

- BDC2 State : Active

- BDC1 State: Active

Scaled Measurement Value: 1.430m

## Process Data Configuration 2: Distance and Excess Gain

| Subindex   | Subindex   | Name                          | Name                          | Name                          | Number of Bits   | Number of Bits   | Data Values   | Data Values   |
|------------|------------|-------------------------------|-------------------------------|-------------------------------|------------------|------------------|---------------|---------------|
| 1          | 1          | Distance Measurement Value    | Distance Measurement Value    | Distance Measurement Value    | 32 0 to 21000    | 32 0 to 21000    |               |               |
| 2          | 2          | Excess Gain Measurement Value | Excess Gain Measurement Value | Excess Gain Measurement Value | 16               | 16               |               |               |
| Octet 0    |            |                               |                               |                               |                  |                  |               |               |
| Subindex   | 1          |                               | 1                             | 1                             | 1 1              | 1                | 1             | 1             |
| Bit offset | 47         |                               | 46                            | 45                            | 44               | 43 42            | 41            | 40            |
| Value      | 0          |                               | 0                             | 0                             | 0 0              | 0                | 0             | 0             |
| Octet 1    |            |                               |                               |                               |                  |                  |               |               |
| Subindex   | 1          |                               | 1                             | 1                             | 1 1              | 1                | 1             | 1             |
| Bit offset | 39         |                               | 38                            | 37                            | 36 35            | 34               | 33            | 32            |
| Value      | 0          |                               | 0                             | 0                             | 0 0              | 0                | 0             | 0             |
| Octet 2    |            |                               |                               |                               |                  |                  |               |               |
| Subindex   | 1          |                               | 1                             | 1                             | 1 1              | 1                | 1             | 1             |
| Bit offset | 31         |                               | 30                            | 29                            | 28 27            | 26               | 25            | 24            |
| Value      | 0          |                               | 0                             | 0                             | 0 0              | 1                | 0             | 1             |
| Octet 3    |            |                               |                               |                               |                  |                  |               |               |
| Subindex   | 1          |                               | 1                             | 1                             | 1 1              | 1                | 1             | 1             |
| Bit offset | 23         |                               | 22                            | 21                            | 20 19            | 18               | 17            | 16            |
| Value      | 1          |                               | 0                             | 0                             | 1 0              | 1                | 1             | 0             |
| Octet 4    |            |                               |                               |                               |                  |                  |               |               |
| Subindex   | 2          |                               | 2                             | 2                             | 2 2              | 2                | 2             | 2             |
| Bit offset | 15         |                               | 14                            | 13                            | 12 11            | 10               | 9             | 8             |

Continued on page 3

Continued from page 2

| Octet 4    |    |    |    |    |    |    |    |    |
|------------|----|----|----|----|----|----|----|----|
| Value      | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |
| Octet 5    |    |    |    |    |    |    |    |    |
| Subindex   | 2  | 2  | 2  | 2  | 2  | 2  | 2  | 2  |
| Bit offset | 7  | 6  | 5  | 4  | 3  | 2  | 1  | 0  |
| Value      | 1  | 1  | 1  | 1  | 1  | 1  | 0  | 1  |

## Example for Distance and Excess Gain

Based on the values in the Distance and Excess Gain example:

- Measurement Value: 1430 (1.43 m)
- Excess Gain: 509

## Process Data Configuration 3: Distance and Excess Gain with Binary Data

| Subindex   | Name                          | Name                          | Name                          | Name                          | Number of Bits                     | Number of Bits                     | Data Values                        | Data Values                        |
|------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| 1          | Distance Measurement Value    | Distance Measurement Value    | Distance Measurement Value    | Distance Measurement Value    | 32 0 to 21000                      | 32 0 to 21000                      | 32 0 to 21000                      | 32 0 to 21000                      |
| 2          | Excess Gain Measurement Value | Excess Gain Measurement Value | Excess Gain Measurement Value | Excess Gain Measurement Value | 8 (restricted 0-255×)              | 8 (restricted 0-255×)              | 8 (restricted 0-255×)              | 8 (restricted 0-255×)              |
| 3          | Stability State               | Stability State               | Stability State               | Stability State               | 1 0=no target or marginal, 1=valid | 1 0=no target or marginal, 1=valid | 1 0=no target or marginal, 1=valid | 1 0=no target or marginal, 1=valid |
| 4          | BDC2 State                    | BDC2 State                    | BDC2 State                    | BDC2 State                    | 1 0=inactive, 1=Active             | 1 0=inactive, 1=Active             | 1 0=inactive, 1=Active             | 1 0=inactive, 1=Active             |
| 5          | BDC1 State                    | BDC1 State                    | BDC1 State                    | BDC1 State                    | 1 0=inactive, 1=Active             | 1 0=inactive, 1=Active             | 1 0=inactive, 1=Active             | 1 0=inactive, 1=Active             |
| Octet 0    |                               |                               |                               |                               |                                    |                                    |                                    |                                    |
| Subindex   | 1                             | 1                             | 1                             | 1                             | 1                                  | 1                                  | 1                                  | 1                                  |
| Bit offset | 47                            | 46                            | 45                            | 44                            | 43                                 | 42                                 | 41                                 | 40                                 |
| Value      | 0                             | 0                             | 0                             | 0                             | 0                                  | 0                                  | 0                                  | 0                                  |
| Octet 1    |                               |                               |                               |                               |                                    |                                    |                                    |                                    |
| Subindex   | 1                             | 1                             | 1                             | 1                             | 1                                  | 1                                  | 1                                  | 1                                  |
| Bit offset | 39                            | 38                            | 37                            | 36                            | 35                                 | 34                                 | 33                                 | 32                                 |
| Value      | 0                             | 0                             | 0                             | 0                             | 0                                  | 0                                  | 0                                  | 0                                  |
| Octet 2    |                               |                               |                               |                               |                                    |                                    |                                    |                                    |
| Subindex   | 1                             | 1                             | 1                             | 1                             | 1                                  | 1                                  | 1                                  | 1                                  |
| Bit offset | 31                            | 30                            | 29                            | 28                            | 27                                 | 26                                 | 25                                 | 24                                 |
| Value      | 0                             | 0                             | 0                             | 0                             | 0                                  | 1                                  | 0                                  | 1                                  |
| Octet 3    |                               |                               |                               |                               |                                    |                                    |                                    |                                    |
| Subindex   | 1                             | 1                             | 1                             | 1                             | 1                                  | 1                                  | 1                                  | 1                                  |
| Bit offset | 23                            | 22                            | 21                            | 20                            | 19                                 | 18                                 | 17                                 | 16                                 |
| Value      | 1                             | 0                             | 0                             | 1                             | 0                                  | 1                                  | 1                                  | 0                                  |
| Octet 4    |                               |                               |                               |                               |                                    |                                    |                                    |                                    |
| Subindex   | 2                             | 2                             | 2                             | 2                             | 2                                  | 2                                  | 2                                  | 2                                  |
| Bit offset | 15                            | 14                            | 13                            | 12                            | 11                                 | 10                                 | 9                                  | 8                                  |
| Value      | 1                             | 1                             | 1                             | 1                             | 1                                  | 1                                  | 1                                  | 1                                  |
| Octet 5    |                               |                               |                               |                               |                                    |                                    |                                    |                                    |
| Subindex   | /                             | /                             | /                             | /                             | /                                  | 3                                  | 4                                  | 5                                  |
| Bit offset | 7                             | 6                             | 5                             | 4                             | 3                                  | 2                                  | 1                                  | 0                                  |
| Value      | N/A                           | N/A                           | N/A                           | N/A                           | N/A                                | 1                                  | 1                                  | 1                                  |

## Example with Distance and Excess Gain with Binary Data

Based on the values in the Distance and Excess Gain with Binary Data example:

- Measurement Value: 1430 (1.43 m)
- Excess Gain: 253
- Stability State: Valid
- BDC2 State: Active
- BDC1 State: Active

## IO-Link Process Data Out (Master to Device)

Not applicable.

## Parameters Set Using IO-Link

These parameters can be read from and/or written to an IO-Link model of the Q90R sensor. Also included is information about whether the variable in question is saved during Data Storage and whether the variable came from the IO-Link Smart Sensor Profile. Unlike Process Data In, which is transmitted from the IO-Link device to the IO-Link master cyclically, these parameters are read or written acyclically as needed.

|   Index | Subindex   | Name                                                                 | Length              | Value Range                                                                                                                              | Default   | Access Rights   | Data Storage?   | Smart Sensor Profile   |
|---------|------------|----------------------------------------------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------|-----------------|------------------------|
|       0 | 1-15       | Direct Parameter Page 1 (incl. Vendor ID & Device ID)                |                     |                                                                                                                                          |           | ro              |                 |                        |
|       0 | 16         | Standard Command                                                     |                     | 65 = SP1 Single Value Teach 66 = SP2 Single Value Teach 130 = Restore Factory Settings 162 = Start discovery 163 = Stop discovery        |           | wo              |                 |                        |
|       1 | 1-16       | Direct Parameters Page 2                                             |                     |                                                                                                                                          |           | rw              |                 |                        |
|       2 |            | Standard Command                                                     | 8-bit Uinteger      | 65 = SP1 Single Value Teach 66 = SP2 Single Value Teach 126 = Locator Start 127 = Locator Stop 129 = Application Reset 131 = Back-to-box |           | wo              |                 | y                      |
|       3 |            | Data Storage Index (device-specific list of parameters to be stored) |                     |                                                                                                                                          |           |                 |                 |                        |
|      12 |            | Device Access Locks                                                  | 16-bit Record       |                                                                                                                                          |           |                 |                 |                        |
|      16 |            | Vendor Name string                                                   | 64-octet string     | Banner Engineering Corporation                                                                                                           |           | ro              |                 |                        |
|      17 |            | Vendor Text string                                                   | 64-octet string     | More Sensors. More Solutions                                                                                                             |           | ro              |                 |                        |
|      18 |            | Product Name string                                                  | 64-octet string     | Q90R                                                                                                                                     |           | ro              |                 |                        |
|      19 |            | Product ID string                                                    | 64-octet string     |                                                                                                                                          |           | ro              |                 |                        |
|      20 |            | Product Text string                                                  | 64-octet string     | More Sensors. More Solutions                                                                                                             |           | ro              |                 | y                      |
|      21 |            | Serial Number                                                        | 16-octet string     |                                                                                                                                          |           | ro              |                 |                        |
|      22 |            | Hardware Version                                                     | 64-octet string     |                                                                                                                                          |           | ro              |                 |                        |
|      23 |            | Firmware Version                                                     | 64-octet string     |                                                                                                                                          |           | ro              |                 | y                      |
|      24 |            | App Specific Tag (user defined)                                      | 32-octet string     |                                                                                                                                          |           | rw              | y               | y                      |
|      25 |            | Function Tag                                                         | 32-octet string     |                                                                                                                                          |           | rw              | y               | y                      |
|      26 |            | Location Tag                                                         | 32-octet string     |                                                                                                                                          |           | rw              | y               | y                      |
|      36 |            | Device Status                                                        | 8-bit Uinteger      | 0=Device is OK 4=Failure                                                                                                                 |           | ro              |                 |                        |
|      37 |            | Detailed Device Status                                               | Array[6] of 3-octet |                                                                                                                                          |           | ro              |                 |                        |
|      40 |            | Process Data Input                                                   |                     | see Process Data In                                                                                                                      |           | ro              |                 |                        |
|      58 |            | Teach-in Channel                                                     | 8-bit Uinteger      | 0=Default, 1=BDC1, 2=BDC2                                                                                                                | 0         | rw              |                 |                        |
|      59 |            | Teach-In Status                                                      |                     |                                                                                                                                          |           |                 |                 |                        |
|      59 | 1          | Teach State: 4-bit Integer                                           | 4-bit Uinteger      | 0 = Idle 1 = SP1 Success 2 = SP2 Success 3 = SP1 SP2 Success 4 = Wait for Command 5 = Busy 7 = Error                                     |           | ro              |                 | y                      |
|      59 | 2          | SP1 TP1                                                              | 1-bit integer       | 0 = not taught or unsuccessful 1 = successfully taught                                                                                   |           | ro              |                 | y                      |
|      59 | 3          | SP1 TP2                                                              | 1-bit integer       | 0 = not taught or unsuccessful 1 = successfully taught                                                                                   |           | ro              |                 | y                      |

Continued on page 5

Continued from page 4

Continued on page 6

| Index   | Subindex                                                 | Name                               | Length                                                                                              | Value Range   | Default Access Rights   | Data Storage?   | Smart Sensor Profile   |
|---------|----------------------------------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------|---------------|-------------------------|-----------------|------------------------|
| 59 4    | SP2 TP1                                                  | 1-bit integer                      | 0 = not taught or unsuccessful 1 = successfully                                                     | taught        | ro                      |                 | y                      |
| 59 5    | SP2 TP2                                                  | 1-bit integer                      | 0 = not taught or unsuccessful 1 = successfully taught                                              |               | ro                      |                 | y                      |
| 60      | BDC1 Setpoints                                           |                                    |                                                                                                     |               |                         |                 |                        |
| 60 1    | BDC1 Setpoint SP1 (Switch or Window mode) (mm)           | 32-bit Integer                     | 100-20000                                                                                           |               | 20000 rw                | y               | y                      |
| 60 2    | BDC1 Setpoint SP2 (Window mode only) (mm)                | 32-bit Integer                     | 100-20000 0 = unused for Mode                                                                       | Switch        | 0 rw                    | y y             |                        |
| 61      | BDC1 Configuration                                       |                                    |                                                                                                     |               |                         |                 |                        |
| 61 1    | BDC1 Switchpoint Logic                                   | 8-bit Uinteger                     | 0 = LO (NO), 1 = DO (NC)                                                                            |               | 0 rw                    | y y             |                        |
| 61 2    | BDC1 Mode                                                | 8-bit Uinteger                     | 1 = Switch Mode/Single Point Mode 2 = Window Mode                                                   |               | 1 rw                    | y y             |                        |
| 61 3    | Hysteresis                                               | 16-bit Uinteger                    | 0-20000                                                                                             |               | 50 rw                   | y y             |                        |
| 62      | BDC2 Setpoints                                           |                                    |                                                                                                     |               |                         |                 |                        |
| 62 1    | BDC2 Setpoint SP1 (Switch or Window mode) (mm)           | 32-bit Integer                     | 100-20000                                                                                           |               | 20000 rw                | y y             |                        |
| 62 2    | BDC2 Setpoint SP2 (Window mode only) (mm)                | 32-bit Integer                     | 100-20000 0 = unused for Mode                                                                       | Switch        | 0 rw                    | y y             |                        |
| 63      | BDC2 Configuration                                       |                                    |                                                                                                     |               |                         |                 |                        |
| 63 1    | BDC2 Switchpoint Logic                                   | 8-bit Uinteger                     | 0 = LO (NO), 1 = DO (NC)                                                                            |               | 0 rw                    | y y             |                        |
| 63 2    | BDC2 Mode                                                | 8-bit Uinteger                     | 1 = Switch Mode/Single Point Mode, 2 = Window Mode                                                  |               | 1 rw                    | y y             |                        |
| 63 3    | Hysteresis                                               | 16-bit Uinteger                    | 0-20000                                                                                             |               | 50 rw                   | y y             |                        |
| 64      | Configuration                                            |                                    |                                                                                                     |               |                         |                 |                        |
| 64 1    | Response Speed                                           | 8-bit Uinteger                     | 0 = Fast 1 = Medium 2 = Slow                                                                        |               | 1 rw                    | y               |                        |
| 64 2    | Peak Select Mode                                         | 8-bit Uinteger                     | 0 = Strongest Peak, 1 = First Peak                                                                  |               | 1 rw                    | y               |                        |
| 64 3    | Output Polarity                                          | 8-bit Uinteger                     | 0 = NPN, 1 = PNP                                                                                    |               | 1 rw                    | y               |                        |
| 64 4    | Process Data Filter Time (ms)                            | 16-bit Uinteger                    | 0-65535 ms                                                                                          |               | 0 rw                    | y               |                        |
| 64 5    | Process Data Layout                                      | 8-bit Uinteger                     | 0=Digital Measurement Sensor 1=Distance and Excess Gain 2=Distance and Excess Gain with Binary Data |               | 0 rw                    | y               |                        |
| 64 6    | Remote Input Mode                                        | 8-bit Uinteger                     | 0 = Disabled, 1 = Teach                                                                             |               | 0 rw                    | y               |                        |
| 64 7    | LEDs Disabled                                            | 8-bit Uinteger                     | 0 = Enabled, 1 =                                                                                    |               | 0 rw                    | y               |                        |
| 64 8    | Minimum amplitude required target detection              | for 32-bit Integer                 | 100-5000                                                                                            | Disabled      | 100 rw                  | y               |                        |
| 64 9    | Limit Filter Enabled                                     | 8-bit Uinteger                     | 0 = Disabled, 1 =                                                                                   | Enabled       | 0 rw                    | y               |                        |
| 64 10   | Limit Filter Positive Hold Time (ms)                     | 32-bit Integer                     | 50-3600000                                                                                          |               | 1000 rw                 | y               |                        |
| 64 11   | Limit Filter Negative Hold Time (ms)                     | 32-bit Integer                     | 50-3600000                                                                                          |               | 1000 rw                 | y               |                        |
| 64      |                                                          | 32-bit Integer                     | 0-1000                                                                                              |               | 150 rw                  | y               |                        |
| 12      | Limit Filter Positive Distance (mm)                      |                                    | 0-1000                                                                                              |               | rw                      |                 |                        |
| 4 13    | Limit Filter Negative Distance                           | (mm) 32-bit Integer 8-bit Uinteger | 0=Independent Output, 1=Complementary, Frequency Output                                             |               | 150 rw                  | y y             |                        |
| 64 14   | Secondary Output Mode BDC1 Vendor Specific Configuration |                                    | 2=Pulse                                                                                             |               | 0                       |                 |                        |
| 65 1    | BDC1 Delay On (ms)                                       | 32-bit Uinteger                    | 0-60000, 0 = disabled                                                                               |               | 0 rw                    | y               |                        |
| 65 2    | BDC1 Delay Off (ms)                                      | 32-bit Uinteger                    | 0-60000, 0 = disabled                                                                               |               | 500 rw                  | y               |                        |
| 65 3    | BDC1 Teach Offset (mm)                                   | 32-bit Integer                     | -20000 to 20000                                                                                     |               | 100 rw                  | y               |                        |
| 66      | BDC2 Vendor Specific Configuration                       |                                    |                                                                                                     |               |                         |                 |                        |
| 66 1    | BDC2 Delay On (ms)                                       | 32-bit Uinteger                    | 0-60000, 0 = disabled                                                                               |               | 0 rw                    | y               |                        |
| 66 2    | BDC2 Delay Off (ms)                                      | 32-bit Uinteger                    | 0-60000, 0 = disabled                                                                               |               | 500 rw                  | y               |                        |
| 66 3    | BDC2 Teach Offset (mm)                                   | 32-bit Integer                     | -20000 to 20000                                                                                     |               | 100 rw                  | y               |                        |
| 67      | Status                                                   |                                    |                                                                                                     |               |                         |                 |                        |
| 67 1    | Distance Measurement (mm)                                | 32-bit Integer                     | 0-21000                                                                                             |               | 0 ro                    | y               |                        |

Continued from page 5

|   Index | Subindex   | Name                                     | Length          | Value Range                                                          | Default   | Access Rights   | Data Storage?   | Smart Sensor Profile   |
|---------|------------|------------------------------------------|-----------------|----------------------------------------------------------------------|-----------|-----------------|-----------------|------------------------|
|      67 | 2          | Excess Gain                              | 32-bit Integer  | 0-2147483647                                                         | 0         | ro              | y               |                        |
|      67 | 3          | Stability                                | 8-bit Uinteger  | 0 = No Target 1 = Marginal Target 2 = Strong Target                  | 0         | ro              | y               |                        |
|      67 | 4          | Fault Status                             | 8-bit Uinteger  | 0 = No Fault Present, 1 = Fault Present                              | 0         | ro              | y               |                        |
|      67 | 5          | Temperature                              | 32-bit Integer  |                                                                      | 0         | ro              | y               |                        |
|      67 | 6          | Last Taught Temperature                  | 32-bit Integer  |                                                                      | 0         | ro              | y               |                        |
|      69 |            | All-Time Run Time (0.25 hr)              | 32-bit Uinteger | 0-4294967295                                                         | 0         | ro              | y               |                        |
|      70 |            | Resettable Run Time (0.25 hr)            | 32-bit Uinteger | 0-4294967295                                                         | 0         | rw              |                 |                        |
|      71 |            | PFM Configuration                        |                 |                                                                      |           |                 |                 |                        |
|      71 | 1          | Loss of Signal                           | 8-bit Uinteger  | 0=Hold, 1=Low, 2=High                                                | 100       | rw              | y               |                        |
|      71 | 2          | SP1 PFM Setpoint                         | 32-bit Integer  | 100-20000                                                            | 300       | rw              | y               |                        |
|      71 | 3          | SP2 PFM Setpoint                         | 32-bit Integer  | 100-20000                                                            | 20000     | rw              | y               |                        |
|      76 |            | All-Time Run Time Event Time (0.25 hr)   | 32-bit Uinteger | 0-4294967295, 0 = disable raising event                              | 0         | rw              | y               |                        |
|      77 |            | Resettable Run Time Event Time (0.25 hr) | 32-bit Uinteger | 0-4294967295, 0 = disable raising event                              | 0         | rw              | y               |                        |
|      78 |            | Active Sensing Range                     |                 |                                                                      |           |                 |                 |                        |
|      78 | 1          | Active Sensing Range Near (mm)           | 32-bit Integer  | 0-21000                                                              | 0         | rw              | y               |                        |
|      78 | 2          | Active Sensing Range Far (mm)            | 32-bit Integer  | 0-21000                                                              | 21000     | rw              | y               |                        |
|   16512 |            | MDC Descriptor                           |                 | Measuring Data Channel Descriptor - Smart Sensor Profile 2nd Edition |           |                 |                 |                        |
|   16512 | 1          | Lower Limit                              | 32-bit Integer  |                                                                      | -32000    | ro              | y               |                        |
|   16512 | 2          | Upper Limit                              | 32-bit Integer  |                                                                      | 32000     | ro              | y               |                        |
|   16512 | 3          | Unit                                     | 16-bit Uinteger | 1010 = m                                                             | 1010      | ro              | y               |                        |
|   16512 | 4          | Scale                                    | 8-bit Integer   | -3 = range shift of 10 -3                                            | -3        | ro              | y               |                        |

## IO-Link Events

Events are acyclic transmissions from the IO-Link device to the IO-Link master. Events can be error messages and/or warning or maintenance data.

| Code           | Type         | Name                            | Description                                                                                              |
|----------------|--------------|---------------------------------|----------------------------------------------------------------------------------------------------------|
| 25376 (0x6320) | Error        | Parameter error                 | Check datasheet and values                                                                               |
| 36000 (0x8ca0) | Warning      | All-time Run Time Event         | Event indicating the corresponding configured running time has elapsed                                   |
| 36001 (0x8ca1) | Warning      | Resettable Run Time Event       | Event indicating the corresponding configured running time has elapsed                                   |
| 36003 (0x8ca3) | Notification | Teach Completed Event           | Event indicating a teach has been completed                                                              |
| 36004 (0x8ca4) | Notification | Factory Settings Restored Event | Event indicating that the factory settings have been restored                                            |
| 36005 (0x8ca5) | Notification | Teach Coerced Event             | Event indicating a taught condition resulting in a setpoint being coerced; taught was updated            |
| 36007 (0x8ca7) | Notification | Teach Failed Event              | Event indicating an invalid target condition was attempted to be taught; taught setpoint was not updated |
| 36096 (0x8d00) | Error        | Transceiver Fault Event         | Event indicating that an error has occurred with the radar transceiver                                   |
| 36097 (0x8d01) | Error        | System Fault Event              | Contact Banner Engineering to resolve                                                                    |