# pylint: disable=R0401
from . import factory
from ..utility import new_value


__COMBINATION_CONFIGURATION__ = """    - combination: This strategy is intended to handle columns
      composed of multiple data types.  In the strategy section of the configuration you need
      to define the column as if it contained another entire configuratuation as follows:
          {
            \"strategy\": \"combination\",
            \"delimiter\": \"_\",
            \"columns_to_obfuscate\": {
              \"0\": {\"strategy\": \"first_name\"},
              \"1\": {\"strategy\": \"last_name\"}
            }
          }
"""


class Combination:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._delimiter = arguments['delimiter']
        self._strategies = factory.build(arguments)

    def obfuscate(self, value):
        values = value.split(self._delimiter)
        new_values = [new_value(data, index, self._strategies) for index, data in enumerate(values)]
        return self._delimiter.join(new_values)

    @classmethod
    def configuration(cls):
        return __COMBINATION_CONFIGURATION__
