## Q90R R-GAGE® Radar Sensor Instruction Manual

<!-- image -->

Original Instructions p/n: 237883 Rev. A March 05, 2024

## Contents

| Chapter 1 Product Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1 Models..................................................................................................................................................................................................... 4                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 1.2 Overview.................................................................................................................................................................................................. 4                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 1.3 Features and Indicators........................................................................................................................................................................... 5 5                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1.4 Radar Configuration Software .................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chapter 2 Installation Instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2.1 Sensor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Orientation................................................................................................................................................................................... 6 2.2 Wiring ...................................................................................................................................................................................................... 6                                                                                                                                                                                                                           |
| 2.3 Mount the Device..................................................................................................................................................................................... 7                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Chapter 3 Getting Started                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3.1 Install the Software..................................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 8 3.2 Connect to the Sensor............................................................................................................................................................................. 8                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 3.3 Software Overview .................................................................................................................................................................................. 9                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Chapter 4 Banner Radar Configuration Workspace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 4.1 Navigation Toolbar................................................................................................................................................................................. 10 4.2 Live Sensor Data and Legend............................................................................................................................................................... 10                                                                                                                                                                                                                                   |
| 4.3 Summary Pane.......................................................................................................................................................................................11                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 4.4 Sensor Settings Pane.............................................................................................................................................................................11                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 4.4.1 General Tab ..................................................................................................................................................................................11                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 4.4.2 Analog Tab ................................................................................................................................................................................... 12                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 4.4.3 Discrete 1 Tab.............................................................................................................................................................................. 13                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 4.4.4 Discrete 2 Tab.............................................................................................................................................................................. 13 4.5 Live Sensor Data Controls..................................................................................................................................................................... 14                                                                                                                                                                                                                                    |
| 4.6 Using Measurement Hold Example ....................................................................................................................................................... 15                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Chapter 5 Configuring a Sensor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 5.1 Banner Radar Configuration Software................................................................................................................................................... 16                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 5.2 IO-Link Interface .................................................................................................................................................................................... 16                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 5.3 Remote Input ......................................................................................................................................................................................... 16                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 5.4 Remote Teach........................................................................................................................................................................................ 19                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 5.5 Remote Setup........................................................................................................................................................................................ 19 20                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 5.5.1 Analog Teach Modes....................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 5.5.2 Discrete Teach Modes .................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 20 5.5.3 Set the Sensitivity ........................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 20 5.5.4 Set the Speed..............................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 20 5.5.5 Target Selection Mode................................................................................................................................................................. 21                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 5.6 Reset the Sensor to Factory Defaults.................................................................................................................................................... 21 5.7 Factory Default Settings ........................................................................................................................................................................ 22                                                                                                                                                                                                                                       |
| Chapter 6 Specifications 6.1 FCC Part 15 Class A for Intentional Radiators ......................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 24 6.2 Industry Canada Statement for Intentional Radiators............................................................................................................................ 25 6.3 Dimensions............................................................................................................................................................................................                                                                                                                                                                                                                                           |
| 25 6.4 Beam Patterns.......................................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 25                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chapter 7 Accessories 7.1 Configuration Tool.................................................................................................................................................................................. 27                                                                                                                                                                                                                                                                                                                                                                                                              |
| 7.2 Cordsets ................................................................................................................................................................................................ 27 7.3 Brackets................................................................................................................................................................................................. 28 7.4 IO-Link Masters ..................................................................................................................................................................................... 29 |
| Chapter 8 Product Support                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 8.1 Update the Software..............................................................................................................................................................................                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 30 8.2 Repairs .................................................................................................................................................................................................. 30                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 8.3 Contact Us............................................................................................................................................................................................. 31                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 8.4 Banner Engineering Corp. Software Copyright Notice .......................................................................................................................... 31                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Banner Engineering Corp Limited Warranty.......................................................................................................................................... 31                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 8.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Index....................................................................................................................................... 32

## Chapter Contents

| 1.1 Models............................................................................................................................................................................................................   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.2 Overview ........................................................................................................................................................................................................    |
| 1.3 Features and Indicators..................................................................................................................................................................................            |
| 1.4 Radar Configuration Software........................................................................................................................................................................                 |

## Chapter 1

## Product Description

Radar-Based Sensors for Detection and Measurement of Moving and Stationary Targets. Patent pending.

<!-- image -->

## WARNING:

- Do not use this device for personnel protection
- Using this device for personnel protection could result in serious injury or death.
- This device does not include the self-checking redundant circuitry necessary to allow its use in personnel safety applications. A device failure or malfunction can cause either an energized (on) or de-energized (off) output condition.

<!-- image -->

IMPORTANT: To satisfy RF exposure requirements, this device and its antenna must operate with a separation distance of at least 20 cm from all persons.

## Models 1.1

Q90R-4040 Models Table 1.

| Models   | Detection Range                                       | Supply Voltage                             | Telecom Approved                                                                 | Output         |
|----------|-------------------------------------------------------|--------------------------------------------|----------------------------------------------------------------------------------|----------------|
|          | 10 V DC to 30 V DC                                    | US, Canada, Europe, Australia, New Zealand | Analog current (4 mAto 20 mA, 1 NPN/PNP discrete, and IO-Link)                   | Q90R-4040-6KIQ |
|          | 0.15 m to 20 m (0.5 ft to 65.6 ft) 12 V DC to 30 V DC | US, Canada, Europe, Australia, New Zealand | Analog voltage (0 V to 10 V or 0.5 V to 4.5 V, 1 NPN/ PNP discrete, and IO-Link) | Q90R-4040-6KUQ |
|          | 10 V DC to 30 V DC                                    | US, Canada, Europe, Australia, New Zealand | Dual discrete (NPN/PNP, PFM, and IO-Link)                                        | Q90R-4040-6KDQ |

## Overview 1.2

The Q90R is an industrial radar sensor that uses high-frequency radio waves from its internal antenna to detect and measure distance to objects in its field of view.

The Q90R detects a wide variety of materials including metal, liquids, or organic materials. Use the supplied software,IOLink, or a remote input wire to configure the sensor to sense objects within a specified distance while ignoring objects beyond

- FMCW radar detects moving and stationary objects
- Adjustable sensing field-ignores objects beyond setpoint
- Easy setup and configuration of range, sensitivity, and output using the Banner Radar Configuration Software
- Sensing functions are immune to wind, fog, steam, and temperature changes and resistant to rain and snow
- Compact, rugged IP69K housing withstands harsh environments

this distance (background suppression). Or configure the sensor to indicate the presence or absence of objects at a specific (or "taught") distance or range of distances (retroreflective).

Figure 1. Sensing Range

<!-- image -->

<!-- image -->

|   D0 (m) |   D1 (m) |   D2 (m) |
|----------|----------|----------|
|        0 |     0.15 |       20 |

## Features and Indicators 1.3

<!-- image -->

