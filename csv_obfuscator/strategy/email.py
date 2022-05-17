import time
from faker import Faker


__EMAIL_CONFIGURATION__ = """    - email: This strategy is intended to obfuscate email columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"email\"}
"""


class EMail:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._fake = Faker()

    def obfuscate(self, value):
        Faker.seed(value + str(time.time_ns()))
        return self._fake.ascii_safe_email()

    @classmethod
    def configuration(cls):
        return __EMAIL_CONFIGURATION__
