<!-- image -->

## Welcome to PyModbus's documentation!

Please select a topic in the left hand column.

## PyModbus - A Python Modbus Stack

<!-- image -->

Pymodbus is a full Modbus protocol implementation offering a client and server with synchronous/asynchronous API and simulators.

Our releases follow the pattern X.Y.Z . We have strict rules for what different version number updates mean:

- Z , No API changes! bug fixes and smaller enhancements.
- Y , API changes, bug fixes and bigger enhancements.
- X , Major changes in API and/or method to use pymodbus

Upgrade examples:

- 3.9.0 -&gt; 3.9.2: just plugin the new version, no changes needed.

Remark fixing bugs, can lead to a different behaviors/returns

- 3.8.0 -&gt; 3.9.0: Smaller changes to the pymodbus calls might be needed
- 2.5.4 -&gt; 3.0.0: Major changes in the application might be needed

It is always recommended to read the CHANGELOG as well as the API\_changes files.

Current release is 3.11.0.

Bleeding edge (not released) is dev.

All changes are described in release notes and all API changes are documented

A big thanks to all the volunteers that helps make pymodbus a great project.

Source code on github

<!-- image -->

<!-- image -->

## Pymodbus in a nutshell

Pymodbus consist of 5 parts:

- client , connect to your favorite device(s)
- server , simulate your favorite device(s)
- repl , a commandline text based client/server simulator
- simulator , an html based server simulator
- examples , showing both simple and advances usage

## Common features

- Full modbus standard protocol implementation
- Support for custom function codes
- Support serial (rs-485), tcp, tls and udp communication
- Support all standard frames: socket, rtu, rtu-over-tcp, tcp and ascii
- Does not have third party dependencies, apart from pyserial (optional)
- Very lightweight project
- Requires Python &gt;= 3.10
- Thorough test suite, that test all corners of the library
- Automatically tested on Windows, Linux and MacOS combined with python 3.10 - 3.13
- Strongly typed API (py.typed present)

The modbus protocol specification: Modbus\_Application\_Protocol\_V1\_1b3.pdf can be found on modbus org

## Client Features

- Asynchronous API and synchronous API for applications
- Very simple setup and call sequence (just 6 lines of code)
- Utilities to convert int/float to/from multiple registers
- Encoder/decoder to help with standard python data types

## Client documentation

## Server Features

- Asynchronous implementation for high performance
- Synchronous API classes for convenience

<!-- image -->

<!-- image -->

- Simulate real life devices
- Full server control context (device information, counters, etc)
- Different backend datastores to manage register values
- Callback to intercept requests/responses
- Work on RS485 in parallel with other devices

## Server documentation

## REPL Features

- Server/client commandline emulator
- Easy test of real device (client)
- Easy test of client app (server)
- Simulation of broken requests/responses
- Simulation of error responses (hard to provoke in real devices)

## REPL documentation

## Simulator Features

- Server simulator with WEB interface
- Configure the structure of a real device
- Monitor traffic online
- Allow distributed team members to work on a virtual device using internet
- Simulation of broken requests/responses
- Simulation of error responses (hard to provoke in real devices)

## Simulator documentation

## Use Cases

The client is the most typically used. It is embedded into applications, where it abstract the modbus protocol from the application by providing an easy to use API. The client is integrated into some well known projects like home-assistant.

Although most system administrators will find little need for a Modbus server, the server is handy to verify the functionality of an application.

The simulator and/or server is often used to simulate real life devices testing applications. The server is excellent to perform high volume testing (e.g. hundreds of devices connected to the application). The advantage of the server is that it runs not only on 'normal' computers but also on small ones like a Raspberry PI. v3.11.0

<!-- image -->

Since the library is written in python, it allows for easy scripting and/or integration into existing solutions.

For more information please browse the project documentation:

https:/ /readthedocs.org/docs/pymodbus/en/latest/index.html

## Install

The library is available on pypi.org and github.com to install with

- pip for those who just want to use the library
- git clone for those who wants to help or just are curious

Be aware that there are a number of project, who have forked pymodbus and

- Seems just to provide a version frozen in time
- Extended pymodbus with extra functionality

The latter is not because we rejected the extra functionality (we welcome all changes), but because the codeowners made that decision.

In both cases, please understand, we cannot offer support to users of these projects as we do not known what have been changed nor what status the forked code have.

A growing number of Linux distributions include pymodbus in their standard installation.

