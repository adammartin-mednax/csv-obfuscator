from .md5 import MD5
from .names import FirstName
from .names import LastName


__STRATEGIES__ = {
    'md5': MD5,
    'first_name': FirstName,
    'last_name': LastName
}


def build(config):
    strategies = {}
    for key, value in config['columns_to_obfuscate'].items():
        strategies[int(key)] = __STRATEGIES__[value['strategy']](value)
    return strategies
