import hashlib


class MD5:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']

    def obfuscate(self, value):
        m = hashlib.new(self._strategy_type, usedforsecurity=False)
        m.update(value.encode('utf-8'))
        return m.hexdigest()
