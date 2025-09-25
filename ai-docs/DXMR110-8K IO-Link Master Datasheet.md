## Overview

Banner's DXMR110-8K IO-Link Controller consolidates data from multiple sources to provide local data processing as well as accessibility for host systems as a platform for the Industrial Internet of Things (IIoT).

The DXMR110-8K IO-Link Controller 8-port IO-link device serves as the gateway for the connection of up to eight IO-link devices including sensors, lighting products, IO-link hubs, and more.

<!-- image -->

The DXMR110-8K contains eight IO-link ports, allowing for concurrent communication to up to eight IO-Link devices. Data is collected into the internal logic controller to facilitate edge processing, protocol conversion to Industrial Ethernet, Modbus/TCP, and PROFINET, and pushing information to web servers. In addition to IO-Link devices, the IO-Link master can be used to transmit up to 16 discrete signals using pin 2 or pin 4 of the IO-link master ports.

The configurable IO-link master device works with IO-link devices and allows for quick deployment of IO-link data to Ethernet, Modbus/TCP, and PROFINET networks (1) .

- Multiprotocol support allows users to stock one part that can be used with a variety of industrial control systems
- Compact form factor weighs less than half of most competing designs, enabling better performance in weight- and size-critical applications such as robotic end-of-arm tooling where excess weight can affect speed
- M12 connections exit from the side rather than the top, providing new options to improve cable bend radius and avoid cable damage
- Two discrete inputs and one discrete output on each port give flexibility to system designers and simplify system architecture
- By locating IO-Link Masters near devices on the machine, users can eliminate I/O cards on the PLC, along with excess wiring to/ from the control panel
- Expanded internal logic controller with action rules and ScriptBasic programming to process and control data from multiple devices
- IP67 housing simplifies installation in any location by eliminating the need for a control cabinet

## Models

| Model      | Ethernet Connection                                                                                             | IO-Link Master Connections                                  | Other Connections                                                        |
|------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------|
| DXMR110-8K | Two female M12 D-Code Ethernet Connectors for daisy chaining and communication to a higher-level control system | Eight female M12 connections for IO-Link master connections | One male M12 for incoming power, one female M12 for daisy chaining power |

## Controller Connections

To connect IO-Link devices on machines in industrial environments, an M12 quick-disconnect connection is typically used. The pin assignment according to IEC 60974-5 is the following:

- Pin 1: 24 V DC
- Pin 2: Switching Digital I/O (PNP only)
- Pin 3: 0 V
- Pin 4: Switching Digital I/O (NPN, PNP, or Push-Pull) and IO-link Communication Line

(1) EtherNet/IP™ is a trademark of ODVA, Inc. Modbus® is a registered trademark of Schneider Electric USA, Inc. PROFINET® is a registered trademark of PROFIBUS Nutzerorganisation e.V. By default, the DXMR110-8K IO-Link Controller is set to a static IP address of 192.168.0.1.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

One male M12 connection provides common power and ground to all M12 IO-Link ports. Two 100 Mbps Ethernet ports (female) use an M12 D-coded Ethernet connection.

- Modbus/TCP
- EtherNet/IP
- PROFINET

Eight IO-Link controller connections using female M12 connectors.

- Separate IO-Link control and programmability for each connection point
- Configurable SIO mode on Input 1 and Input 2 of each IO-Link port

The DXMR110-8K IO-Link Controller has eight Class A ports. Pin 2 on these is an additional discrete IO channel. For specific pinout connections, see .

For more information on the device registers and port settings of the DXMR110-8K IO-Link Controller, refer to the DXMR110-8K IO-Link Controller IO-Link Master Device Register Map (p/n 233478).

## Installation Instructions

## Installing the DXMR110-8K

Install the DXMR110-8K to allow access for functional checks, maintenance, and service or replacement.

