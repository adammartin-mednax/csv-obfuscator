from unittest.mock import patch
from csv_obfuscator.strategy.md5 import MD5
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


def test_factory_will_contain_configured_strategy():
    result = factory.build(ConfigBuilder().with_column_to_obfuscate('1', {'strategy': 'md5'}).config())
    assert type(result[1]) == MD5


@patch('csv_obfuscator.strategy.factory.__STRATEGIES__')
def test_factory_will_pass_arguments_to_strategy_constructor(mock_strategy):
    strategy_arguments = {'strategy': 'md5'}
    result = factory.build(ConfigBuilder().with_column_to_obfuscate('1', strategy_arguments).config())
    mock_strategy.__getitem__().assert_called_once_with(strategy_arguments)