|     |    | LED             | Color   | Description                                                       |
|-----|----|-----------------|---------|-------------------------------------------------------------------|
| 1 2 |  1 | Power           | Green   | Power ON                                                          |
| 1 2 |  2 | Signal Strength | Green   | Signal strength indication                                        |
| 1 2 |  3 | Output 1        | Amber   | Target is within the taught analog span or discrete output status |
| 1 2 |  4 | Output 2        | Amber   | Discrete output status                                            |

## Radar Configuration Software 1.4

Use Banner's Radar Configuration Software to:

- Set up the sensor in 3 easy steps: set the switch point distance, signal strength threshold, and response time
- Easily monitor device status via the software
- Visualize the application in real-time
- Make adjustments to sensor settings on the fly

For more information, visit www.bannerengineering.com/us/en/products/sensors/software/ radar-configuration.html.

<!-- image -->

## Chapter Contents

| 2.1 Sensor Orientation .........................................................................................................................................................................................         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.2 Wiring ............................................................................................................................................................................................................. |
| 2.3 Mount the Device ...........................................................................................................................................................................................         |

## Installation Instructions Chapter 2

## Sensor Orientation 2.1

Correct sensor-to-object orientation is important to ensure proper sensing.

Minimize the tilt angle of a target relative to the sensor. The target should be tilted less than half of the beam angle.

Figure 2. Tilt angle of the target relative to the sensor

T= Target Angle, BA=Beam Angle

<!-- image -->

## Wiring 2.2

Quick disconnect wiring diagrams are functionally identical.

Continued on page 7

<!-- image -->

## Continued from page 6

Figure 5. Dual Discrete Output

<!-- image -->

* Push-Pull output. User-configurable PNP/NPN setting.

** Pulse Frequency Modulation

## Key:

1 = Brown

2 = White

3 = Blue

4 = Black

5 = Gray (Connect for use with remote input or Banner Radar Configuration software)

1

4

5

2

3

NOTE: Banner recommends that the shield wire (quick-disconnect cordsets only) be connected to earth ground or dc common. Shielded cordsets are recommended for all quick-disconnect models.

## Mount the Device 2.3

1. If a bracket is needed, mount the device onto the bracket.
2. Mount the device (or the device and the bracket) to the machine or equipment at the desired location. Do not tighten the mounting screws at this time. 2.
3. Check the device alignment.
4. Tighten the mounting screws to secure the device (or the device and the bracket) in the aligned position.

## Chapter Contents

| 3.1 Install the Software.........................................................................................................................................................................................   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.2 Connect to the Sensor....................................................................................................................................................................................       |
| 3.3 Software Overview .........................................................................................................................................................................................     |

## Getting Started Chapter 3

Power up the sensor, and verify that the power LED is ON green.

## Install the Software 3.1

IMPORTANT: Administrative rights are required to install the Banner Radar Configuration software.

- Download the latest version of the software from www.bannerengineering.com/us/en/products/sensors/software/ radar-configuration.html. 1.
2. Navigate to and open the downloaded file.
3. Click Install to begin the installation process.
- Depending on your system settings, a popup window may appear prompting to allow Banner Radar Configuration to make changes to your computer. Click Yes. 4.
5. Click Close to exit the installer.

## Connect to the Sensor 3.2

<!-- image -->

A = Pro Converter Cable (MQDC-506-USB)

B = Splitter (CSB-M1251FM1251M)

C = PC running Banner Radar Configuration software

D = Q90R

E = Power Supply (PSW-24-1 or PSD-24-4)

F = Optional 5-Pin to 5-Pin Double-Ended Cordset (ex. MQDEC3-515SS)

1. Connect the sensor to the splitter cable from the PRO-KIT. See "Configuration Tool " on page 27.
2. Connect the external power and Pro Converter cable to the splitter cable.
3. Connect the Pro Converter cable to the PC.
4. Open the Banner Radar Configuration Software.
5. Go to Sensor › 5.
6. Connect on the Navigation toolbar.

The Connection screen displays.

6. Select the correct Sensor Model and Com Port for the sensor.
2. Click Connect. The Connection screen closes and the sensor data displays. 7.

## Software Overview 3.3

Easy setup and configuration of range, sensitivity, and output using the Banner Radar Configuration software and Pro Converter Cable.

Figure 6. Banner Radar Configuration Software

<!-- image -->

- Navigation toolbarUse this toolbar to connect to the sensor, to save or load a configuration, or to reset to factory defaults 1.
- Live Sensor Data and LegendShows the signal strength versus distance for the connected sensor, as well as options to select which data displays on the graph 2.
- Summary pane-Displays the distance to the target, the signal strength, and the output status 3.
- Sensor Settings paneSet the sensor parameters in this pane 4.
- Status bar-Shows whether the sensor is connected, if a software update is available, and if the sensor data is being recorded to a file 5.
- Live Sensor Data controls-Use these controls to record, freeze, and play real-time sensor data, and to refresh the sensor connection 6.

## Chapter Contents

| 4.1 Navigation Toolbar........................................................................................................................................................................................   | 10   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 4.2 Live Sensor Data and Legend......................................................................................................................................................................            | 10   |
| 4.3 Summary Pane..............................................................................................................................................................................................11 |      |
| 4.4 Sensor Settings Pane....................................................................................................................................................................................11   |      |
| 4.5 Live Sensor Data Controls ...........................................................................................................................................................................        | 14   |
| 4.6 Using Measurement Hold Example ..............................................................................................................................................................                | 15   |

<!-- image -->

## Banner Radar Configuration Workspace

## Navigation Toolbar 4.1

Use this toolbar to connect to the sensor, to save or load a configuration, or to reset to factory defaults.

## From the File menu, the following options are available:

## Load Config

Load a configuration to the connected sensor. Use this option to set up multiple sensors with the same parameters.

## Save Config

Save a configuration to a desired location for future use.

## Reset Frequently Used Settings

Resets the software settings without changing the configuration of the attached sensor.

## Exit

Exit the Banner Radar Configuration Software.

## From the Sensor menu, the following options are available:

## Connect

Connect to the sensor.

## Disconnect

Disconnect from the sensor.

## Factory Reset

Select to perform a factor reset on the sensor. All custom parameters will be lost.

## From the Help menu, the following option is available:

## About

Select to view the software version number, the copyright notice, and the warranty.

## Live Sensor Data and Legend 4.2

The Live Sensor Data area displays the live distance and amplitude signal from the connected radar sensor. The signal strength threshold, switch point, and hysteresis are also plotted. Use these signals to evaluate targets to determine where the signal strength threshold and switch point should be configured for reliable detection.

Use the Y-Axis Max and the X-Axis Max to adjust the range displayed on the plot.

Legend -- Use the legend to select which data appears on the graph.

## Signal

Displays the strength of the signal over distance.

## Signal Threshold

Displays the signal strength threshold.

## Primary Targets

Represents the signal strength and location of the strongest target inside the switch point.

## Analog Window

The range the analog signal represents.

Available on analog models. Varies by output model.

## Discrete 1/2 Window

The range for the discrete output. Varies by output model.

## Switch Pt Lines

Displays the switch point distance.

## Hysteresis Lines

Displays the hysteresis distance.

## Summary Pane 4.3

The Summary pane (blue shaded area) displays Distance, Signal Strength, and Output Status.

