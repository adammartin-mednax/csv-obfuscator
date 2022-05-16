import re
from csv_obfuscator.strategy.md5_strategy import obfuscate

def test_will_hash_imput():
    value = 'example value'
    md5_regex_validation = re.compile(r'^[A-Fa-f0-9]{32}$', flags=re.M)
    assert len(md5_regex_validation.findall(obfuscate(value.encode('utf-8')))) == 1
