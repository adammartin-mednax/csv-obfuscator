from .md5 import MD5


__STRATEGIES__ = {
    'md5': MD5
}


def build(config):
    strategies = {}
    for key, value in config['columns_to_obfuscate'].items():
        strategies[int(key)] = __STRATEGIES__[value['strategy']](value)
    return strategies