## Distance

Displays the distance to the target.

## Signal Strength

Displays the amount of excess gain of the signal received from the target. The excess gain is relative to the minimum detection threshold (Signal Strength Threshold = 1).

## Output Status

Displays whether the output is ON or OFF, or the analog output value (analog models only).

## Sensor Settings Pane 4.4

Set parameters for the sensor.

Click Read to read the connected sensor's current parameters. Click Write to write the parameters to the sensor. Yellow highlight on a parameter's value indicates changes that have not yet been written to the sensor.

## General Tab 4.4.1

The following are the parameters on the General tab on the Sensor Settings pane.

## Response Speed

Choose the response speed of the sensor (Slow, Medium, Fast).

## Target Selection

Signal Strength Threshold : Choose the threshold for the minimum amount of signal needed to actuate the output. Target Mode:

Strongest Target -Output responds to the target with the highest signal strength that is over the signal strength threshold.

Nearest Target -Output responds to the nearest target that is over the signal strength threshold.

## Advanced Target

Minimum Active Sensing Range

Maximum Active Sensing Range

: Sensor ignores anything from the face of the sensor to this defined range. : Sensor ignores anything past this defined range.

Measurement Hold: A rate of change filter to smooth the output and reduce chatter. For more information, see " Using Measurement Hold Example " on page 15 .

Maximum Distance Increase Hold Time: The period of time the sensor holds its last measurement and output status if the measurement changes more than the configured max distance increase. Available when Measurement Hold is set to enabled.

Maximum Distance Decrease Hold Time: The period of time the sensor holds its last measurement and output status if the measurement changes more than the configured max distance decrease. Available when Measurement Hold is set to enabled.

Maximum Distance Increase: The allowed limit the measurement can increase, or move farther away from the sensor, before initiating the Measurement Hold . Setting this to zero disables it. Available when Measurement Hold is set to enabled.

Maximum Distance Decrease: The allowed limit the measurement can decrease, or move closer to the sensor, before initiating the Measurement Hold . Setting this to zero disables it. Available when Measurement Hold is set to enabled.

## Sensor Polarity

Define the output and remote input signal type.

## Sensor Lockout

Remote Input (Gray Wire) : Enable or disable the remote input wire.

## LED Enable/Disable

Enable or disable the LEDs on the sensor

## Analog Tab 4.4.2

The following are the parameters on the Analog tab on the Sensor Settings pane. This tab is available for analog models.

<!-- image -->

## Analog Span

Define the outer limits of the analog range. This can be used to create a positive or negative slope.

Analog output options:

Current: 4 mA to 20 mA

Voltage: 0 V to 10 V or 0.5 V to 4.5 V

## Output

Loss-of-Signal : Sets the Analog Output value used by the sensor during a loss of signal. When a signal is restored, measurement resumes.

Hold Last Value-The Analog Output holds the last value indefinitely during a loss of signal.

3.5 mA (0 V)-The Analog Output switches to this value 2 seconds after a loss of signal. For Voltage models, this is 0 V. (Default)

20.5 mA (10.5 V/5 V)-The Analog Output switches to this value 2 seconds after a loss of signal. For Voltage models, this is 10.5 V.

Averaging: Use this menu to set the number of measurements that are averaged together for the analog output. Increasing the averaging improves repeatability but increases the total response speed. The default is 1. The filter can be set to 1, 2, 4, 8, 16, 32, 64, or 128. The total response time is shown under Response Time.

## Response Time

Calculates the total response time, taking into account the general response speed and averaging.

Table 2. Analog

|                | Analog Output Filter Setting   | Analog Output Filter Setting   | Analog Output Filter Setting   | Analog Output Filter Setting   | Analog Output Filter Setting   | Analog Output Filter Setting   | Analog Output Filter Setting   | Analog Output Filter Setting   |
|----------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|
| Response Speed | 1                              | 2                              | 4                              | 8                              | 16                             | 32                             | 64                             | 128                            |
|                | Analog Output Spec (ms)        | Analog Output Spec (ms)        | Analog Output Spec (ms)        | Analog Output Spec (ms)        | Analog Output Spec (ms)        | Analog Output Spec (ms)        | Analog Output Spec (ms)        | Analog Output Spec (ms)        |
| Fast           | 16                             | 32                             | 64                             | 128                            | 256                            | 512                            | 1024                           | 2048                           |
| Medium         | 80                             | 160                            | 320                            | 640                            | 1280                           | 2560                           | 5120                           | 10,240                         |
| Slow           | 200                            | 400                            | 800                            | 1600                           | 3200                           | 6400                           | 1280                           | 2560                           |

## Discrete 1 Tab 4.4.3

The following are the parameters on the Discrete 1 tab on the Sensor Settings pane.

## Output Mode

Select

Switch Point or Window .

Switch Point : The distance at which the switch point threshold is placed.

Window

: Define two set points to create window limits.

## Distance Settings

Define the set point(s) and the hysteresis.

## Output Settings

NO/NC : Select Normally Open or Normally Closed from the list.

On Delay : Set an on delay in milliseconds. The maximum time is 60,000 ms.

Off Delay : Set an off delay in milliseconds. The maximum time is 60,000 ms.

## Response Time

Calculates the total response time, taking into account the general response speed and on or off delays.

Table 3. Discrete

| Response Speed   |   Discrete Output ON Spec (ms) |   Discrete Output OFF Spec (ms) |
|------------------|--------------------------------|---------------------------------|
| Fast             |                             50 |                              50 |
| Medium           |                            100 |                             200 |
| Slow             |                            250 |                             550 |

## Discrete 2 Tab 4.4.4

The following are the parameters on the Discrete 2 tab on the Sensor Settings pane. This tab is available for dual discrete models.

## Output Mode

Select Switch Point , Window , Complementary , or Pulse Pro/PFM .

Switch Point : Set a single switch point for the output to change.

Window

: Define two setpoints to create window limits.

Complementary

: Output 2 will be the opposite of Output 1.

Pulse Pro/PFM : Pulse Pro/PFM output to interface with Banner lights or a PLC with PFM inputs.

## Distance Settings

Available when Output Mode is set to Switch Point or Window . Define the set point(s) and the hysteresis.

## Output Settings

Available when Output Mode is set to Switch Point or Window .

NO/NC : Select

Normally Open or Normally Closed from the list.

On Delay : Set an on delay in milliseconds. The maximum time is 60,000 ms.

Off Delay : Set an off delay in milliseconds. The maximum time is 60,000 ms.

## Response Time

Calculates the total response time, taking into account the general response speed and on or off delays.

Table 4. Discrete

| Response Speed   |   Discrete Output ON Spec (ms) |   Discrete Output OFF Spec (ms) |
|------------------|--------------------------------|---------------------------------|
| Fast             |                             50 |                              50 |
| Medium           |                            100 |                             200 |
| Slow             |                            250 |                             550 |

## Pulse Pro/PFM Settings

Available when Output Mode is set to Pulse Pro/PFM .

