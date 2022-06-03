import time
from faker import Faker


__INTEGER_CONFIGURATION__ = """    - integer: This strategy is intended to obfuscate columns like
      year or day or any other integer. In the strategy section of the configuration you need the following:
          - strategy: integer
          - max: An integer representing the maximum random value
          - min: An integer representing the minimum random value
      Example Config:
          {\"strategy\": \"integer\", \"max\": 30, \"min\": 1}
"""


class Integer:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._max_value = arguments['max']
        self._min_value = arguments['min']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        return self._fake.pyint(max_value=self._max_value, min_value=self._min_value)

    @classmethod
    def configuration(cls):
        return __INTEGER_CONFIGURATION__
