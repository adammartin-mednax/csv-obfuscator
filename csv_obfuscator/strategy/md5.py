import hashlib


__MD5_CONFIGURATION__ = """    - md5: This strategy is intended to be a last resort tool.
      You can use this to convert any data into a garbage unreadable hash.
      In the strategy section of the configuration you only need the following:
          {\"strategy\": \"md5\"}
"""


class MD5:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']

    def obfuscate(self, value):
        m = hashlib.new(self._strategy_type, usedforsecurity=False)
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def configuration(cls):
        return __MD5_CONFIGURATION__