The Q90R can generate pulses whose frequency are proportional to the sensor's measured distance, thereby providing a method for representing an analog signal with only a discrete counter. The sensing range of the sensor is scaled from 100 Hz to 600 Hz. 100 Hz equals the near range limit of the sensor, and 600 Hz equals the far sensing range limit. An output of 50 Hz or 650 Hz (user defined in the software) represents a loss of signal condition where there is no target or the target is out of range. This output can be tied directly to a number of Banner lights for visual feedback without the need for a controller.

100 Hz: Define the near sensing range limit of the Pulse Pro range.

600 Hz : Define the far sensing range limit of the Pulse Pro range.

Loss-of-Signal : Sets the value used by the sensor during a loss of signal. When a signal is restored, measurement resumes.

Hold last value-The Discrete 2 Output holds the last value indefinitely during a loss of signal.

50 Hz-The Discrete 2 Output switches to this value 2 seconds after a loss of signal.

650 Hz-The Discrete 2 Output switches to this value 2 seconds after a loss of signal.

## Live Sensor Data Controls 4.5

After connecting to the sensor, data sampling begins automatically (but not recording).

<!-- image -->

To stop data sampling, click Stop.

To restart data sampling, click Play. This only samples data from the sensor and displays it on the plot; it does not record the data to a log file.

<!-- image -->

To record data to a log file, click Record. The log file selection prompt displays. Save the log file as desired. The log file format is .csv.

<!-- image -->

If communication to the sensor is lost, click Refresh Device Connection to reconnect.

## Using Measurement Hold Example 4.6

Measurement Hold (The hold time is set to 1 second) Figure 10.

<!-- image -->

- A. The Max Distance Change threshold (red lines) adapts based on the previous Raw Measurement sample (blue lines) as long as that sample was within the previous thresholds.
- B. The temporary distance spike in the Raw Measurement (blue lines) is filtered out because the distance increase was outside of the Max Distance Change (red lines). The Output Measurement (green lines) will hold its last measurement.

The Raw Measurement change (blue lines) is greater than the Max Distance Change (red lines) so the Output Measurement (green lines) holds its previous value while the Raw Measurement is beyond the Max Distance

- C. Change. After the 1 second Hold Time expires, the Output Measurement and Max Distance Change thresholds are updated based on the next Raw Measurement value.
- D. The Raw Measurement (blue lines) drops down to a value below the Max Distance Change (red lines) so the Output Measurement (green lines) holds its value for the Hold Time. After the 1 second Hold Time expires, the Output Measurement and Max Distance Change thresholds are updated based on the next Raw Measurement value.

| Chapter Contents                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5.1 Banner Radar Configuration Software ......................................................................................................................................................... 16                |
| 5.2 IO-Link Interface........................................................................................................................................................................................... 16 |
| 5.3 Remote Input................................................................................................................................................................................................ 16 |
| 5.4 Remote Teach .............................................................................................................................................................................................. 19  |
| 5.5 Remote Setup .............................................................................................................................................................................................. 19  |
| 5.6 Reset the Sensor to Factory Defaults .......................................................................................................................................................... 21              |
| 5.7 Factory Default Settings............................................................................................................................................................................... 22      |

## Configuring a Sensor Chapter 5

## Banner Radar Configuration Software 5.1

Use the Banner Radar Configuration software and PRO-KIT to set up the R-GAGE sensor.

For more information visit www.bannerengineering.com/us/en/products/sensors/software/radar-configuration.html.

## IO-Link Interface 5.2

IO-Link is a point-to-point communication link between a master device and sensor. Use IO-Link to parameterize sensors and transmit process data automatically.

For the latest IO-Link protocol and specifications, see www.io-link.com.

Each IO-Link device has an IODD (IO Device Description) file that contains information about the manufacturer, article number, functionality etc. This information can be easily read and processed by the user. Each device can be unambiguously identified via the IODD as well as via an internal device ID. Download the Q90R's IO-Link IODD package (p/n 237876 for analog models and p/n 237875 for dual discrete models) from Banner Engineering's website at www.bannerengineering.com.

Banner has also developed Add On Instruction (AOI) files to simplify ease-of-use between the Q90R, multiple third-party vendors' IO-Link masters, and the Logix Designer software package for Rockwell Automation PLCs. Three types of AOI files for Rockwell Allen-Bradley PLCs are listed below. These files and more information can be found at www.bannerengineering.com.

Process Data AOIs -These files can be used alone, without the need for any other IO-Link AOIs. The job of a Process Data AOI is to intelligently parse out the Process Data word(s) in separate pieces of information. All that is required to make use of this AOI is an EtherNet/IP connection to the IO-Link Master and knowledge of where the Process Data registers are located for each port.

Parameter Data AOIs -These files require the use of an associated IO-Link Master AOI. The job of a Parameter Data AOI, when working in conjunction with the IO-Link Master AOI, is to provide quasi-realtime read/write access to all IO-Link parameter data in the sensor. Each Parameter Data AOI is specific to a given sensor or device.

IO-Link Master AOIs -These files require the use of one or more associated Parameter Data AOIs. The job of an IO-Link Master AOI is to translate the desired IO-Link read/write requests, made by the Parameter Data AOI, into the format a specific IO-Link Master requires. Each IO-Link Master AOI is customized for a given brand of IO-Link Master.

Add and configure the relevant Banner IO-Link Master AOI in your ladder logic program first; then add and configure Banner IO-Link Device AOIs as desired, linking them to the Master AOI as shown in the relevant AOI documentation.

## Remote Input 5.3

Use the remote input to program the sensor remotely.

The remote input provides limited programming options and is Active High. This can be configured for Active Low in the Banner Radar Configuration software by changing the Sensor Polarity. For Active High, connect the gray input wire to V+ (10 V DC to 30 V DC), with a remote switch connected between the wire and V+. For Active Low, connect the gray input wire to ground (0 V DC) with a remote switch connected between the wire and ground.

The remote input wire is disabled by default. Pulse the remote input wire 10 times or use the Banner Radar Configuration software to enable the feature. After enabling the remote input feature, pulse the remote input according to the diagram and the instructions provided in this manual. Remote teach can also be performed using the button on the Pro Converter Cable.

The length of the individual programming pulses is equal to the value T: 0.04 seconds ≤ T ≤ 0.8 seconds .

Exit remote programming modes by setting the remote input Low for longer than 2 seconds or by waiting for 60 seconds.

Figure 11. Remote Input Map

<!-- image -->

NOTE: If a factory reset is performed through the Banner Radar Configuration Software, the remote input wire becomes disabled (factory default setting). If the sensor is returned to factory defaults by using the remote input wire, the input wire remains enabled and the rest of the settings are restored to factory defaults.

## Remote Teach 5.4

Use the following procedure to teach the first and second switch points.

- Pulse the remote input once. The green Power LED flashes, the amber LED is off, and the red LED is off. 1.
2. Present the first point.
- Teach the switch point. 3.
4. Present the second point.
- Teach the switch point. 5.

