<!-- image -->

## Client

Pymodbus offers both a synchronous client and a asynchronous client . Both clients offer simple calls for each type of request, as well as a unified response, removing a lot of the complexities in the modbus protocol.

In addition to the 'pure' client, pymodbus offers a set of utilities converting to/from registers to/from 'normal' python values.

The client is NOT thread safe, meaning the application must ensure that calls are serialized. This is only a problem for synchronous applications that use multiple threads or for asynchronous applications that use multiple asyncio.create\_task .

It is allowed to have multiple client objects that e.g. each communicate with a TCP based device.

## Client performance

There are currently a big performance gap between the 2 clients.

This is due to a rather old implementation of the synchronous client, we are currently working to update the client code. Our aim is to achieve a similar data rate with both clients and at least double the data rate while keeping the stability. Table below is a test with 1000 calls each reading 10 registers.

| client        | asynchronous   | synchronous   |
|---------------|----------------|---------------|
| total time    | 0,33 sec       | 114,10 sec    |
| ms/call       | 0,33 ms        | 114,10 ms     |
| ms/register   | 0,03 ms        | 11,41 ms      |
| calls/sec     | 3.030          | 8             |
| registers/sec | 30.300         | 87            |

## Client protocols/framers

<!-- image -->

<!-- image -->

| protocol        | ASCII   | RTU   | RTU_OVER_TCP   | SOCKET   | TLS   |
|-----------------|---------|-------|----------------|----------|-------|
| SERIAL (RS-485) | Yes     | Yes   | No             | No       | No    |
| TCP             | Yes     | No    | Yes            | Yes      | No    |
| TLS             | No      | No    | No             | No       | Yes   |
| UDP             | Yes     | No    | Yes            | Yes      | No    |

## Serial (RS-485)

Pymodbus do not connect to the device (server) but connects to a comm port or usb port on the local computer.

RS-485 is a half duplex protocol, meaning the servers do nothing until the client sends a request then the server being addressed responds. The client controls the traffic and as a consequence one RS-485 line can only have 1 client but upto 254 servers (physical devices).

RS-485 is a simple 2 wire cabling with a pullup resistor. It is important to note that many USB converters do not have a builtin resistor, this must be added manually. When experiencing many faulty packets and retries this is often the problem.

## TCP

Pymodbus connects directly to the device using a standard socket and have a one-to-one connection with the device. In case of multiple TCP devices the application must instantiate multiple client objects one for each connection.

 Tip

<!-- image -->

a TCP device often represent multiple physical devices (e.g Ethernet-RS485 converter), each of these devices can be addressed normally

## TLS

A variant of TCP that uses encryption and certificates. TLS is mostly used when the devices are connected to the internet.

## UDP

<!-- image -->

## Client usage

Using pymodbus client to set/get information from a device (server) is done in a few simple steps.

## Synchronous example

```
from pymodbus.client import ModbusTcpClient client = ModbusTcpClient('MyDevice.lan') # Create client object client.connect() # connect to device client.write_coil(1, True , device_id=1) # set information in device result = client.read_coils(2, 3, device_id=1) # get information from device print(result.bits[0]) # use information client.close() # Disconnect device
```

The line client.connect() connects to the device (or comm port). If this cannot connect successfully within the timeout it throws an exception. After this initial connection, further calls to the same client (here, client.write\_coil(...) and client.read\_coils(...) ) will check whether the client is still connected, and automatically reconnect if not.

## Asynchronous example

```
from pymodbus.client import AsyncModbusTcpClient client = AsyncModbusTcpClient('MyDevice.lan') # Create client object await client.connect() # connect to device, reconnect automatically await client.write_coil(1, True , device_id=1) # set information in device result = await client.read_coils(2, 3, device_id=1) # get information from device print(result.bits[0]) # use information client.close() # Disconnect device
```

The line client = AsyncModbusTcpClient('MyDevice.lan') only creates the object; it does not activate anything.

The line await client.connect() connects to the device (or comm port), if this cannot connect successfully within the timeout it throws an exception. If connected successfully reconnecting later is handled automatically

<!-- image -->

The line await client.write\_coil(1, True, device\_id=1) is an example of a write request, set address 1 to True on device 1.

The line result = await client.read\_coils(2, 3, device\_id=1) is an example of a read request, get the value of address 2, 3 and 4 (count = 3) from device 1.

The last line client.close() closes the connection and render the object inactive.

## Retry logic for async clients

If no response is received to a request (call), it is retried (parameter retries) times, if not successful an exception response is returned, BUT the connection is not touched.

If 3 consequitve requests (calls) do not receive a response, the connection is terminated.

## Development notes

