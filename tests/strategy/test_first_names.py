from csv_obfuscator.strategy.names import FirstName, __FIRST_NAMES__


EXPECTED_CONFIGURATION = """    - first_name: This strategy is intended to obfuscate first name columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"first_name\"}
"""


def test_will_return_random_elven_name():
    strategy = FirstName({'strategy': 'first_name'})
    result = strategy.obfuscate('Any_First_Name')
    assert result in __FIRST_NAMES__


def test_will_not_always_return_same_elven_name():
    strategy = FirstName({'strategy': 'first_name'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('some_name')] = index
    assert len(results.keys()) > 1


def test_will_explain_first_name_configuration():
    strategy = FirstName({'strategy': 'first_name'})
    assert strategy.configuration() == EXPECTED_CONFIGURATION
