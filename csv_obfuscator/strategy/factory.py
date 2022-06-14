from .md5 import MD5
from .names import FirstName
from .names import LastName
from .names import FullName
from .social_security import SSN
from .phone_number import PhoneNumber
from .float import PyFloat
from .integer import Integer
from .percentage import Percentage
from .date import PyDate
from .email import EMail
from .combination import Combination


__CONFIGURATION_BASE_MESSAGE__ = """CSV-OBFUSCATOR and CONFIG.JSON

    The csv-obfuscator is intended to obfuscate columns of a csv based on
    configuration that is supplied via a configuration file.  The configuration
    file is intended to be written in JSON format
    (https://en.wikipedia.org/wiki/JSON#Syntax).

    The file is expected to be named `config.json`.

    The config.json file is expected to contain the following elements:
        - input_file: The input file to obfuscate.

            \"input_file\": \"examples/simple.csv\"

        - output_file: The output file to write the obfuscated data to.

            \"output_file": "output.csv"

        - delimiter: The delimiter the file uses. Usually this is a \",\" but may
            be something other like \"|\".

            \"delimiter\": \",\"

        - columns_to_obfuscate: This is the segment where the columns to obfuscate
            are defined.  This is a list of columns, which are `0` indexed.  This
            means the first column in the csv is treated as `0`.  For each
            column position a strategy is defined for it.  That strategy will
            be applied to the individual column.  For example if we only wanted
            to obfuscate the first column that contains a social security number we
            would have a segment that looks like:

            \"columns_to_obfuscate\": {
              \"0\": {\"strategy\": \"social_security\"}
            }

    A full `config.json` file might look something like this:

        {
          \"input_file\": \"examples/simple.csv\",
          \"output_file\": \"output.csv\",
          \"delimiter\": \",\",
          \"columns_to_obfuscate\": {
            \"0\": {\"strategy\": \"first_name\"},
            \"1\": {\"strategy\": \"last_name\"},
            \"2\": {\"strategy\": \"social_security\"},
            \"5\": {\"strategy\": \"float\", \"max\": 10000, \"min\": 1000, \"decimals\": 2},
            \"6\": {\"strategy\": \"phone_number\"}
          }
        }

Individual Strategy Definitions
"""


__STRATEGIES__ = {
    'md5': MD5,
    'first_name': FirstName,
    'last_name': LastName,
    'full_name': FullName,
    'social_security': SSN,
    'phone_number': PhoneNumber,
    'integer': Integer,
    'float': PyFloat,
    'percentage': Percentage,
    'email': EMail,
    'date': PyDate,
    'combination': Combination
}


def build(config):
    strategies = {}
    for key, value in config['columns_to_obfuscate'].items():
        strategies[int(key)] = __STRATEGIES__[value['strategy']](value)
    return strategies


def configuration():
    composed_message = __CONFIGURATION_BASE_MESSAGE__
    for strategy in __STRATEGIES__.values():
        composed_message += strategy.configuration()
    return composed_message
