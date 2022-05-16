import re
from csv_obfuscator.strategy.social_security import SSN

def test_will_return_a_random_ssn():
    strategy = SSN({'strategy': 'social_security'})
    result = strategy.obfuscate('Any_SSN')
    pattern = re.compile(r'^\d\d\d-\d\d-\d\d\d\d$')
    assert bool(re.match(pattern, result))

def test_will_not_always_return_same_ssn():
    strategy = SSN({'strategy': 'social_security'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('Any_SSN')] = index
    assert len(results.keys()) > 1
