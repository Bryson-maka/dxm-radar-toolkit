<!-- image -->

## Server (3.x)

Pymodbus offers servers with transport protocols for

- Serial (RS-485) typically using a dongle
- TCP
- TLS
- UDP
- possibility to add a custom transport protocol

communication in 2 versions:

- synchronous server
- asynchronous server

```
, using asyncio.
```

Remark All servers are implemented with asyncio, and the synchronous servers are just an interface layer allowing synchronous applications to use the server as if it was synchronous.

Warning The current framer implementation does not support running the server on a shared rs485 line (multipoint).

Server classes .

class pymodbus.server.ModbusBaseServer ( params: CommParams , context: ModbusServerContext | None , ignore\_missing\_devices: bool , broadcast\_enable: bool , identity: ModbusDeviceIdentification | None , framer: FramerType , trace\_packet: Callable[[bool, bytes], bytes] | None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None , trace\_connect: Callable[[bool], None] | None , custom\_pdu: list[type[ModbusPDU]] | None )

Bases:

ModbusProtocol

Common functionality for all server classes.

active\_server

: ModbusBaseServer | None callback\_connected ()→ None

Call when connection is successful.

= None

<!-- image -->

latest

<!-- image -->

Handle received data.

<!-- image -->

class pymodbus.server.ModbusSerialServer ( context: ModbusServerContext , * , framer: FramerType = FramerType.RTU , ignore\_missing\_devices: bool = False , identity: ModbusDeviceIdentification | None = None , broadcast\_enable: bool = False , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None , custom\_pdu: list[type[ModbusPDU]] | None = None , **kwargs )

Bases:

ModbusBaseServer

A modbus threaded serial socket server.



Tip

Remember to call serve\_forever to start server.

class pymodbus.server.ModbusSimulatorServer ( modbus\_server: str = 'server' , modbus\_device: str = 'device' , http\_host: str = '0.0.0.0' , http\_port: int = 8080 , log\_file: str = 'server.log' , json\_file: str = 'setup.json' , custom\_actions\_module: str | None = None )

Bases:

object

ModbusSimulatorServer

.

Parameters:

modbus\_server

- Server name in json file (default: 'server')

- modbus\_device - Device name in json file (default: 'client')
- http\_host - TCP host for HTTP (default: 'localhost')
- http\_port - TCP port for HTTP (default: 8080)
- json\_file - setup file (default: 'setup.json')

custom\_actions\_module

(default: none)

- python module with custom actions latest

if either http\_port or http\_host is none, HTTP will not be started. This class starts a http server, that serves a couple of endpoints:

- '&lt;addr&gt;/' static files
- '&lt;addr&gt;/api/log' log handling, HTML with GET, REST-API with post
- '&lt;addr&gt;/api/registers' register handling, HTML with GET, REST-API with post
- '&lt;addr&gt;/api/calls' call (function code / message) handling, HTML with GET, REST-API with post
- '&lt;addr&gt;/api/server' server handling, HTML with GET, REST-API with post

## Example:

```
from pymodbus.server import ModbusSimulatorServer async def run(): simulator = ModbusSimulatorServer( modbus_server="my server", modbus_device="my device", http_host="localhost", http_port=8080) await simulator.run_forever(only_start= True ) ... await simulator.stop()
```

```
Build list of registers matching filter. Clear register filter. Start monitoring calls. Reset call simulation. Set register value. Simulate responses. action_add ( params , range_start , range_stop ) action_clear ( _params , _range_start , _range_stop ) action_monitor ( params , range_start , range_stop ) action_reset ( _params , _range_start , _range_stop ) action_set ( params , _range_start , _range_stop ) action_simulate ( params , _range_start , _range_stop )
```

```
latest
```

<!-- image -->

Stop call monitoring. action\_stop ( \_params , \_range\_start , \_range\_stop )

build\_html\_calls

(

params: dict

Build html calls page.

## build\_html\_log ( \_params , html )

Build html log page.

build\_html\_registers

(

params

,

html: str

,

html

)

Build html registers page.

build\_html\_server ( \_params , html )

Build html server page.

build\_json\_calls

(

params: dict

Build json calls response.

build\_json\_log

(

params

)

Build json log page.

## build\_json\_registers ( params )

Build json registers response.

build\_json\_server ( params )

Build html server page.

async handle\_html

Handle html.

async handle\_html\_static

Handle static html.

async handle\_json

(

request

Handle api registers.

(

request

)

)→ dict

)→ str

)

