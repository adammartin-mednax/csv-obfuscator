import time
from faker import Faker


__SOCIAL_SECURITY_CONFIGURATION__ = """    - social_security: This strategy is intended to obfuscate social security columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"social_security\"}
"""


class SSN:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        return self._fake.ssn()

    @classmethod
    def configuration(cls):
        return __SOCIAL_SECURITY_CONFIGURATION__
