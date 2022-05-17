import re
from csv_obfuscator.strategy.phone_number import PhoneNumber


EXPECTED_CONFIGURATION = """    - phone_number: This strategy is intended to obfuscate phone number columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"phone_number\"}
"""


def test_will_return_a_random_phone_number():
    strategy = PhoneNumber({'strategy': 'phone_number'})
    result = strategy.obfuscate('Any_Phone_Number')
    pattern = re.compile(r'^\d\d\d\d\d\d\d\d\d\d$')
    assert bool(re.match(pattern, result))


def test_will_not_always_return_same_phone_number():
    strategy = PhoneNumber({'strategy': 'phone_number'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('Any_Phone_Number')] = index
    assert len(results.keys()) > 1


def test_will_explain_phone_number_configuration():
    assert PhoneNumber.configuration() == EXPECTED_CONFIGURATION