(

request

)

latest

Build html register submit.

Start modbus and http servers.

Start Modbus server as asyncio task.

Stop modbus and http servers.

Stop modbus server.

Bases:

ModbusBaseServer

A modbus threaded tcp socket server.

 Tip

Remember to call serve\_forever to start server.

Bases:

ModbusTcpServer

A modbus threaded tls socket server.

 Tip

Remember to call serve\_forever to start server.

helper\_handle\_submit ( params , submit\_actions )

async run\_forever ( only\_start=False )

async start\_modbus\_server ( app )

async

stop

()

async stop\_modbus\_server ( app )

class pymodbus.server.ModbusTcpServer ( context: ModbusServerContext , * , framer=FramerType.SOCKET , identity: ModbusDeviceIdentification | None = None , address: tuple[str, int] = ('', 502) , ignore\_missing\_devices: bool = False , broadcast\_enable: bool = False , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None , custom\_pdu: list[type[ModbusPDU]] | None = None )

class pymodbus.server.ModbusTlsServer ( context: ModbusServerContext , * , framer=FramerType.TLS , identity: ModbusDeviceIdentification | None = None , address: tuple[str, int] = ('', 502) , sslctx=None , certfile=None , keyfile=None , password=None , ignore\_missing\_devices=False , broadcast\_enable=False , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None , custom\_pdu: list[type[ModbusPDU]] | None = None )

latest

<!-- image -->

Bases:

ModbusBaseServer

A modbus threaded udp socket server.

 Tip

Remember to call serve\_forever to start server.

Terminate server.

Terminate server.

Start and run a serial modbus server.

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusSerialServer

 Tip

Only handles a single server !

Use ModbusSerialServer to allow multiple servers in one app.

Start and run a tcp modbus server.

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusTcpServer

 Tip

Only handles a single server !

class pymodbus.server.ModbusUdpServer ( context: ModbusServerContext , * , framer=FramerType.SOCKET , identity: ModbusDeviceIdentification | None = None , address: tuple[str, int] = ('', 502) , ignore\_missing\_devices: bool = False , broadcast\_enable: bool = False , trace\_packet: Callable[[bool, bytes], bytes] | None = None , trace\_pdu: Callable[[bool, ModbusPDU], ModbusPDU] | None = None , trace\_connect: Callable[[bool], None] | None = None , custom\_pdu: list[type[ModbusPDU]] | None = None )

async pymodbus.server.ServerAsyncStop ()→ None

pymodbus.server.ServerStop ()→ None

async pymodbus.server.StartAsyncSerialServer ( context: ModbusServerContext , **kwargs )→ None

async pymodbus.server.StartAsyncTcpServer ( context: ModbusServerContext , **kwargs )→ None

latest

<!-- image -->

Use ModbusTcpServer to allow multiple servers in one app.

Start and run a tls modbus server.

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusTlsServer

 Tip

Only handles a single server !

Use ModbusTlsServer to allow multiple servers in one app.

Start and run a udp modbus server.

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusUdpServer

 Tip

Only handles a single server !

Use ModbusUdpServer to allow multiple servers in one app.

Start and run a modbus serial server.

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusSerialServer

 Tip

Only handles a single server !

Use ModbusSerialServer to allow multiple servers in one app.

## async pymodbus.server.StartAsyncTlsServer ( context: ModbusServerContext , **kwargs )→ None

async pymodbus.server.StartAsyncUdpServer ( context: ModbusServerContext , **kwargs )→ None

## pymodbus.server.StartSerialServer ( context: ModbusServerContext , **kwargs )→ None

<!-- image -->

latest

<!-- image -->

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusTcpServer

 Tip

Only handles a single server !

Use ModbusTcpServer to allow multiple servers in one app.

Start and run a modbus TLS server.

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusTlsServer

 Tip

Only handles a single server !

Use ModbusTlsServer to allow multiple servers in one app.

Start and run a modbus UDP server. pymodbus.server.StartUdpServer ( context: ModbusServerContext , **kwargs )→ None

Parameters:

- context - Datastore object

- kwargs - for parameter explanation see ModbusUdpServer

 Tip

Only handles a single server !

Use ModbusUdpServer to allow multiple servers in one app.

Get command line arguments.

## pymodbus.server.StartTlsServer ( context: ModbusServerContext , **kwargs )→ None

pymodbus.server.get\_simulator\_commandline ( cmdline=None )

<!-- image -->

<!-- image -->