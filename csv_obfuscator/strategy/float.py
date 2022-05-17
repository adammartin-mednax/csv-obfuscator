import time
from faker import Faker


__FLOAT_CONFIGURATION__ = """    - float: This strategy is intended to obfuscate columns like
      money. In the strategy section of the configuration you need the following:
          - strategy: float
          - max: An integer representing the maximum random value
          - min: An integer representing the minimum random value
          - decimals: The maximum number of decimals to include. Values will
            print as numbers so they will render as 1000.1 not 1000.10.
      Example Config:
          {\"strategy\": \"float\", \"max\": 10000, \"min\": 1000, \"decimals\": 2}
"""


class PyFloat:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._max_value = arguments['max']
        self._min_value = arguments['min']
        self._decimals = arguments['decimals']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        return self._fake.pyfloat(max_value=self._max_value, min_value=self._min_value, right_digits=self._decimals)

    @classmethod
    def configuration(cls):
        return __FLOAT_CONFIGURATION__