| Action                         | Action   | Result                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single-pulse the remote input. | T        | Teach Accepted The green Power LED is off, the yellow LED of the output being taught flashes while the yellow LED of the output not being taught is off. The red LED indicates signal strength. Teach Not Accepted The green Power LED continues to flash, the yellow LED is off, and the red LED is off. Retry teaching the first point. |

| Action                         | Action   | Result                                                                                                                                                                                                                                                                                     |
|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single-pulse the remote input. | T        | The green Power LED turns on. Teach Accepted The sensor returns to run mode. Teach Not Accepted The green Power LED remains off, the yellow LED of the output being taught continues to flash while the yellow LED of the output not being taught is off. Retry teaching the second point. |

## Remote Setup 5.5

Use Remote Setup to set the output mode to set normally open or normally closed, change the analog slope, or set the teach mode.

While in remote set up, pulsing the remote wire once configures output 1. For analog models, the slope of the output changes. For discrete output, output 1 and output 2 options are identical.

Changing the Output Mode using remote input affects both the output configuration (normally open versus normally closed) and the Teach mode. The output configuration change takes effect immediately and can be used to change the output between normally open and normally closed or the analog slope without changing the switch point distance. The change in Teach mode does not immediately change the switch point location, but will affect the behavior of the next remote Teach.

<!-- image -->

<!-- image -->

## Analog Teach Modes 5.5.1

The default is to teach two separate points. With a positive slope, the first taught point is 4 mA and the second taught point is 20 mA.

If the two taught points are within 100 mm or less, the sensor views them as the same point. It considers that point as the 20 mA spot and sets the 4 mA spot at 150 mm. If a taught point is within the dead zone, the sensor sets that point at 150 mm.

## Discrete Teach Modes 5.5.2

Teaching two separate points creates a window around that range.

Background Teach-Teaching the same point twice (points within 100 mm of each other) sets the switch point 200 mm in front of the taught point.

Object Teach-Teaching the same point twice (points within 100 mm of each other) sets the switch point 100 mm behind the taught point.

Window Teach-Teaching the same point twice (points within 100 mm of each other) sets a window ±50 mm on either side of the taught point, for a total window size of 100 mm.

## Set the Sensitivity 5.5.3

Use Sensitivity Selection to set the signal strength threshold.

- Access Sensitivity Selection. 1.
- Select the desired signal threshold. 2.

| Action                         | Result                              |
|--------------------------------|-------------------------------------|
| Triple-pulse the remote input. | The green power LED flashes slowly. |

|   Action Pulses |                               | TEACH Mode                     | Result                                                                                                                                                                                                                       |
|-----------------|-------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               1 | T                             | Signal Strength Threshold = 1  | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               2 | T T T                         | Signal Strength Threshold = 2  | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               3 | T T T T T                     | Signal Strength Threshold = 3  | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               4 | T T T T T T T                 | Signal Strength Threshold = 5  | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               5 | T T T T T T T T T             | Signal Strength Threshold = 10 | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               6 | T T T T T T T T T T T         | Signal Strength Threshold = 15 | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               7 | T T T T T T T T T T T T T     | Signal Strength Threshold = 20 | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |
|               8 | T T T T T T T T T T T T T T T | Signal Strength Threshold = 30 | The signal threshold is set and the green power LED flashes equal to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode. |

## Set the Speed 5.5.4

Use Speed Selection to set the speed of the sensor.

1. Access Speed Selection.

| Action                       | Result                              |
|------------------------------|-------------------------------------|
| Four-pulse the remote input. | The green power LED flashes slowly. |

- Select the desired signal threshold. 2.

| Action   |           |                |                                                                                                                                                       |
|----------|-----------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pulses   |           | TEACH Mode     |                                                                                                                                                       |
| 1        | T         | Speed = Fast   | to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. The sensor exits remote teach and returns to run mode. |
| 2        | T T T     | Speed = Medium | to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. The sensor exits remote teach and returns to run mode. |
| 3        | T T T T T | Speed = Slow   | to the number of pluses, pauses, and then flashes equal to the number of pulses a second time. The sensor exits remote teach and returns to run mode. |

## Target Selection Mode 5.5.5

Use Target Selection to set the target that the output sees.

- Access Target Selection mode. 1.
- Select the desired signal threshold. 2.

| Action                       | Result                              |
|------------------------------|-------------------------------------|
| Five-pulse the remote input. | The green power LED flashes slowly. |

| Action   |       |                                                                                                                             | Result                                                                                                                           |
|----------|-------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Pulses   |       | TEACH Mode                                                                                                                  |                                                                                                                                  |
| 1        | T     | Nearest Target-Output responds to the nearest target that is over the signal strength threshold.                            | The signal threshold is set and the green power LED flashes equal to the number of pluses,                                       |
| 2        | T T T | Strongest Target-Output responds to the target with the highest signal strength that is over the signal strength threshold. | pauses, and then flashes equal to the number of pulses a second time. Then the sensor exits remote teach and returns to run mode |

## Reset the Sensor to Factory Defaults 5.6

Reset the sensor to factory default settings using one of two methods.

NOTE: If a factory reset is performed through the Banner Radar Configuration Software, the remote input wire becomes disabled (factory default setting). If the sensor is returned to factory defaults by using the remote input wire, the input wire remains enabled and the rest of the settings are restored to factory defaults.

To reset using the Banner Radar Configuration software, go to Sensor › Factory Reset. The sensor indicators flash once, the sensor is reset back to the factory default settings, and a confirmation message displays.

To reset using the remote input, eight-pulse the remote input to apply the factory defaults.

## Factory Default Settings 5.7

Table 5. General Tab Default Settings

| Setting                        | Factory Default   |
|--------------------------------|-------------------|
| Response Speed                 | Medium            |
| Signal Strength Threshold      | 1.0               |
| Target Mode                    | Nearest Target    |
| Measurement Hold               | Disabled          |
| Discrete Output & Remote Input | PNP               |
| Remote Input Wire              | Disabled          |

## Table 6. Analog Tab Default Settings

| Setting        | Factory Default           |
|----------------|---------------------------|
| Range          | 4 mAto 20 mA(0 V to 10 V) |
| 4mA/0V Point   | 0.15 m (0.49 ft)          |
| 20mA/10V Point | 20.0 m (65.6 ft)          |
| Loss of Signal | 3.5 mA(0 V)               |
| Averaging      | 1× (no averaging)         |

Table 7. Discrete 1 Tab Default Settings

| Setting     | Factory Default   |
|-------------|-------------------|
| Output Mode | Switch Point      |
| Setpoint 1  | 20.0 m (65.6 ft)  |
| Hysteresis  | 0.05 m (2 in)     |
| NO/NC       | Normally Open     |
| On Delay    | 0 ms              |
| Off Delay   | 500 ms            |

Table 8. Discrete 2Tab Default Settings

| Setting     | Factory Default   |
|-------------|-------------------|
| Output Mode | Switch Point      |
| Setpoint 1  | 20.0 m (65.6 ft)  |
| Hysteresis  | 0.05 m (2 in)     |
| NO/NC       | Normally Open     |
| On Delay    | 0 ms              |
| Off Delay   | 500 ms            |

## Chapter Contents

