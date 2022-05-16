import time
from faker import Faker


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
