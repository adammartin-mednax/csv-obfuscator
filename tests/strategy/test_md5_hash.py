import re
from csv_obfuscator.strategy.md5 import MD5, obfuscate

def test_will_hash_imput():
    value = 'example value'
    md5_regex_validation = re.compile(r'^[A-Fa-f0-9]{32}$', flags=re.M)
    assert len(md5_regex_validation.findall(obfuscate(value))) == 1


def test_will_hash_input():
    value = 'example value'
    strategy = MD5({'strategy': 'md5'})
    md5_regex_validation = re.compile(r'^[A-Fa-f0-9]{32}$', flags=re.M)
    assert len(md5_regex_validation.findall(strategy.obfuscate(value))) == 1