| 6.1 FCC Part 15 Class A for Intentional Radiators .............................................................................................................................................                   |   24 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 6.2 Industry Canada Statement for Intentional Radiators ..................................................................................................................................                        |   25 |
| 6.3 Dimensions................................................................................................................................................................................................... |   25 |
| 6.4 Beam Patterns..............................................................................................................................................................................................   |   25 |

## Chapter 6

## Range

The sensor can detect an object at the following range, depending on the material of the target: 0.15 m to 20 m (0.5 ft to 65.6 ft)

## Operating Principle

Frequency-modulated continuous-wave (FMCW) radar

## Operating Frequency

60 to 61.5 GHz

## Supply Voltage (Vcc)

Analog Voltage models: 12 V DC to 30 V DC Analog Current and Dual Discrete models: 10 V DC to 30 V DC

Use only with a suitable Class 2 power supply (UL) or Limited Power Supply (CE)

## Power and Current Consumption, exclusive of load

Power consumption: &lt; 2.4 W

Current consumption: &lt;100 mA at 24 V DC

## Supply Protection Circuitry

Protected against reverse polarity and transient overvoltages

## Linearity

&lt;± 10 mm at &lt; 300 mm &lt;± 4 mm at &gt; 300 mm Reference target with RCS = 1m²

## Delay at Power-up

&lt; 2 s

## Output Configuration

Analog Outputs:

## ·Current models

Discrete Output (Black Wire): IO-Link, push/pull output, configurable PNP or NPN output Analog output (White Wire): 4 mA to 20 mA

## ·Voltage models

Discrete Output (Black Wire): IO-Link, push/pull output, configurable PNP or NPN output

Analog output (White Wire): Configurable 0 V to 10 V or 0.5 V to 4.5 V

## ·Dual Discrete models

Discrete Output 1 (Black Wire): IO-Link, push/pull output, configurable PNP or NPN output Discrete Output 2 (White Wire): Configurable PNP or NPN, or Pulse Frequency Modulated (PFM) output

## Repeatability

2 mm

10 mm at Excess Gain &lt; 10×

## Maximum Transmitting Power

Peak EIRP: 100 mW, 20 dBm

## Output Protection

Protected against output short-circuit

## Specifications

## Remote Input

Allowable Input Voltage Range: 0 to Vsupply

Active High (internal weak pull-down): High state &gt; (Vsupply 2.25 V) at 2 mA maximum

Active Low (internal weak pull-up): Low state &lt; 2.25 V at 2 mA maximum

## Response Time

Analog update rate: 15 ms Discrete output response: 50 ms

Speeds given for fast mode.

## Indicators

Power LED: Green, power on

## Signal Strength LED:

Green Flash: weak signal

Green Solid: 4× threshold

Output LEDs: Amber, target within taught analog span/ discrete output status

## Construction

Housing: Aluminum

Window: Polycarbonate

## Connections

Integral M12 quick disconnect Models with a quick disconnect require a mating cordset

## Vibration and Mechanical Shock

All models meet MIL-STD-202G, Method 201A (Vibration: 10 Hz to 60 Hz, 0.06 inch (1.52 mm) double amplitude, 2 hours each along X, Y and Z axes) requirements. Also meets IEC 60947-5-2 (Shock: 30G 11 ms duration, half sine wave) requirements. Method 213B conditions H&amp;I. Shock: 75G with device operating; 100G for non-operation

## Operating Temperature

Standard model: -40 °C to +65 °C (-40 °F to +149 °F)

## Temperature Effect

&lt;±10 mm from -40 °C to +65 °C (-40 °F to +149 °F)

## Environmental Rating

IP67 per IEC60529 IEC IP69K per BS/ISO 20653:2013

## Country of Origin

USA

## Certifications

<!-- image -->

<!-- image -->

Banner Engineering BV Park Lane, Culliganlaan 2F bus 3 1831 Diegem, BELGIUM

<!-- image -->

Turck Banner LTD Blenheim House Blenheim Court Wickford, Essex SS11 8YT GREAT BRITAIN

<!-- image -->

<!-- image -->

ETSI EN 305 550 V2.1.0 ETSI EN 305 550-1 V.1.2.1 ETSI EN 305 550-2 V.1.2.1 FCC ID: UE3Q90R

IC: 7044A-Q90R6

Install where not accessible by unauthorized personnel.

The device shall only be accessible for adjustment, programming, or maintenance.

The device was evaluated for IK08 impact energy in accordance with IEC 62262.

## Output Ratings

Analog Outputs:

- Current Output (Q90R….-.I.. models): 1 kΩ maximum load resistance at 24 V; maximum load resistance = [(Vcc - 4.5)/ 0.02 Ω]
- Voltage Output (Q90R….-.U.. models): 2.5 kΩ minimum load resistance
- Current rating = 50 mA maximum each

| Black wire specifications per configuration   | Black wire specifications per configuration   | Black wire specifications per configuration   |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| IO-Link Push/Pull                             | Output High                                   | ≥ Vsupply - 2.5 V                             |
| IO-Link Push/Pull                             | Output Low                                    | ≤ 2.5 V                                       |
|                                               | Output High                                   | ≥ Vsupply - 2.5 V                             |
|                                               | Output Low                                    | ≤ 1V (loads ≤ 1 MegΩ)                         |
| NPN                                           | Output High                                   | ≥ Vsupply - 2.5 V                             |
| NPN                                           | Output Low                                    | ≤ 2.5 V                                       |

| White wire specifications per configuration   | White wire specifications per configuration   | White wire specifications per configuration   |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| PNP                                           | Output High                                   | ≥ Vsupply - 2.5 V                             |
| PNP                                           | Output Low                                    | ≤ 2.5 V (loads ≤ 70 kΩ)                       |
| NPN                                           | Output High                                   | ≥ Vsupply - 2.5 V                             |
| NPN                                           | Output Low                                    | ≤ 2.5 V                                       |

## FCC Part 15 Class A for Intentional Radiators 6.1

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

<!-- image -->

(Part 15.21) Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.

## Industry Canada Statement for Intentional Radiators 6.2

This device contains licence-exempt transmitters(s)/receiver(s) that comply with Innovation, Science and Economic Development Canada's licence-exempt RSS(s). Operation is subject to the following two conditions:

1.  This device may not cause interference.
2.  This device must accept any interference, including interference that may cause undesired operation of the device.

Cet appareil contient des émetteurs/récepteurs exemptés de licence conformes à la norme Innovation, Sciences, et Développement économique Canada. L'exploitation est autorisée aux deux conditions suivantes:

- L'appareil ne doit pas produire de brouillage. 1.
- L'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement. 2.

## Dimensions 6.3

All measurements are listed in millimeters [inches], unless noted otherwise.

<!-- image -->

<!-- image -->

<!-- image -->

## Beam Patterns 6.4

The beam pattern of the radar sensor is dependent on the radar cross section (RCS) of the target.

The beam pattern graphs represent Standard Mode and are guides for representative object detection capabilities based on different-sized radar cross sections and corresponding example real-world targets. Use the following charts as a starting point in application setup. Note that applications vary.

