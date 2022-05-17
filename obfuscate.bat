set PATH=%CD%\winpython\python-3.10.4\;%PATH%
"%~dp0winpython\python-3.10.4\scipts\pip3.exe" install Faker==13.11.1
"%~dp0winpython\python-3.10.4\python.exe" "%~dp0obfuscate.py"