Large parts of the implementation are shared between the different classes, to ensure high stability and efficient maintenance. The synchronous clients are not thread safe nor is a single client intended to be used from multiple threads. Due to the nature of the modbus protocol, it makes little sense to have client calls split over different threads, however the application can do it with proper locking implemented. The asynchronous client only runs in the thread where the asyncio loop is created, it does not provide mechanisms to prevent (semi)parallel calls, that must be prevented at application level. Client device addressing With TCP , TLS and UDP , the tcp/ip address of the physical device is defined when creating the object. Logical devices represented by the device is addressed with the device\_id= parameter. With Serial , the comm port is defined when creating the object. The physical devices are addressed with the device\_id= parameter. device\_id=0 is defined as broadcast in the modbus standard, but pymodbus treats it as a normal device. please note device\_id=0 can only be used to address devices that truly have id=0 ! Using device\_id=0 to address a single device with id not 0 is against the protocol. If an application is expecting multiple responses to a broadcast request, it must call client.execute and deal with the responses. If no response is expected to a request, the no\_response\_expected=True argument can be used in the normal API calls, this will cause the call to return immediately with ExceptionResponse(0xff) latest

.

<!-- image -->

## Client response handling

All simple request calls (mixin) return a unified result independent whether it´s a read, write or diagnostic call.

The application should evaluate the result generically:

```
try : rr = await client.read_coils(1, 1, device_id=1) except ModbusException as exc: _logger.error(f"ERROR: exception in pymodbus { exc } ") raise exc if rr.isError(): _logger.error("ERROR: pymodbus returned an error!") raise ModbusException(txt)
```

except ModbusException as exc: happens generally when pymodbus experiences an internal error. There are a few situation where an unexpected response from a device can cause an exception.

rr.isError() is set whenever the device reports a problem.

And in case of read retrieve the data depending on type of request

- rr.bits is set for coils / input\_register requests
- rr.registers is set for other requests

Remark if using no\_response\_expected=True rr will always be None.

## Client interface classes

There are a client class for each type of communication and for asynchronous/synchronous

| Serial   | AsyncModbusSerialClient   | ModbusSerialClient   |
|----------|---------------------------|----------------------|
| TCP      | AsyncModbusTcpClient      | ModbusTcpClient      |
| TLS      | AsyncModbusTlsClient      | ModbusTlsClient      |
| UDP      | AsyncModbusUdpClient      | ModbusUdpClient      |

<!-- image -->

## Client common

Some methods are common to all clients:

class pymodbus.client.base.ModbusBaseClient ( framer: FramerType , retries: int , comm\_params: CommParams , trace\_packet: Callable[[bool, bytes], bytes] | None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None , trace\_connect: Callable[[bool], None] | None )

Bases: ModbusClientMixin [ Awaitable [ ModbusPDU ]] ModbusBaseClient . ModbusBaseClient is normally not referenced outside pymodbus . Return state of connection. Call transport connect. Register a custom response class with the decoder (call sync ). Parameters: custom\_response\_class - (optional) Modbus response class. Raises: MessageRegisterException - Check exception text. Use register() to add non-standard responses (like e.g. a login prompt) and have them interpreted automatically. Close connection. Override default max no request responses. Parameters: max\_count - Max aborted requests before disconnecting. The parameter retries defines how many times a request is retried before being aborted. Once aborted a counter is incremented, and when this counter is greater than max\_count the connection is terminated. property connected : bool async connect ()→ bool register ( custom\_response\_class: type[ModbusPDU] )→ None close ()→ None set\_max\_no\_responses ( max\_count: int )→ None latest



Tip

When a request is successful the count is reset.

class pymodbus.client.base.ModbusBaseSyncClient ( framer: FramerType , retries: int , comm\_params: CommParams , trace\_packet: Callable[[bool, bytes], bytes] | None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None , trace\_connect: Callable[[bool], None] | None )

Bases: ModbusClientMixin [ ModbusPDU ]

ModbusBaseClient .

ModbusBaseClient is normally not referenced outside pymodbus .

register ( custom\_response\_class: type[ModbusPDU] )→ None

Register a custom response class with the decoder.

Parameters:

Raises:

custom\_response\_class

- (optional) Modbus response class.

MessageRegisterException - Check exception text.

Use register() to add non-standard responses (like e.g. a login prompt) and have them interpreted automatically.

## idle\_time ()→ float

Time before initiating next transaction (call sync ).

Applications can call message functions without checking idle\_time(), this is done automatically.

```
set_max_no_responses ( max_count: int )→ None
```

Override default max no request responses.

Parameters: max\_count - Max aborted requests before disconnecting.

The parameter retries defines how many times a request is retried before being aborted. Once aborted a counter is incremented, and when this counter is greater than max\_count the connection is terminated.

<!-- image -->

When a request is successful the count is reset.

## connect ()→ bool

Connect to other end, overwritten.

latest

<!-- image -->

Close connection, overwritten.

## Client serial

class pymodbus.client.AsyncModbusSerialClient ( port: str , * , framer: FramerType = FramerType.RTU , baudrate: int = 19200 , bytesize: int = 8 , parity: str = 'N' , stopbits: int = 1 , handle\_local\_echo: bool = False , name: str = 'comm' , reconnect\_delay: float = 0.1 , reconnect\_delay\_max: float = 300 , timeout: float = 3 , retries: int = 3 , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None )

