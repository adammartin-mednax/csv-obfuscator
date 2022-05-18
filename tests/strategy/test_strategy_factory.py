from unittest.mock import patch
from csv_obfuscator.strategy.md5 import MD5
from csv_obfuscator.strategy.names import FirstName, LastName
from csv_obfuscator.strategy.social_security import SSN
from csv_obfuscator.strategy.phone_number import PhoneNumber
from csv_obfuscator.strategy.float import PyFloat
from csv_obfuscator.strategy.email import EMail
from csv_obfuscator.strategy.integer import Integer
from csv_obfuscator.strategy import factory


class ConfigBuilder():
    def __init__(self):
        self._input_file = 'default_input_file'
        self._output_file = 'default_output_file'
        self._delimiter = ','
        self._columns_to_obfuscate = {}

    def with_input_file(self, input_file):
        self._input_file = input_file
        return self

    def with_output_file(self, output_file):
        self._output_file = output_file
        return self

    def with_delimiter(self, delimiter):
        self._delimiter = delimiter
        return self

    def with_column_to_obfuscate(self, column, strategy):
        self._columns_to_obfuscate[column] = strategy
        return self

    def config(self):
        config = {
            'input_file': self._input_file,
            'output_file': self._output_file,
            'delimiter': self._delimiter,
            'columns_to_obfuscate': self._columns_to_obfuscate
        }
        return config


def test_factory_will_return_dict_of_strategies():
    result = factory.build(ConfigBuilder().config())
    assert type(result) == dict


def test_factory_will_return_configured_strategies():
    result = factory.build(ConfigBuilder().with_column_to_obfuscate('1', {'strategy': 'md5'})
                                          .with_column_to_obfuscate('2', {'strategy': 'first_name'})
                                          .with_column_to_obfuscate('3', {'strategy': 'last_name'})
                                          .with_column_to_obfuscate('4', {'strategy': 'social_security'})
                                          .with_column_to_obfuscate('5', {'strategy': 'phone_number'})
                                          .with_column_to_obfuscate('6', {'strategy': 'float', 'min': 1, 'max': 10, 'decimals': 2})
                                          .with_column_to_obfuscate('7', {'strategy': 'email'})
                                          .with_column_to_obfuscate('8', {'strategy': 'integer', 'min': 1, 'max': 10})
                                          .config())
    assert type(result[1]) == MD5
    assert type(result[2]) == FirstName
    assert type(result[3]) == LastName
    assert type(result[4]) == SSN
    assert type(result[5]) == PhoneNumber
    assert type(result[6]) == PyFloat
    assert type(result[7]) == EMail
    assert type(result[8]) == Integer


@patch('csv_obfuscator.strategy.factory.__STRATEGIES__')
def test_factory_will_pass_arguments_to_strategy_constructor(mock_strategy):
    strategy_arguments = {'strategy': 'md5'}
    result = factory.build(ConfigBuilder().with_column_to_obfuscate('1', strategy_arguments).config())
    mock_strategy.__getitem__().assert_called_once_with(strategy_arguments)


def test_factry_will_print_configuration_message():
    composed_message = factory.__CONFIGURATION_BASE_MESSAGE__
    for strategy in factory.__STRATEGIES__.values():
        composed_message += strategy.configuration()
    assert composed_message == factory.configuration()
