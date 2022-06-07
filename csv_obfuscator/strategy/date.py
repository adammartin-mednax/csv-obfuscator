import time
import datetime
from faker import Faker


__DATE_CONFIGURATION__ = """    - date: This strategy is intended to obfuscate date
      columns. In the strategy section of the configuration you need the following:
          - strategy: date
          - format: The string format as defined https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
             As an example \"%m/%d/%Y\" will translate dates like \"01/01/2020\" or \"1/1/2020\"
          - direction: This tells which direction to randomly increase or decrease the
             date by.  Valid values:
             - subtract: subtracts a random number of days from the date.  This is good for start dates so
                they never occur after end dates.
             - add: add a random number of days to the date.  This is good for end dates so
                they never occur before start dates.
          - max: The maximum number of days to add or subtract
      Example Config:
          {\"strategy\": \"date\", \"format\": \"%m/%d/%Y\", \"direction\": \"add\", \"max\": 100}
"""


class PyDate:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']
        self._format = arguments['format']
        self._direction = arguments['direction']
        self._max_value = arguments['max']
        self._fake = Faker()

    def obfuscate(self, value):
        if value and not value.isspace():
            result = self._new_date(value)
            return datetime.datetime.strftime(result, self._format)
        return value

    def _new_date(self, value):
        Faker.seed(value + str(time.time_ns()))
        curr_date = datetime.datetime.strptime(value, self._format).date()
        days = self._fake.pyint(max_value=self._max_value, min_value=1)
        if self._direction == 'add':
            return curr_date + datetime.timedelta(days=days)
        return curr_date - datetime.timedelta(days=days)

    @classmethod
    def configuration(cls):
        return __DATE_CONFIGURATION__
