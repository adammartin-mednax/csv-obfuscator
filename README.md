# CSV Obfuscation Tool

This project is an extension of the great work of Fabio Domingues [CSV Obfuscation](https://github.com/fabiodomingues/csv-obfuscation).

I needed a version to be far more rich in how it handles data types and fulfills obfuscating data in a way that makes it useable in test environments.

This project is intended to build a usable obfuscator tool on multiple OS platforms.  It needs to be configurable to handle a variable set of data types and CSVs.

#Requirements

This tool and project requires [Docker](https://www.docker.com) to be useful.

#Usage

When using the tool you should receive an text output to guide you on how to configure it.

## Directly from project

```
poetry run python obfuscate.py

<USAGE WILL PRINT HERE>
```

## Windows platform

```
build_obfuscate.bat
run_obfuscate.bat

<This should start a docker container with the current directory mounted as the working directory.>

obfuscate
<USAGE WILL PRINT HERE>
```

## Mac Platform

```
make build-docker
docker run -it -v $pwd:/current_directory -w /current_directory csv_obfuscator_linux bash

<This should start a docker container with the current directory mounted as the working directory.>

obfuscate

<USAGE WILL PRINT HERE>
```

# Development

## Prerequisites

* Python Environment with [Poetry](https://python-poetry.org/)
* make

### Building

This project has all build steps defined in the Makefile.

Please refer to it for all supported build steps like:

* **clean**: Clean the project removing build, distribution, and pycache directories
* **initialize**: Install dependencies defined by poetry
* **analyze**: Analyzes the project using Flake8 and pylint.
* **quick-test**: Just run the tests
* **unit-test**: Analyze and unit test
* **build-docker**: Build the docker container the tool runs in.
* **build**/**all**: build it all!
