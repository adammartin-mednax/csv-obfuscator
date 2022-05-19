import time
from faker import Faker


__PERCENTAGE_CONFIGURATION__ = """    - percentage: This strategy is intended to obfuscate columns like
      bonus percentage. In the strategy section of the configuration you need the following:
          - strategy: float
          - max: An integer representing the maximum percentage random value ('20' means 20%)
          - min: An integer representing the minimum percentage random value ('1' means 1%)
          - decimals: The maximum number of decimals to include. Values will
            print as numbers so they will render as 10.1 not 10.10.
      Example Configs:
          {\"strategy\": \"percentage\", \"max\": 50, \"min\": 10, \"decimals\": 0}
          {\"strategy\": \"percentage\", \"max\": 40, \"min\": 10, \"decimals\": 2}
"""


class Percentage:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._max_value = arguments['max']
        self._min_value = arguments['min']
        self._decimals = arguments['decimals']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        if self._decimals == 0:
            return str(self._fake.pyint(max_value=self._max_value, min_value=self._min_value))
        return str(self._fake.pyfloat(max_value=self._max_value, min_value=self._min_value, right_digits=self._decimals))

    @classmethod
    def configuration(cls):
        return __PERCENTAGE_CONFIGURATION__
