from csv_obfuscator.strategy.names import FirstName, __FIRST_NAMES__

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
