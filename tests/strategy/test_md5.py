import re
from csv_obfuscator.strategy.md5 import MD5


EXPECTED_CONFIGURATION = """    - md5: This strategy is intended to be a last resort tool.
      You can use this to convert any data into a garbage unreadable hash.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"md5\"}
"""


def test_will_hash_input():
    value = 'example value'
    strategy = MD5({'strategy': 'md5'})
    md5_regex_validation = re.compile(r'^[A-Fa-f0-9]{32}$', flags=re.M)
    assert len(md5_regex_validation.findall(strategy.obfuscate(value))) == 1


def test_will_explain_md5_configuration():
    assert MD5.configuration() == EXPECTED_CONFIGURATION