- Use the Beam Width versus Distance chart to understand where corresponding objects can be detected. Adjusting the signal strength threshold also affects the beam pattern when the target is constant.
- Use the Beam Width versus Degrees chart to help determine how much the target can tilt from 90 degrees while still maintaining detection.

Unless otherwise specified, the following beam patterns are shown with Signal Strength Threshold = 1.

<!-- image -->

Typical beam pattern, in degrees, on representative targets Figure 13.

<!-- image -->

## Chapter Contents

| 7.1 Configuration Tool ........................................................................................................................................................................................      |   27 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 7.2 Cordsets.......................................................................................................................................................................................................  |   27 |
| 7.3 Brackets ....................................................................................................................................................................................................... |   28 |
| 7.4 IO-Link Masters............................................................................................................................................................................................      |   29 |

## Accessories Chapter 7

## Configuration Tool 7.1

## PRO-KIT

## Includes:

- Pro Converter Cable (MQDC-506-USB)
- Splitter (CSB-M1251FM1251M)
- Power Supply (PSW-24-1)

## Cordsets 7.2

<!-- image -->

| 5-Pin Threaded M12 Cordsets with Shield-Single Ended   | 5-Pin Threaded M12 Cordsets with Shield-Single Ended   | 5-Pin Threaded M12 Cordsets with Shield-Single Ended   | 5-Pin Threaded M12 Cordsets with Shield-Single Ended              | 5-Pin Threaded M12 Cordsets with Shield-Single Ended   |
|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------|
| Model                                                  | Length                                                 | Dimensions                                             | Style Pinout (Female)                                             |                                                        |
| MQDEC2-506 2 m (6.56                                   | ft) Straight                                           | 44 Typ. ø 14.5 M12 x 1 32 Typ. [1.26"] 30 Typ. [1.18"] | MQDEC2-550 MQDEC2-575 MQDEC2-5100                                 |                                                        |
| 5 m (16.4 ft)                                          | ft) Straight                                           | 44 Typ. ø 14.5 M12 x 1 32 Typ. [1.26"] 30 Typ. [1.18"] | MQDEC2-515                                                        |                                                        |
| 9 m (29.5 ft)                                          | ft) Straight                                           | 44 Typ. ø 14.5 M12 x 1 32 Typ. [1.26"] 30 Typ. [1.18"] | MQDEC2-530                                                        |                                                        |
| 15 m (49.2 ft)                                         | ft) Straight                                           | 44 Typ. ø 14.5 M12 x 1 32 Typ. [1.26"] 30 Typ. [1.18"] | 2                                                                 |                                                        |
| 23 m (75.44                                            | ft)                                                    | 44 Typ. ø 14.5 M12 x 1 32 Typ. [1.26"] 30 Typ. [1.18"] | 1                                                                 |                                                        |
| 30.5                                                   | m (100 ft)                                             | 44 Typ. ø 14.5 M12 x 1 32 Typ. [1.26"] 30 Typ. [1.18"] | 3                                                                 |                                                        |
| 2 m (6.56 ft)                                          | Right-Angle                                            | ø 14.5 [0.57"] M12 x 1                                 | 4 5 2 = White MQDEC2-506RA MQDEC2-515RA MQDEC2-530RA MQDEC2-550RA |                                                        |
| 5 m (16.4 ft)                                          | Right-Angle                                            | ø 14.5 [0.57"] M12 x 1                                 | 1 = Brown                                                         |                                                        |
| 9 m (29.5                                              | ft)                                                    | ø 14.5 [0.57"] M12 x 1                                 | 3 = Blue                                                          |                                                        |
| 15 m (49.2 ft)                                         | Right-Angle                                            | ø 14.5 [0.57"] M12 x 1                                 | 4 = Black                                                         |                                                        |
| 23 m (75.44 ft)                                        | Right-Angle                                            | ø 14.5 [0.57"] M12 x 1                                 | 5 = Gray MQDEC2-575RA                                             |                                                        |
| 31 m (101.68 ft)                                       | Right-Angle                                            | ø 14.5 [0.57"] M12 x 1                                 | MQDEC2-5100RA                                                     |                                                        |

<!-- image -->

| 5-Pin Male Threaded and 5-Pin Female Quick Disconnect M12 Cordset with Shield-Double Ended   | 5-Pin Male Threaded and 5-Pin Female Quick Disconnect M12 Cordset with Shield-Double Ended   | 5-Pin Male Threaded and 5-Pin Female Quick Disconnect M12 Cordset with Shield-Double Ended   | 5-Pin Male Threaded and 5-Pin Female Quick Disconnect M12 Cordset with Shield-Double Ended   | 5-Pin Male Threaded and 5-Pin Female Quick Disconnect M12 Cordset with Shield-Double Ended   |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Model                                                                                        | Length "L1"                                                                                  | Style                                                                                        | Pinout (Male)                                                                                | Pinout (Female)                                                                              |
| 0.91 m (2.99 ft)                                                                             | Female Straight/Male Straight                                                                |                                                                                              | 1 4 5 3 2                                                                                    | MQDEC3-503SS 2                                                                               |
| 1.83 m (6 ft)                                                                                | Female Straight/Male Straight                                                                |                                                                                              | 1 4 5 3 2                                                                                    | 1 MQDEC3-506SS                                                                               |
| 4.58 m (15 ft)                                                                               | Female Straight/Male Straight                                                                |                                                                                              | 1 4 5 3 2                                                                                    | 3 MQDEC3-515SS                                                                               |
| 9.2 m (30.2 ft)                                                                              | Female Straight/Male Straight                                                                |                                                                                              | 1 4 5 3 2                                                                                    | MQDEC3-530SS                                                                                 |

Continued on page 28

<!-- image -->

Continued from page 27

<!-- image -->

<!-- image -->

NOTE: The splitter in the PRO-KIT has two male and one female connectors. The CSB-M1251M1251B splitter has one male and two female connectors. Use the CSB-M1251M1251B to connect the sensor to power and a one of the Banner Pro lights with the Pulse Pro output.

## Brackets 7.3

## SMBAMSQ90R

- Adjustable mounting bracket
- 14-Gauge 304 stainless steel
- M6 × 1 mounting hardware included

## SMBRAQ90R

- Right-angle mounting bracket
- 14-Gauge 304 stainless steel
- M6 × 1 mounting hardware included

## SMBMAG3

- 3.2 inch diameter magnet with 95 lbs pull force
- Use with LMBWLC90PT, SMBAMS70AS, SMBAMSQ90R bracket
- Hardware for mounting to bracket included

<!-- image -->

<!-- image -->

<!-- image -->

## NOTE: Use SMBMAG3 with SMBAMSQ90R.

## IO-Link Masters 7.4

## DXMR110-8K Series Controller IO-Link Master

- Two female M12 D-Code Ethernet connectors for daisy chaining and communication to a higher-level control system
- Eight female M12 connections for IO-Link master connections
- One male M12 connection for incoming power, one female M12 connection for daisy chaining power

## DXMR90-4K Series Controller IO-Link Master

- One female M12 D-Code Ethernet connector
- Four female M12 connections for IO-Link master connections
- One male M12 (Port 0) connection for incoming power and Modbus RS-485, one female M12 connection for daisy chaining Port 0 signals

## R45C-2K-MQ 2-Port IO-Link Master/Modbus Converter

- Connects two IO-Link devices and provides access via Modbus RTU interface
- 5-pin M12 male quick-disconnect connector
- Two 4-pin M12 female quick-disconnect connectors

## R90C-4K-MQ 4-Port IO-Link Master/Modbus Convertor

- Connects four IO-Link devices and provides access via Modbus RTU interface
- 5-pin M12 male quick-disconnect connector
- Four 4-pin M12 female quick-disconnect connectors

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Chapter Contents

| 8.1 Update the Software.....................................................................................................................................................................................         |   30 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 8.2 Repairs......................................................................................................................................................................................................... |   30 |
| 8.3 Contact Us....................................................................................................................................................................................................   |   31 |
| 8.4 Banner Engineering Corp. Software Copyright Notice.................................................................................................................................                              |   31 |
| 8.5 Banner Engineering Corp Limited Warranty.................................................................................................................................................                        |   31 |

## Chapter 8

## Product Support

## Update the Software 8.1

Use this procedure to update the Banner Radar Configuration Software.

The Banner Radar Configuration Software automatically looks for updated software versions. The symbol in the lower right corner indicates that a software update is available.

Figure 14. Software Update Available

<!-- image -->

- Click in the lower right corner of the software. 1.

The Banner Radar Configuration Software Update screen displays.

Figure 15. Banner Radar Configuration Software Update Screen

<!-- image -->

- Click Upgrade to begin the process. 2.

The Banner Radar Configuration Software closes and an installer (BannerRadarConfigInstaller.exe) downloads to the desktop.

NOTE: If changes have not been written to the sensor, the system asks whether you want to exit the program. Click No to stop the update process and return to the Software. Write the changes to the sensor, then return to step 1, above, to update the Software.

3. Navigate to and open the file BannerRadarConfigInstaller.exe.
2. Depending on your system settings, a popup window may appear prompting to allow Banner Radar Configuration Software to make changes to your computer. Click Yes. 4.
5. Click Close to exit the installer.

The software update is complete.

## Repairs 8.2

Contact Banner Engineering for troubleshooting of this device. Do not attempt any repairs to this Banner device; it contains no field-replaceable parts or components. If the device, device part, or device component is determined to be defective by a Banner Applications Engineer, they will advise you of Banner's RMA (Return Merchandise Authorization) procedure.

<!-- image -->

IMPORTANT: If instructed to return the device, pack it with care. Damage that occurs in return shipping is not covered by warranty.

You may be asked to provide the configuration file and the data log file (.cfg) to aid in troubleshooting.

## Contact Us 8.3

Banner Engineering Corp. headquarters is located at: 9714 Tenth Avenue North | Minneapolis, MN 55441, USA | Phone: + 1 888 373 6767

For worldwide locations and local representatives, visit www.bannerengineering.com.

## Banner Engineering Corp. Software Copyright Notice 8.4

© Banner Engineering Corp., All Rights Reserved.

https://www.bannerengineering.com/us/en/company/terms-and-conditions.html

Disclaimer of Warranties. This software is provided "AS-IS." To the maximum extent permitted by applicable law, Banner, it affiliates, and its channel partners disclaim all warranties, expressed or implied, including any warranty that the software is fit for a particular purpose, title, merchantability, data loss, noninterference with or non-infringement of any intellectual property rights, or the accuracy, reliability, quality or content in or linked to the services. Banner and its affiliates and channel partners do not warrant that the services are secure, free from bugs, viruses, interruption, errors, theft or destruction. If the exclusions for implied warranties do not apply to you, any implied warranties are limited to 60 days from the date of first use of this software.

Limitation of Liability and Indemnity. Banner, its affiliates and channel partners are not liable for indirect, special, incidental, punitive or consequential damages, damages relating to corruption, security, loss or theft of data, viruses, spyware, loss of business, revenue, profits, or investment, or use of software or hardware that does not meet Banner minimum systems requirements. The above limitations apply even if Banner and its affiliates and channel partners have been advised of the possibility of such damages. This Agreement sets forth the entire liability of Banner, its affiliates and your exclusive remedy with respect to the software use.

## Banner Engineering Corp Limited Warranty 8.5

Banner Engineering Corp. warrants its products to be free from defects in material and workmanship for one year following the date of shipment. Banner Engineering Corp. will repair or replace, free of charge, any product of its manufacture which, at the time it is returned to the factory, is found to have been defective during the warranty period. This warranty does not cover damage or liability for misuse, abuse, or the improper application or installation of the Banner product.

THIS LIMITED WARRANTY IS EXCLUSIVE AND IN LIEU OF ALL OTHER WARRANTIES WHETHER EXPRESS OR IMPLIED (INCLUDING, WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE), AND WHETHER ARISING UNDER COURSE OF PERFORMANCE, COURSE OF DEALING OR TRADE USAGE.

This Warranty is exclusive and limited to repair or, at the discretion of Banner Engineering Corp., replacement. IN NO EVENT SHALL BANNER ENGINEERING CORP. BE LIABLE TO BUYER OR ANY OTHER PERSON OR ENTITY FOR ANY EXTRA COSTS, EXPENSES, LOSSES, LOSS OF PROFITS, OR ANY INCIDENTAL, CONSEQUENTIAL OR SPECIAL DAMAGES RESULTING FROM ANY PRODUCT DEFECT OR FROM THE USE OR INABILITY TO USE THE PRODUCT, WHETHER ARISING IN CONTRACT OR WARRANTY, STATUTE, TORT, STRICT LIABILITY, NEGLIGENCE, OR OTHERWISE.

Banner Engineering Corp. reserves the right to change, modify or improve the design of the product without assuming any obligations or liabilities relating to any product previously manufactured by Banner Engineering Corp. Any misuse, abuse, or improper application or installation of this product or use of the product for personal protection applications when the product is identified as not intended for such purposes will void the product warranty. Any modifications to this product without prior express approval by Banner Engineering Corp will void the product warranties. All specifications published in this document are subject to change; Banner reserves the right to modify product specifications or update documentation at any time. Specifications and product information in English supersede that which is provided in any other language. For the most recent version of any documentation, refer to: www.bannerengineering.com.

For patent information, see www.bannerengineering.com/patents.

## Index

## A

analog TEACH modes 20

advanced target 11

analog tab 12

averaging 12

## H

hold time 11

## I

IO-Link 16

## L

lockout 11

## M

minimum active sensing range 11

maximum active sensing range 11

measurement hold 11

maximum distance increase 11

maximum distance decrease 11

## O

output 12

## P

polarity 11

## R

response speed 11

response time 12

## S

Sensor Settings 11

software 16

sensor polarity 11

sensor lockout 11

## T

TEACH modes 20

target selection 11

tab

analog 12

<!-- image -->

<!-- image -->

<!-- image -->

LinkedIn

Twitter

Facebook

<!-- image -->