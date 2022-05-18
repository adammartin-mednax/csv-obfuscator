import re
from csv_obfuscator.strategy.percentage import Percentage


EXPECTED_CONFIGURATION = """    - percentage: This strategy is intended to obfuscate columns like
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


def is_percentage(result):
    pattern = re.compile('\\d+(?:\\.\\d+)?')
    return re.fullmatch(pattern, result)


def test_will_return_a_percentage():
    strategy = Percentage({'strategy': 'percentage', "max": 50, "min": 10, "decimals": 0})
    assert is_percentage(strategy.obfuscate('Any_percentage'))


def test_will_return_a_percentage_less_than_max_limit():
    max_value = 10
    strategy = Percentage({'strategy': 'percentage', "max": max_value, "min": 1, "decimals": 2})
    for i in range(1000):
        assert float(strategy.obfuscate('Any_percentage')) <= max_value


def test_will_return_a_percentage_greater_than_min_limit():
    min_value = 1000
    strategy = Percentage({'strategy': 'percentage', "max": 10000, "min": min_value, "decimals": 2})
    for i in range(1000):
        assert float(strategy.obfuscate('Any_percentage')) >= min_value


def test_will_return_a_percentage_with_right_number_of_decimals():
    decimals = 2
    strategy = Percentage({'strategy': 'percentage', "max": 10000, "min": 1, "decimals": decimals})
    for i in range(1000):
        assert len(strategy.obfuscate('Any_percentage').split('.')[1]) <= decimals


def test_will_return_a_percentage_with_can_handle_0_decimals():
    minimum = 1
    maximum = 50
    strategy = Percentage({'strategy': 'percentage', "max": maximum, "min": minimum, "decimals": 0})
    for i in range(1000):
        value = strategy.obfuscate('Any_percentage')
        print(value)
        assert is_percentage(value)
        assert minimum <= int(value) <= maximum


def test_will_explain_percentage_configuration():
    assert Percentage.configuration() == EXPECTED_CONFIGURATION
