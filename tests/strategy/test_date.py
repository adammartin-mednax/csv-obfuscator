import datetime
from csv_obfuscator.strategy.date import PyDate


EXPECTED_CONFIGURATION = """    - date: This strategy is intended to obfuscate date
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


def isdate(strdate, format):
    try:
        datetime.datetime.strptime(strdate, format).date()
        return True
    except ValueError:
        return False


def test_will_return_a_date():
    format = '%m/%d/%Y'
    strategy = PyDate({'strategy': 'date', 'format': format, 'direction': 'add', 'max': 100})
    assert isdate(strategy.obfuscate('1/1/2021'), format)


def test_will_return_a_random_date_in_expected_range_for_add():
    format = '%m/%d/%Y'
    max_value = 100
    date_time = datetime.date(2021, 1, 1)
    strategy = PyDate({'strategy': 'date', 'format': format, 'direction': 'add', 'max': max_value})
    for i in range(1000):
        new_date = strategy.obfuscate(date_time.strftime(format))
        new_datetime = datetime.datetime.strptime(new_date, format).date()
        assert new_datetime > date_time
        assert new_datetime <= date_time + datetime.timedelta(days=max_value)


def test_will_return_a_random_date_in_expected_range_for_subtract():
    format = '%m/%d/%Y'
    max_value = 100
    date_time = datetime.date(2021, 1, 1)
    strategy = PyDate({'strategy': 'date', 'format': format, 'direction': 'subtract', 'max': max_value})
    for i in range(1000):
        new_date = strategy.obfuscate(date_time.strftime(format))
        new_datetime = datetime.datetime.strptime(new_date, format).date()
        assert new_datetime < date_time
        assert new_datetime >= date_time - datetime.timedelta(days=max_value)


def test_will_return_empty_string_for_empty_string():
    strategy = PyDate({'strategy': 'date', 'format': '%m/%d/%Y', 'direction': 'subtract', 'max': 10})
    assert strategy.obfuscate('') == ''


def test_will_return_empty_string_for_nil_string():
    strategy = PyDate({'strategy': 'date', 'format': '%m/%d/%Y', 'direction': 'subtract', 'max': 10})
    assert strategy.obfuscate(None) == None


def test_will_return_empty_string_for_blank_string():
    strategy = PyDate({'strategy': 'date', 'format': '%m/%d/%Y', 'direction': 'subtract', 'max': 10})
    assert strategy.obfuscate('     ') == '     '


def test_will_explain_date_configuration():
    assert PyDate.configuration() == EXPECTED_CONFIGURATION
