import time
from faker import Faker


class SSN:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        return self._fake.ssn()