Bases: ModbusBaseClient

## AsyncModbusSerialClient .

Fixed parameters:

Parameters:

port - Serial port used for communication.

Optional parameters:

## Parameters:

 Tip

The trace methods allow to modify the datastream/pdu !



Tip

- framer - Framer name, default FramerType.RTU
- baudrate - Bits per second.
- bytesize - Number of bits per byte 7-8.
- parity - 'E'ven, 'O'dd or 'N'one
- stopbits - Number of stop bits 1, 1.5, 2.
- handle\_local\_echo - Discard local echo from dongle.
- name - Set communication name, used in logging
- reconnect\_delay - Minimum delay in seconds.milliseconds before reconnecting.
- reconnect\_delay\_max - Maximum delay in seconds.milliseconds before reconnecting.
- timeout - Timeout for connecting and receiving data, in seconds.
- retries - Max number of retries per request.
- trace\_packet - Called with bytestream received/to be sent
- trace\_pdu - Called with PDU received/to be sent
- trace\_connect - Called when connected/disconnected

latest

<!-- image -->

reconnect\_delay doubles automatically with each unsuccessful connect, from reconnect\_delay to reconnect\_delay\_max . Set reconnect\_delay=0 to avoid automatic reconnection.

## Example:

```
from pymodbus.client import AsyncModbusSerialClient async def run(): client = AsyncModbusSerialClient("dev/serial0") await client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

class pymodbus.client.ModbusSerialClient ( port: str , * , framer: FramerType = FramerType.RTU , baudrate: int = 19200 , bytesize: int = 8 , parity: str = 'N' , stopbits: int = 1 , handle\_local\_echo: bool = False , name: str = 'comm' , reconnect\_delay: float = 0.1 , reconnect\_delay\_max: float = 300 , timeout: float = 3 , retries: int = 3 , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None )

Bases: ModbusBaseSyncClient

## ModbusSerialClient .

Fixed parameters:

Parameters: port

## Optional parameters:

```
Parameters: framer - Framer name, default FramerType.RTU baudrate - Bits per second. bytesize - Number of bits per byte 7-8. parity - 'E'ven, 'O'dd or 'N'one stopbits - Number of stop bits 0-2. handle_local_echo - Discard local echo from dongle. name - Set communication name, used in logging reconnect_delay - Not used in the sync client reconnect_delay_max - Not used in the sync client timeout - Timeout for connecting and receiving data, in seconds. retries - Max number of retries per request. trace_packet - Called with bytestream received/to be sent latest
```

- trace\_pdu - Called with PDU received/to be sent

- Serial port used for communication.

 Tip

The trace methods allow to modify the datastream/pdu !

## Example:

```
from pymodbus.client import ModbusSerialClient def run(): client = ModbusSerialClient("dev/serial0") client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

```
Check if socket exists. Connect to the modbus serial server. Close the underlying socket connection. Send data on the underlying socket. Read data from the underlying descriptor. Check if socket is open. property connected : bool connect ()→ bool close () send ( request: bytes , addr: tuple | None = None )→ int recv ( size: int | None )→ bytes is_socket_open ()→ bool
```

## Client TCP

- trace\_connect - Called when connected/disconnected

<!-- image -->

reconnect\_delay: float = 0.1 , reconnect\_delay\_max: float = 300 , timeout: float = 3 , retries: int = 3 , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None )

Bases: ModbusBaseClient

## AsyncModbusTcpClient .

Fixed parameters:

Parameters: host - Host IP address or host name

Optional parameters:

| Parameters:   | framer - Framer name, default FramerType.SOCKET                              |
|---------------|------------------------------------------------------------------------------|
|               | port - Port used for communication                                           |
|               | name - Set communication name, used in logging                               |
|               | source_address - source address of client                                    |
|               | reconnect_delay - Minimum delay in seconds.milliseconds before reconnecting. |
|               | reconnect_delay_max - Maximum delay in seconds.milliseconds before           |
|               | reconnecting.                                                                |
|               | retries - Max number of retries per request.                                 |
|               | trace_packet - Called with bytestream received/to be sent                    |
|               | trace_pdu - Called with PDU received/to be sent                              |
|               | trace_connect - Called when connected/disconnected                           |



Tip

The trace methods allow to modify the datastream/pdu !



Tip reconnect\_delay doubles automatically with each unsuccessful connect, from reconnect\_delay to reconnect\_delay\_max . Set reconnect\_delay=0 to avoid automatic reconnection.

Example:

latest