You need to have python3 installed, preferable 3.11.

## Install with pip

You can install using pip by issuing the following commands in a terminal window:

```
pip install pymodbus
```

If you want to use the serial interface:

pip install pymodbus[serial]

<!-- image -->

<!-- image -->

This will install pymodbus with the pyserial dependency.

Pymodbus offers a number of extra options:

- repl , needed by pymodbus.repl
- serial , needed for serial communication
- simulator , needed by pymodbus.simulator
- documentation , needed to generate documentation
- development , needed for development
- all , installs all of the above

which can be installed as:

```
pip install pymodbus[<option>,...]
```

It is possible to install old releases if needed:

```
pip install pymodbus==3.5.4
```

## Install with github

On github, fork https:/ /github.com/pymodbus-dev/pymodbus.git

Clone the source, and make a virtual environment:

```
git clone git://github.com/<your account>/pymodbus.git
```

```
cd pymodbus python3 -m venv .venv
```

Activate the virtual environment, this command needs repeated in every new terminal:

```
source .venv/bin/activate
```

To get a specific release:

```
git checkout v3.5.2
```

<!-- image -->

v3.11.0

<!-- image -->

or the bleeding edge:

```
git checkout dev
```

Some distributions have an old pip, which needs to be upgraded:

```
pip install -upgrade pip
```

Install required development tools:

```
pip install ".[development]"
```

Install all (allows creation of documentation etc):

```
pip install '.[all]'
```

Install git hooks, that helps control the commit and avoid errors when submitting a Pull Request:

```
cp githooks/* .git/hooks
```

This installs dependencies in your virtual environment with pointers directly to the pymodbus directory, so any change you make is immediately available as if installed.

The repository contains a number of important branches and tags.

- dev is where all development happens, this branch is not always stable.
- master is where are releases are kept.
- vX.Y.Z (e.g. v2.5.3) is a specific release

## Example Code

For those of you who just want to get started quickly, here you go:

```
from pymodbus.client import ModbusTcpClient client = ModbusTcpClient('MyDevice.lan') client.connect() client.write_coil(1, True ) result = client.read_coils(1,1) print(result.bits[0]) client.close() v3.11.0
```

We provide a couple of simple ready to go clients:

- async client
- sync client

For more advanced examples, check out Examples included in the repository. If you have created any utilities that meet a specific need, feel free to submit them so others can benefit.

Also, if you have a question, please create a post in discussions q&amp;a topic, so that others can benefit from the results.

If you think, that something in the code is broken/not running well, please open an issue, read the Template-text first and then post your issue with your setup information.

## Example documentation

## Contributing

Just fork the repo and raise your Pull Request against dev branch.

<!-- image -->

We always have more work than time, so feel free to open a discussion / issue on a theme you want to solve.

If your company would like your device tested or have a cloud based device simulation, feel free to contact us. We are happy to help your company solve your modbus challenges.

That said, the current work mainly involves polishing the library and solving issues:

- Fixing bugs/feature requests
- Architecture documentation
- Functional testing against any reference we can find

There are 2 bigger projects ongoing:

- rewriting the internal part of all clients (both sync and async)
- Add features to the simulator, and enhance the web design

## Development instructions

The current code base is compatible with python &gt;= 3.10.

Here are some of the common commands to perform a range of activities:

<!-- image -->

<!-- image -->

```
source .venv/bin/activate   <-- Activate the virtual environment ./check_ci.sh               <-- run the same checks as CI runs on a pull request.
```

## Make a pull request:

```
git checkout dev          <-- activate development branch git pull                  <-- update branch with newest changes git checkout -b feature   <-- make new branch for pull request ... make source changes git commit                <-- commit change to git git push                  <-- push to your account on github on github open a pull request, check that CI turns green and then wait for review comments.
```

Test your changes:

```
cd test pytest
```

you can also do extended testing:

```
pytest --cov         <-- Coverage html report in build/html pytest --profile     <-- Call profile report in prof
```

## Internals

There is no documentation of the architecture (help is welcome), but most classes and methods are documented:

Pymodbus internals

## Generate documentation

Remark Assumes that you have installed documentation tools:;

pip install '.[documentation]'

to build do:

v3.11.0

<!-- image -->

The documentation is available in &lt;root&gt;/build/html

Remark: this generates a new zip/tgz file of examples which are uploaded.

## License Information

Released under the BSD License

<!-- image -->