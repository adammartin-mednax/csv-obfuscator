from .md5 import MD5
from .names import FirstName
from .names import LastName
from .social_security import SSN
from .phone_number import PhoneNumber


__STRATEGIES__ = {
    'md5': MD5,
    'first_name': FirstName,
    'last_name': LastName,
    'social_security': SSN,
    'phone_number': PhoneNumber
}


def build(config):
    strategies = {}
    for key, value in config['columns_to_obfuscate'].items():
        strategies[int(key)] = __STRATEGIES__[value['strategy']](value)
    return strategies