```
from pymodbus.client import AsyncModbusTcpClient async def run(): client = AsyncModbusTcpClient("localhost") await client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

class pymodbus.client.ModbusTcpClient ( host: str , * , framer: FramerType = FramerType.SOCKET , port: int = 502 , name: str = 'comm' , source\_address: tuple[str, int] | None = None , reconnect\_delay: float = 0.1 , reconnect\_delay\_max: float = 300 , timeout: float = 3 , retries: int = 3 , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None )

Bases:

ModbusBaseSyncClient

## ModbusTcpClient .

Fixed parameters:

Parameters:

host - Host IP address or host name

## Optional parameters:

Parameters:

 Tip

The trace methods allow to modify the datastream/pdu !

- framer - Framer name, default FramerType.SOCKET
- port - Port used for communication
- name - Set communication name, used in logging
- source\_address - source address of client
- reconnect\_delay - Not used in the sync client
- reconnect\_delay\_max - Not used in the sync client
- timeout - Timeout for connecting and receiving data, in seconds.
- retries - Max number of retries per request.
- trace\_packet - Called with bytestream received/to be sent
- trace\_pdu - Called with PDU received/to be sent
- trace\_connect - Called when connected/disconnected

<!-- image -->

```
from pymodbus.client import ModbusTcpClient async def run(): client = ModbusTcpClient("localhost") client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

```
Check if socket exists. Connect to the modbus tcp server. Close the underlying socket connection. Send data on the underlying socket. Read data from the underlying descriptor. Check if socket is open. property connected : bool connect () close () send ( request , addr: tuple | None = None ) recv ( size: int | None )→ bytes is_socket_open ()→ bool
```

## Client TLS

class pymodbus.client.AsyncModbusTlsClient ( host: str, *, sslctx: ~ssl.SSLContext = &lt;ssl.SSLContext object&gt;, framer: ~pymodbus.framer.base.FramerType = FramerType.TLS, port: int = 802, name: str = 'comm', source\_address: tuple[str, int] | None = None, reconnect\_delay: float = 0.1, reconnect\_delay\_max: float = 300, timeout: float = 3, retries: int = 3, trace\_packet: ~collections.abc.Callable[[bool, bytes], bytes] | None = None, trace\_pdu: ~collections.abc.Callable[[bool, ~pymodbus.pdu.pdu.ModbusPDU], ~pymodbus.pdu.pdu.ModbusPDU] | None = None, trace\_connect: ~collections.abc.Callable[[bool], None] | None = None )

Bases:

AsyncModbusTcpClient

## AsyncModbusTlsClient .

Fixed parameters:

<!-- image -->

## Optional parameters:

Parameters:

 Tip

The trace methods allow to modify the datastream/pdu !

 Tip reconnect\_delay doubles automatically with each unsuccessful connect, from reconnect\_delay to reconnect\_delay\_max . Set reconnect\_delay=0 to avoid automatic reconnection.

## Example:

```
from pymodbus.client import AsyncModbusTlsClient async def run(): client = AsyncModbusTlsClient("localhost") await client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

- Host IP address or host name

- sslctx - SSLContext to use for TLS
- framer - Framer name, default FramerType.TLS
- port - Port used for communication
- name - Set communication name, used in logging
- source\_address - Source address of client
- reconnect\_delay - Minimum delay in seconds.milliseconds before reconnecting.
- reconnect\_delay\_max - Maximum delay in seconds.milliseconds before reconnecting.
- timeout - Timeout for connecting and receiving data, in seconds.
- retries - Max number of retries per request.
- trace\_packet - Called with bytestream received/to be sent
- trace\_pdu - Called with PDU received/to be sent
- trace\_connect - Called when connected/disconnected

<!-- image -->

## Generate sslctx from cert/key/password.

Parameters:

- certfile - Cert file path for TLS server request

- keyfile - Key file path for TLS server request

- password - Password for for decrypting private key file

Remark: - MODBUS/TCP Security Protocol Specification demands TLSv2 at least -verify\_mode is set to ssl.NONE

class pymodbus.client.ModbusTlsClient ( host: str, *, sslctx: ~ssl.SSLContext = &lt;ssl.SSLContext object&gt;, framer: ~pymodbus.framer.base.FramerType = FramerType.TLS, port: int = 802, name: str = 'comm', source\_address: tuple[str, int] | None = None, reconnect\_delay: float = 0.1, reconnect\_delay\_max: float = 300, timeout: float = 3, retries: int = 3, trace\_packet: ~collections.abc.Callable[[bool, bytes], bytes] | None = None, trace\_pdu: ~collections.abc.Callable[[bool, ~pymodbus.pdu.pdu.ModbusPDU], ~pymodbus.pdu.pdu.ModbusPDU] | None = None, trace\_connect: ~collections.abc.Callable[[bool], None] | None = None )

Bases:

ModbusTcpClient

## ModbusTlsClient .

Fixed parameters:

Parameters:

host - Host IP address or host name

## Optional parameters:

Parameters:

<!-- image -->

The trace methods allow to modify the datastream/pdu !

- sslctx - SSLContext to use for TLS
- framer - Framer name, default FramerType.TLS
- port - Port used for communication
- name - Set communication name, used in logging
- source\_address - Source address of client
- reconnect\_delay - Not used in the sync client
- reconnect\_delay\_max - Not used in the sync client
- timeout - Timeout for connecting and receiving data, in seconds.
- retries - Max number of retries per request.
- trace\_packet - Called with bytestream received/to be sent
- trace\_pdu - Called with PDU received/to be sent
- trace\_connect - Called when connected/disconnected

<!-- image -->

<!-- image -->

```
from pymodbus.client import ModbusTlsClient async def run(): client = ModbusTlsClient("localhost") client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

