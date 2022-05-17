import csv
from io import StringIO
from unittest.mock import patch, mock_open, call
from csv_obfuscator import load


file_stream = 'blah'


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


@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.process')
@patch('csv_obfuscator.load_config', return_value=ConfigBuilder().with_input_file('input').with_output_file('output').config())
def test_load_will_open_file_to_write_to_and_read_from(mock_config, mock_process, mock_file):
    load()
    mock_file.assert_has_calls([call('output', mode='w', newline=''), call('input')], any_order=True)


@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.process')
@patch('csv_obfuscator.load_config', return_value=ConfigBuilder().with_input_file('input').with_output_file('output').config())
def test_load_will_delegate_to_process_function(mock_config, mock_process, mock_file):
    expected_input_stream = open('input')
    expected_output_stream = open('output', mode='w')
    load()
    mock_process.assert_called_once_with(mock_config.return_value, expected_input_stream, expected_output_stream)