Fasteners must be of sufficient strength to guard against breakage. The use of permanent fasteners or locking hardware is recommended to prevent the loosening or displacement of the device. The mounting hole (4.5 mm) in the DXMR110-8K accepts M4 (#8) hardware. See the figure below to help in determining the minimum screw length.

<!-- image -->

CAUTION: Do not overtighten the DXMR110-8K's mounting screw during installation. Overtightening can affect the performance of the DXMR110-8K.

## Wiring

<!-- image -->

Ports 1-8 5-pin M12 female connector

<!-- image -->

| Port 1-8 5-pin M12 Connector (female)   |   Pin | Wire Color   | Description                         |
|-----------------------------------------|-------|--------------|-------------------------------------|
| 2 3 4 1 5                               |     1 | Brown (bn)   | 18 V DC to 30 V DC                  |
| 2 3 4 1 5                               |     2 | White (wh)   | I/Q (digital in-out)                |
| 2 3 4 1 5                               |     3 | Blue (bu)    | DC common (GND)                     |
| 2 3 4 1 5                               |     4 | Black (bk)   | C/Q (communications/digital in-out) |
| 2 3 4 1 5                               |     5 | Gray (gy)    | No connection/not used              |

5-pin M12 male connector

<!-- image -->

| 5-pin M12 Male Power Connector   |   Pin | Wire Color   | Description            |
|----------------------------------|-------|--------------|------------------------|
| 1 4 5 3 2                        |     1 | Brown (bn)   | 18 V DC to 30 V DC     |
| 1 4 5 3 2                        |     2 | White (wh)   | 18 V DC to 30 V DC     |
| 1 4 5 3 2                        |     3 | Blue (bu)    | DC common (GND)        |
| 1 4 5 3 2                        |     4 | Black (bk)   | DC common (GND)        |
| 1 4 5 3 2                        |     5 |              | No connection/not used |

5-pin M2 female connector

<!-- image -->

| 5-pin M12 Female Power Connector   |   Pin | Wire Color   | Description            |
|------------------------------------|-------|--------------|------------------------|
| 2 3 4 1 5                          |     1 | Brown (bn)   | 18 V DC to 30 V DC     |
| 2 3 4 1 5                          |     2 | White (wh)   | 18 V DC to 30 V DC     |
| 2 3 4 1 5                          |     3 | Blue (bu)    | DC common (GND)        |
| 2 3 4 1 5                          |     4 | Black (bk)   | DC common (GND)        |
| 2 3 4 1 5                          |     5 |              | No connection/not used |

D-code industrial Ethernet connectors

<!-- image -->

| 4-pin D-Code Female Industrial Ethernet Connector   |   Pin | Wire Color   | Description   |
|-----------------------------------------------------|-------|--------------|---------------|
| 1 4 3 2                                             |     1 | Black (bk)   | +Tx           |
| 1 4 3 2                                             |     2 | Red (rd)     | +Rx           |
| 1 4 3 2                                             |     3 | Green (gn)   | -Tx           |
| 1 4 3 2                                             |     4 | White (wh)   | -Rx           |

## Specifications

## Supply Voltage

18 V DC to 30 V DC

## Supply Protection Circuitry

Protected against reverse polarity and transient voltages

## Power Consumption

24 V DC at 150 mA + 200mA/port = 1750 mA maximum

## Application Note

When connecting external devices to the DXMR110-8K, it is important that the power consumption of the IO-Link master and connected devices combined does not exceed 8 Amps

## Construction

Connector Body: PVC translucent black

## Indicators

Green/amber/red: Program status indicators

Green: Ethernet communications

Red/green/blue on port 1: IO-Link Port 1 Status

Red/green/blue on port 2: IO-Link Port 2 Status

Red/green/blue on port 3: IO-Link Port 3 Status

Red/green/blue on port 4: IO-Link Port 4 Status

Red/green/blue on port 5: IO-Link Port 5 Status

Red/green/blue on port 6: IO-Link Port 6 Status

Red/green/blue on port 7: IO-Link Port 7 Status

Red/green/blue on port 8: IO-Link Port 8 Status

## Connections

Nine 5-pin fixed nylon M12 female quick disconnects connector

One 5-pin nickel-plated brass M12 male quick disconnect connector

Two 4-pin D-Code fixed nylon M12 female quick disconnect connectors

## Communication Protocols

PROFINET®, Modbus/TCP, EtherNet/IP™ EtherNet/IP™ is a trademark of ODVA, Inc. Modbus® is a registered trademark of Schneider Electric USA, Inc. PROFINET® is a registered trademark of PROFIBUS Nutzerorganisation e.V.

## Security Protocols

TLS, SSL, HTTPS

## Digital Inputs (SIO [DI] Mode)

Input Current: 5 mA typical ON Voltage/Current: 15 V DC minimum/5 mA minimum

OFF Voltage: 5 V DC maximum

## Digital Outputs (SIO [DO] Mode)

On-Resistance: 120 mΩ typical, 250 mΩ maximum Current Limit: 0.7 A minimum, 1.0 A typical, 1.3 A maximum Off Leakage Current: -10 μA minimum, 10 μA maximum

## IO-Link Baud Rates

<!-- image -->

<!-- image -->

COM1: 4.8 kbps

COM2: 38.4 kbps

COM3: 230.4 kbps

## Operating Conditions

-40 °C to +70 °C (-40 °F to +158 °F)

90% at +70 °C maximum relative humidity (non-condensing)

## Storage Temperature

-40 °C to +80 °C (-40 °F to +176 °F)

## Environmental Ratings

For Indoor Use Only

IP65, IP67, NEMA 1, UL Type 1

## Vibration and Mechanical Shock

Meets IEC 60068-2-6 requirements (Vibration: 10 Hz to 55 Hz, 1.0 mm amplitude, 5 minutes sweep, 30 minutes dwell) Meets IEC 60068-2-27 requirements (Shock: 30G 11 ms duration, half sine wave)

## Certifications

Banner Engineering BV Park Lane, Culliganlaan 2F bus 3 1831 Diegem, BELGIUM

Turck Banner LTD Blenheim House

Blenheim Court Wickford, Essex SS11 8YT

GREAT BRITAIN

## Required Overcurrent Protection

<!-- image -->

WARNING: Electrical connections must be made by qualified personnel in accordance with local and national electrical codes and regulations.

Overcurrent protection is required to be provided by end product application per the supplied table.

Overcurrent protection may be provided with external fusing or via Current Limiting, Class 2 Power Supply.

Supply wiring leads &lt; 24 AWG shall not be spliced.

For additional product support, go to www.bannerengineering.com .

|   Supply Wiring (AWG) |   Required Overcurrent Protection (A) |   Supply Wiring (AWG) |   Required Overcurrent Protection (A) |
|-----------------------|---------------------------------------|-----------------------|---------------------------------------|
|                    20 |                                     5 |                    26 |                                   1   |
|                    22 |                                     3 |                    28 |                                   0.8 |
|                    24 |                                     1 |                    30 |                                   0.5 |

## Dimensions

All measurements are listed in millimeters, unless noted otherwise. The measurements provided are subject to change.

## DXMR110-8K Dimensions

145.0 mm

[5.71']

<!-- image -->

## Accessories

## Power Supplies

PSD-24-4 -DC Power Supply, Desktop style, 3.9 A, 24 V DC, Class 2, 4-pin M12/Euro-style quick disconnect (QD)

PSDINP-24-06 -DC power supply, 0.63 Amps, 24 V DC, with DIN Rail Mount, Class I Division 2 (Groups A, B, C, D) Rated

PSDINP-24-13 -DC power supply, 1.3 Amps, 24 V DC, with DIN Rail Mount, Class I Division 2 (Groups A, B, C, D) Rated

PSDINP-24-25 -DC power supply, 2.5 Amps, 24 V DC, with DIN Rail Mount, Class I Division 2 (Groups A, B, C, D) Rated

PSW-24-1-DC power supply with multi-blade wall plug, 100-240 V AC 50/60 Hz input, 24 V DC 1 A output, UL Listed Class 2, 4-pin female M12 connector

PSWB-24-1-DC power supply with multi-blade wall plug,100-240 V AC 50/60 Hz input, 24 V DC 1 A output, UL Listed Class 2, barrel jack connector

## SMBR90S

- Stainless steel bracket
- 4x M4-07 pemnuts (B)
- Includes 2x M4 stainless steel hex head screws and flat washers

Hole center spacing: A = 40, B = 20

Hole size: A = ø 5

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Banner Engineering Corp Limited Warranty

Banner Engineering Corp. warrants its products to be free from defects in material and workmanship for one year following the date of shipment. Banner Engineering Corp. will repair or replace, free of charge, any product of its manufacture which, at the time it is returned to the factory, is found to have been defective during the warranty period. This warranty does not cover damage or liability for misuse, abuse, or the improper application or installation of the Banner product.

THIS LIMITED WARRANTY IS EXCLUSIVE AND IN LIEU OF ALL OTHER WARRANTIES WHETHER EXPRESS OR IMPLIED (INCLUDING, WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE), AND WHETHER ARISING UNDER COURSE OF PERFORMANCE, COURSE OF DEALING OR TRADE USAGE.

This Warranty is exclusive and limited to repair or, at the discretion of Banner Engineering Corp., replacement. IN NO EVENT SHALL BANNER ENGINEERING CORP. BE LIABLE TO BUYER OR ANY OTHER PERSON OR ENTITY FOR ANY EXTRA COSTS, EXPENSES, LOSSES, LOSS OF PROFITS, OR ANY INCIDENTAL, CONSEQUENTIAL OR SPECIAL DAMAGES RESULTING FROM ANY PRODUCT DEFECT OR FROM THE USE OR INABILITY TO USE THE PRODUCT, WHETHER ARISING IN CONTRACT OR WARRANTY, STATUTE, TORT, STRICT LIABILITY, NEGLIGENCE, OR OTHERWISE.

Banner Engineering Corp. reserves the right to change, modify or improve the design of the product without assuming any obligations or liabilities relating to any product previously manufactured by Banner Engineering Corp. Any misuse, abuse, or improper application or installation of this product or use of the product for personal protection applications when the product is identified as not intended for such purposes will void the product warranty. Any modifications to this product without prior express approval by Banner Engineering Corp will void the product warranties. All specifications published in this document are subject to change; Banner reserves the right to modify product specifications or update documentation at any time. Specifications and product information in English supersede that which is provided in any other language. For the most recent version of any documentation, refer to: www.bannerengineering.com.

For patent information, see www.bannerengineering.com/patents.