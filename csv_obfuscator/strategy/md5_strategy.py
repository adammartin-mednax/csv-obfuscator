import hashlib


def obfuscate(value):
    m = hashlib.new('md5', usedforsecurity=False)
    m.update(value)
    return m.hexdigest()
