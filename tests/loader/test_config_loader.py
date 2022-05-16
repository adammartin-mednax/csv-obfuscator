import json
from unittest.mock import patch, mock_open, call
from csv_obfuscator.loader import load_config


expected_config = {
  'input_file': 'path_to/file.csv',
  'columns_to_obfuscate': {
    '0': {'strategy': 'strategy_type'},
  }
}
fake_stream = json.dumps(expected_config, indent=2)


@patch('builtins.open', new_callable=mock_open, read_data=fake_stream)
def test_will_return_configuration_as_hash(mock_open):
    assert expected_config == load_config()
