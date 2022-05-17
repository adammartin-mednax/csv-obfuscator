from csv_obfuscator.strategy.names import LastName, __LAST_NAMES__


EXPECTED_CONFIGURATION = """    - last_name: This strategy is intended to obfuscate last name columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"last_name\"}
"""


def test_will_return_random_elven_name():
    strategy = LastName({'strategy': 'last_name'})
    result = strategy.obfuscate('Any_Last_Name')
    assert result in __LAST_NAMES__


def test_will_not_always_return_same_elven_name():
    strategy = LastName({'strategy': 'larst_name'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('some_name')] = index
    assert len(results.keys()) > 1


def test_will_explain_last_name_configuration():
    strategy = LastName({'strategy': 'last_name'})
    assert strategy.configuration() == EXPECTED_CONFIGURATION
