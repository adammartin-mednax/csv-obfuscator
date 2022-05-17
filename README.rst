# CSV Obfuscation Tool

This project is an extension of the great work of Fabio Domingues [CSV Obfuscation](https://github.com/fabiodomingues/csv-obfuscation).

I needed a version to be far more rich in how it handles data types and fulfills obfuscating data in a way that makes it useable in test environments.

This project is intended to build a usable obfuscator tool on multiple OS platforms.  It needs to be configurable to handle a variable set of data types and CSVs.

#Usage

When using the tool you should receive an text output to guide you on how to configure it.

## Directly from project

```
poetry run python obfuscate.py

<USAGE WILL PRINT HERE>
```

## Windows platform

```
./obfuscate.bat

<USAGE WILL PRINT HERE>
```

## Mac Platform

```
./obfuscate

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
* **build-mac**: build on mac
* **build-win**: build on windows
* **build**/**all**: build it all!