classmethod generate\_ssl ( certfile: str | None = None , keyfile: str | None = None , password: str | None = None )→ SSLContext

Generate sslctx from cert/key/password.

- Parameters: certfile - Cert file path for TLS server request keyfile - Key file path for TLS server request
- password - Password for for decrypting private key file

Remark: - MODBUS/TCP Security Protocol Specification demands TLSv2 at least -verify\_mode is set to ssl.NONE

```
Connect internal. Connect to the modbus tls server. property connected : bool connect ()
```

## Client UDP

class pymodbus.client.AsyncModbusUdpClient ( host: str , * , framer: FramerType = FramerType.SOCKET , port: int = 502 , name: str = 'comm' , source\_address: tuple[str, int] | None = None , reconnect\_delay: float = 0.1 , reconnect\_delay\_max: float = 300 , timeout: float = 3 , retries: int = 3 , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None )

Bases: ModbusBaseClient

AsyncModbusUdpClient .

Fixed parameters:

Parameters:

host - Host IP address or host name

<!-- image -->

Parameters:

 Tip

The trace methods allow to modify the datastream/pdu !

 Tip reconnect\_delay doubles automatically with each unsuccessful connect, from reconnect\_delay to reconnect\_delay\_max . Set reconnect\_delay=0 to avoid automatic reconnection.

## Example:

