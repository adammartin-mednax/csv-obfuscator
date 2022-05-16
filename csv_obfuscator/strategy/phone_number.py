import time
from faker import Faker


class PhoneNumber:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        result = self._fake.msisdn()[3:]
        if result.startswith('0'):
            result = result.replace('0', '1', 1)
        return result
