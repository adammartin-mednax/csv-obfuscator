from csv_obfuscator.strategy.integer import Integer


EXPECTED_CONFIGURATION = """    - integer: This strategy is intended to obfuscate columns like
      year or day or any other integer. In the strategy section of the configuration you need the following:
          - strategy: integer
          - max: An integer representing the maximum random value
          - min: An integer representing the minimum random value
      Example Config:
          {\"strategy\": \"integer\", \"max\": 30, \"min\": 1}
"""


def test_will_return_an_integer():
    strategy = Integer({'strategy': 'integer', "max": 100, "min": 1})
    assert isinstance(strategy.obfuscate('Any_Int'), int)


def test_will_return_an_integer_less_than_max_limit():
    max_value = 10
    strategy = Integer({'strategy': 'integer', "max": max_value, "min": 1})
    for i in range(1000):
        assert strategy.obfuscate('Any_Int') <= max_value


def test_will_return_an_integer_greater_than_min_limit():
    min_value = 1000
    strategy = Integer({'strategy': 'integer', "max": 10000, "min": min_value})
    for i in range(1000):
        assert strategy.obfuscate('Any_Int') >= min_value


def test_will_explain_integer_configuration():
    assert Integer.configuration() == EXPECTED_CONFIGURATION