```
from pymodbus.client import AsyncModbusUdpClient async def run(): client = AsyncModbusUdpClient("localhost") await client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

```
class pymodbus.client.ModbusUdpClient ( host: str , * , framer: FramerType = FramerType.SOCKET , port: int = 502 , name: str = 'comm' , source_address: tuple[str, int] | None = None , reconnect_delay: float = 0.1 , reconnect_delay_max: float = 300 , timeout: float = 3 , retries: int = 3 , trace_packet: Callable[[bool, bytes], bytes] | None = None , trace_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace_connect: Callable[[bool], None] | None = None ) latest
```

Bases:

ModbusBaseSyncClient

- framer - Framer name, default FramerType.SOCKET
- port - Port used for communication.
- name - Set communication name, used in logging
- source\_address - source address of client,
- reconnect\_delay - Minimum delay in seconds.milliseconds before reconnecting.
- reconnect\_delay\_max - Maximum delay in seconds.milliseconds before reconnecting.
- timeout - Timeout for connecting and receiving data, in seconds.
- retries - Max number of retries per request.
- trace\_packet - Called with bytestream received/to be sent
- trace\_pdu - Called with PDU received/to be sent
- trace\_connect - Called when connected/disconnected

<!-- image -->

## ModbusUdpClient .

Fixed parameters:

Parameters:

host - Host IP address or host name

## Optional parameters:

- Parameters: framer - Framer name, default FramerType.SOCKET port - Port used for communication. name - Set communication name, used in logging source\_address - source address of client, reconnect\_delay - Not used in the sync client reconnect\_delay\_max - Not used in the sync client timeout - Timeout for connecting and receiving data, in seconds. retries - Max number of retries per request. trace\_packet - Called with bytestream received/to be sent trace\_pdu - Called with PDU received/to be sent trace\_connect - Called when connected/disconnected

 Tip

The trace methods allow to modify the datastream/pdu !

## Example:

```
from pymodbus.client import ModbusUdpClient async def run(): client = ModbusUdpClient("localhost") client.connect() ... client.close()
```

Please refer to Pymodbus internals for advanced usage.

```
Connect internal. property connected : bool
```

## Modbus calls

Pymodbus makes all standard modbus requests/responses available as simple calls.

<!-- image -->

Using Modbus&lt;transport&gt;Client.register() custom messages can be added to pymodbus, and handled automatically.

## class pymodbus.client.mixin.ModbusClientMixin

```
Bases: Generic [ T ]
```

## ModbusClientMixin .

This is an interface class to facilitate the sending requests/receiving responses like read\_coils. execute() allows to make a call with non-standard or user defined function codes (remember to add a PDU in the transport class to interpret the request/response).

Simple modbus message call:

```
response = client.read_coils(1, 10) # or response = await client.read_coils(1, 10)
```

Advanced modbus message call:

```
request = ReadCoilsRequest(1,10) response = client.execute( False , request) # or request = ReadCoilsRequest(1,10) response = await client.execute( False , request)
```

 Tip

All methods can be used directly (synchronous) or with await &lt;method&gt; (asynchronous) depending on the client used.

```
abstractmethod execute ( no_response_expected: bool , request: ModbusPDU )→ T
```

Execute request.

```
read_coils ( address: int , * , count: int = 1 , device_id: int = 1 , no_response_expected: bool = False )→ T
```

Read coils (code 0x01).

- Parameters: address - Start address to read from count - (optional) Number of coils to read device\_id - (optional) Modbus device ID

latest

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises: ModbusException -

reads from 1 to 2000 contiguous in a remote device.

Coils are addressed as 0-N (Note some device manuals uses 1-N, assuming 1==0).

read\_discrete\_inputs ( address: int , * , count: int = 1 , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Read discrete inputs (code 0x02).

## Parameters:

- address - Start address to read from

- count - (optional) Number of coils to read

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

read from 1 to 2000(0x7d0) discrete inputs (bits) in a remote device.

Discrete Inputs are addressed as 0-N (Note some device manuals uses 1-N, assuming 1==0).

read\_holding\_registers ( address: int , * , count: int = 1 , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Read holding registers (code 0x03).

## Parameters:

- address - Start address to read from

- count - (optional) Number of registers to read

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

This function is used to read the contents of a contiguous block of holding registers in a remote device. The Request specifies the starting register address and the number of registers.

Registers are addressed starting at zero. Therefore devices that specify 1-16 are addressed as 0-15.

<!-- image -->

Read input registers (code 0x04).

Parameters:

- address - Start address to read from

- count - (optional) Number of registers to read

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

This function is used to read from 1 to approx. 125 contiguous input registers in a remote device. The Request specifies the starting register address and the number of registers.

Registers are addressed starting at zero. Therefore devices that specify 1-16 are addressed as 0-15.

Write single coil (code 0x05). write\_coil ( address: int , value: bool , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- address - Address to write to

- value - Boolean to write

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

write ON/OFF to a single coil in a remote device.

Coils are addressed as 0-N (Note some device manuals uses 1-N, assuming 1==0).

```
write_register ( address: int , value: int , * , device_id: int = 1 , no_response_expected: bool = False )→ T
```

Write register (code 0x06).

## Parameters:

- address - Address to write to

- value - Value to write

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises:

ModbusException -

This function is used to write a single holding register in a remote device.

<!-- image -->

latest

The Request specifies the address of the register to be written.

<!-- image -->

Read Exception Status (code 0x07). read\_exception\_status ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

This function is used to read the contents of eight Exception Status outputs in a remote device.

The function provides a simple method for accessing this information, because the Exception Output references are known (no output reference is needed in the function).

Diagnose query data (code 0x08 sub 0x00). diag\_query\_data ( msg: bytes , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- msg - Message to be returned

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The data passed in the request data field is to be returned (looped back) in the response. The entire response message should be identical to the request.

diag\_restart\_communication ( toggle: bool , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Diagnose restart communication (code 0x08 sub 0x01).

Parameters:

- toggle - True if toggled.

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The remote device serial line port must be initialized and restarted, and all of its communications event counters are cleared. If the port is currently in Listen Only Mode, no response is returned. This function is the only one that brings the port out of Listen Only Mode. If the port is not currently in Listen Only Mode, a normal response is returned. This occurs before the restart is update\_datastored. latest

<!-- image -->

Diagnose read diagnostic register (code 0x08 sub 0x02).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The contents of the remote device's 16-bit diagnostic register are returned in the response.

```
diag_change_ascii_input_delimeter ( * , delimiter: int = 10 , device_id: int = 1 , no_response_expected: bool = False )→ T
```

Diagnose change ASCII input delimiter (code 0x08 sub 0x03).

Parameters:

- delimiter - char to replace LF

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The character passed in the request becomes the end of message delimiter for future messages (replacing the default LF character). This function is useful in cases of a Line Feed is not required at the end of ASCII messages.

```
diag_force_listen_only ( * , device_id: int = 1 , no_response_expected: bool = False )→ T
```

Diagnose force listen only (code 0x08 sub 0x04).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

Forces the addressed remote device to its Listen Only Mode for MODBUS communications.

This isolates it from the other devices on the network, allowing them to continue communicating without interruption from the addressed remote device. No response is returned.

```
diag_clear_counters ( * , device_id: int = 1 , no_response_expected: bool = False )→ T
```

<!-- image -->

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

Clear ll counters and the diagnostic register. Also, counters are cleared upon power-up

Diagnose read bus message count (code 0x08 sub 0x0B). diag\_read\_bus\_message\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The response data field returns the quantity of messages that the remote device has detected on the communications systems since its last restart, clear counters operation, or power-up diag\_read\_bus\_comm\_error\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Diagnose read Bus Communication Error Count (code 0x08 sub 0x0C).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The response data field returns the quantity of CRC errors encountered by the remote device since its last restart, clear counter operation, or power-up diag\_read\_bus\_exception\_error\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Diagnose read Bus Exception Error Count (code 0x08 sub 0x0D).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException

-

latest

<!-- image -->

Diagnose read device Message Count (code 0x08 sub 0x0E).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The response data field returns the quantity of messages addressed to the remote device, that the remote device has processed since its last restart, clear counters operation, or power-up diag\_read\_device\_no\_response\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Diagnose read device No Response Count (code 0x08 sub 0x0F).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The response data field returns the quantity of messages addressed to the remote device, that the remote device has processed since its last restart, clear counters operation, or power-up.

Diagnose read device NAK Count (code 0x08 sub 0x10). diag\_read\_device\_nak\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

The response data field returns the quantity of messages addressed to the remote device for which it returned a Negative ACKNOWLEDGE (NAK) exception response, since its last restart, clear counters operation, or power-up. Exception responses are described and listed in section 7 .

diag\_read\_device\_busy\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False

)→ T

latest

Diagnose read device Busy Count (code 0x08 sub 0x11).

Parameters:

device\_id

- (optional) Modbus device ID

<!-- image -->

Raises:

- no\_response\_expected - (optional) The client will not expect a response to the request

ModbusException

-

The response data field returns the quantity of messages addressed to the remote device for which it returned device Busy exception response, since its last restart, clear counters operation, or power-up.

diag\_read\_bus\_char\_overrun\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Diagnose read Bus Character Overrun Count (code 0x08 sub 0x12).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException

-

The response data field returns the quantity of messages addressed to the remote device that it could not handle due to a character overrun condition, since its last restart, clear counters operation, or power-up. A character overrun is caused by data characters arriving at the port faster than they can be stored, or by the loss of a character due to a hardware malfunction.

Diagnose read Iop overrun count (code 0x08 sub 0x13). diag\_read\_iop\_overrun\_count ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException

-

An IOP overrun is caused by data characters arriving at the port faster than they can be stored, or by the loss of a character due to a hardware malfunction. This function is specific to the 884.

Diagnose Clear Overrun Counter and Flag (code 0x08 sub 0x14). diag\_clear\_overrun\_counter ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException

-

latest

An error flag should be cleared, but nothing else in the specification mentions is, so it is ignored.

diag\_getclear\_modbus\_response ( * , data: int = 0 , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Diagnose Get/Clear modbus plus (code 0x08 sub 0x15).

Parameters:

- data - 'Get Statistics' or 'Clear Statistics'

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

In addition to the Function code (08) and Subfunction code (00 15 hex) in the query, a two-byte Operation field is used to specify either a 'Get Statistics' or a 'Clear Statistics' operation. The two operations are exclusive - the 'Get' operation cannot clear the statistics, and the 'Clear' operation does not return statistics prior to clearing them. Statistics are also cleared on power-up of the device,

Diagnose get event counter (code 0x0B). diag\_get\_comm\_event\_counter ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

This function is used to get a status word and an event count from the remote device.

By fetching the current count before and after a series of messages, a client can determine whether the messages were handled normally by the remote device.

The device's event counter is incremented once for each successful message completion. It is not incremented for exception responses, poll commands, or fetch event counter commands.

The event counter can be reset by means of the Diagnostics function Restart Communications or Clear Counters and Diagnostic Register.

Diagnose get event counter (code 0x0C). diag\_get\_comm\_event\_log ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

device\_id

- (optional) Modbus device ID

latest

<!-- image -->

Raises:

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises: ModbusException -

This function is used to get a status word. Event count, message count, and a field of event bytes from the remote device. The status word and event counts are identical to that returned by the Get Communications Event Counter function. The message counter contains the quantity of messages processed by the remote device since its last restart, clear counters operation, or power-up. This count is identical to that returned by the Diagnostic function Return Bus Message Count. The event bytes field contains 0-64 bytes, with each byte corresponding to the status of one MODBUS send or receive operation for the remote device. The remote device enters the events into the field in chronological order. Byte 0 is the most recent event. Each new byte flushes the oldest byte from the field.

## write\_coils ( address: int , values: list[bool] , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Write coils (code 0x0F).

## Parameters:

- address - Start address to write to
- values - List of booleans to write, or a single boolean to write
- device\_id - (optional) Modbus device ID
- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises: ModbusException -

write ON/OFF to multiple coils in a remote device. Coils are addressed as 0-N (Note some device manuals uses 1-N, assuming 1==0).

write\_registers ( address: int , values: list[int] , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Write registers (code 0x10).

## Parameters:

- address - Start address to write to
- values - List of values to write
- device\_id - (optional) Modbus device ID
- no\_response\_expected - (optional) The client will not expect a response to the request latest

ModbusException

-

This function is used to write a block of contiguous registers (1 to approx. 120 registers) in a remote device.

report\_device\_id ( * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Report device ID (code 0x11).

Parameters:

- device\_id - (optional) Modbus device ID

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

This function is used to read the description of the type, the current status and other information specific to a remote device.

read\_file\_record ( records: list[FileRecord] , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Read file record (code 0x14).

Parameters:

- records - List of FileRecord (Reference type, File number, Record Number)

- device\_id - device id

- no\_response\_expected - (optional) The client will not expect a response to the request

Raises:

ModbusException -

This function is used to perform a file record read. All request data lengths are provided in terms of number of bytes and all record lengths are provided in terms of registers.

A file is an organization of records. Each file contains 10000 records, addressed 0000 to 9999 decimal or 0x0000 to 0x270f. For example, record 12 is addressed as 12. The function can read multiple groups of references. The groups can be separating (noncontiguous), but the references within each group must be sequential. Each group is defined in a separate 'sub-request' field that contains seven bytes:

```
The reference type: 1 byte The file number: 2 bytes The starting record number within the file: 2 bytes The length of the record to be read: 2 bytes
```

The quantity of registers to be read, combined with all other fields in the expected response, must not exceed the allowable length of the MODBUS PDU: 235 bytes.

<!-- image -->

write\_file\_record ( records: list[FileRecord] , * , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Write file record (code 0x15).

## Parameters:

- records - List of File\_record (Reference type, File number, Record Number, Record Length, Record Data)

- device\_id - (optional) Device id

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises:

ModbusException

-

This function is used to perform a file record write. All request data lengths are provided in terms of number of bytes and all record lengths are provided in terms of the number of 16 bit words.

mask\_write\_register ( * , address: int = 0 , and\_mask: int = 65535 , or\_mask: int = 0 , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Mask write register (code 0x16).

## Parameters:

## Raises:

- address - The mask pointer address (0x0000 to 0xffff)
- and\_mask - The and bitmask to apply to the register address
- or\_mask - The or bitmask to apply to the register address
- device\_id - (optional) device id
- no\_response\_expected - (optional) The client will not expect a response to the request

ModbusException

-

This function is used to modify the contents of a specified holding register using a combination of an AND mask, an OR mask, and the register's current contents.

The function can be used to set or clear individual bits in the register.

readwrite\_registers ( * , read\_address: int = 0 , read\_count: int = 0 , write\_address: int = 0 , address: int | None = None , values: list[int] | None = None , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Read/Write registers (code 0x17).

## Parameters:

- read\_address - The address to start reading from
- read\_count - The number of registers to read from address
- write\_address - The address to start writing to
- address - (optional) use as read/write address
- values - List of values to write, or a single value to write
- device\_id - (optional) Modbus device ID

latest

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises: ModbusException -

This function performs a combination of one read operation and one write operation in a single MODBUS transaction. The write operation is performed before the read.

Holding registers are addressed starting at zero. Therefore holding registers 1-16 are addressed in the PDU as 0-15.

Read FIFO queue (code 0x18). read\_fifo\_queue ( * , address: int = 0 , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

## Parameters:

- address - The address to start reading from

- device\_id - (optional) device id

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises:

ModbusException

-

This function allows to read the contents of a First-In-First-Out (FIFO) queue of register in a remote device. The function returns a count of the registers in the queue, followed by the queued data. Up to 32 registers can be read: the count, plus up to 31 queued data registers.

The queue count register is returned first, followed by the queued data registers. The function reads the queue contents, but does not clear them.

read\_device\_information ( * , read\_code: int | None = None , object\_id: int = 0 , device\_id: int = 1 , no\_response\_expected: bool = False )→ T

Read FIFO queue (code 0x2B sub 0x0E).

## Parameters:

- read\_code - The device information read code

- object\_id - The object to read from

- device\_id - (optional) Device id

- no\_response\_expected - (optional) The client will not expect a response to the request

## Raises: ModbusException -

This function allows reading the identification and additional information relative to the physical and functional description of a remote device, only. latest

The Read Device Identification interface is modeled as an address space composed of a set of addressable data elements. The data elements are called objects and an object Id identifies them.

<!-- image -->

class

DATATYPE

Bases:

Enum

Datatype enum (name and internal data), used for convert\_* calls.

classmethod convert\_from\_registers ( registers: list[int] , data\_type: DATATYPE , word\_order: Literal['big', 'little'] = 'big' , string\_encoding: str = 'utf-8' )→ int | float | str | list[bool] | list[int] | list[float]

Convert registers to int/float/str.

## Parameters:

- registers - list of registers received from e.g. read\_holding\_registers()

- data\_type - data type to convert to

- word\_order - 'big'/'little' order of words/registers

- string\_encoding - The encoding with which to decode the bytearray, only used when data\_type=DATATYPE.STRING

Returns:

scalar or array of 'data\_type'

Raises:

- ModbusException - when size of registers is not a multiple of data\_type

- ParameterException - when the specified string encoding is not supported

classmethod convert\_to\_registers ( value: int | float | str | list[bool] | list[int] | list[float] , data\_type: DATATYPE , word\_order: Literal['big', 'little'] = 'big' , string\_encoding: str = 'utf-8' )→ list[int]

Convert int/float/str to registers (16/32/64 bit).

## Parameters:

- value - value to be converted

- data\_type - data type to convert from

- word\_order - 'big'/'little' order of words/registers

- string\_encoding - The encoding with which to encode the bytearray, only used when data\_type=DATATYPE.STRING

Returns:

List of registers, can be used directly in e.g. write\_registers()

Raises:

- TypeError - when there is a mismatch between data\_type and value

- ParameterException - when the specified string encoding is not supported

latest

(

value

)

<!-- image -->