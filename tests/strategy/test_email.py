import re
from csv_obfuscator.strategy.email import EMail


EXPECTED_CONFIGURATION = """    - email: This strategy is intended to obfuscate email columns.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"email\"}
"""


def test_will_return_a_different_email():
    original_email='Any_e_mail'
    strategy = EMail({'strategy': 'email'})
    assert strategy.obfuscate(original_email) != original_email


def test_will_return_a_random_email():
    strategy = EMail({'strategy': 'email'})
    result = strategy.obfuscate('Any_e_mail')
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    assert re.fullmatch(pattern, result)


def test_will_not_always_return_same_email():
    strategy = EMail({'strategy': 'email'})
    results = {}
    for index in range(100):
        results[strategy.obfuscate('Any_email')] = index
    assert len(results.keys()) > 1


def test_will_explain_email_configuration():
    assert EMail.configuration() == EXPECTED_CONFIGURATION
