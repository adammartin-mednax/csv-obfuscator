def new_value(value, index, strategies):
    if index in strategies:
        return strategies[index].obfuscate(value)
    return value
