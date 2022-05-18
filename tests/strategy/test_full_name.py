from csv_obfuscator.strategy.names import __FIRST_NAMES__, __LAST_NAMES__, FullName


EXPECTED_CONFIGURATION = """    - full_name: This strategy is intended to obfuscate full name columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"full_name\"}
"""


def test_will_return_random_elven_full_name():
    strategy = FullName({'strategy': 'full_name'})
    first, last = strategy.obfuscate('Any_full_name').split()
    assert first in __FIRST_NAMES__
    assert last in __LAST_NAMES__


def test_will_not_always_return_same_elven_full_name():
    strategy = FullName({'strategy': 'full_name'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('some_name')] = index
    assert len(results.keys()) > 1


def test_will_explain_full_name_configuration():
    assert FullName.configuration() == EXPECTED_CONFIGURATION
