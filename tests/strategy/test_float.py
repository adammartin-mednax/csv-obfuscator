from csv_obfuscator.strategy.float import PyFloat


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def test_will_return_a_float():
    strategy = PyFloat({'strategy': 'float', "max": 10000, "min": 1000, "decimals": 2})
    assert isfloat(strategy.obfuscate('Any_Float'))


def test_will_return_a_float_less_than_max_limit():
    max_value = 10
    strategy = PyFloat({'strategy': 'float', "max": max_value, "min": 1, "decimals": 2})
    for i in range(1000):
        assert strategy.obfuscate('Any_Float') <= max_value


def test_will_return_a_float_greater_than_min_limit():
    min_value = 1000
    strategy = PyFloat({'strategy': 'float', "max": 10000, "min": min_value, "decimals": 2})
    for i in range(1000):
        assert strategy.obfuscate('Any_Float') >= min_value


def test_will_return_a_float_with_right_number_of_decimals():
    decimals = 2
    strategy = PyFloat({'strategy': 'float', "max": 10000, "min": 1, "decimals": decimals})
    for i in range(1000):
        assert len(str(strategy.obfuscate('Any_Float')).split('.')[1]) <= decimals
