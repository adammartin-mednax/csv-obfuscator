from unittest.mock import patch
from csv_obfuscator.strategy.combination import Combination


class ConfigBuilder():
    def __init__(self):
        self._delimiter = '_'
        self._columns_to_obfuscate = {}

    def with_delimiter(self, delimiter):
        self._delimiter = delimiter
        return self

    def with_segment_to_obfuscate(self, column, strategy):
        self._columns_to_obfuscate[column] = strategy
        return self

    def config(self):
        config = {
            'strategy': 'combination',
            'delimiter': self._delimiter,
            'columns_to_obfuscate': self._columns_to_obfuscate
        }
        return config


EXPECTED_CONFIGURATION = """    - combination: This strategy is intended to handle columns
      composed of multiple data types.  In the strategy section of the configuration you need
      to define the column as if it contained another entire configuratuation as follows:
          {
            \"strategy\": \"combination\",
            \"delimiter\": \"_\",
            \"columns_to_obfuscate\": {
              \"0\": {\"strategy\": \"first_name\"},
              \"1\": {\"strategy\": \"last_name\"}
            }
          }
"""


@patch('csv_obfuscator.strategy.factory.build')
def test_will_rely_on_factory_to_determine_strategies(mock_build):
    config = ConfigBuilder().with_segment_to_obfuscate('0', {'strategy': 'first_name'}).with_segment_to_obfuscate('1', {'strategy': 'email'}).config()
    strategy = Combination(config)
    mock_build.assert_called_once_with(config)


def test_will_update_a_segement_that_is_configured():
    first_name = 'Joe'
    other_date = 'OtherData'
    config = ConfigBuilder().with_segment_to_obfuscate('0', {'strategy': 'first_name'}).config()
    result = Combination(config).obfuscate(f'{first_name}_{other_date}').split('_')
    assert result[0] != first_name


def test_will_not_update_a_segement_that_is_not_configured():
    first_name = 'Joe'
    other_date = 'OtherData'
    config = ConfigBuilder().with_segment_to_obfuscate('0', {'strategy': 'first_name'}).config()
    result = Combination(config).obfuscate(f'{first_name}_{other_date}').split('_')
    assert result[1] == other_date


def test_will_explain_combination_configuration():
    assert Combination.configuration() == EXPECTED_CONFIGURATION
