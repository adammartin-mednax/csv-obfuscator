import re
from csv_obfuscator.strategy.phone_number import PhoneNumber


def test_will_return_a_random_ssn():
    strategy = PhoneNumber({'strategy': 'phone_number'})
    result = strategy.obfuscate('Any_Phone_Number')
    pattern = re.compile(r'^\d\d\d\d\d\d\d\d\d\d$')
    assert bool(re.match(pattern, result))


def test_will_not_always_return_same_ssn():
    strategy = PhoneNumber({'strategy': 'phone_number'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('Any_Phone_Numbery_SSN')] = index
    assert len(results.keys()) > 1
