import csv
from io import StringIO
from unittest.mock import patch
from csv_obfuscator import process
from csv_obfuscator.strategy import md5


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


class FakeObfuscate():
    def __init__(self):
        self.strategies = None

    def obfuscate(self, csv_reader, csv_writer, strategies):
        csv_writer.writerow(next(csv_reader))
        self.strategies = strategies


@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
def test_process_will_create_a_csv_reader(mock_reader, mock_writer, mock_obfuscate):
    input_stream = StringIO()
    expected_delimiter = '|'
    config = ConfigBuilder().with_delimiter(expected_delimiter).config()
    process(config, input_stream, StringIO())
    mock_reader.assert_called_once_with(input_stream, delimiter=expected_delimiter)


@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
def test_process_will_create_a_csv_writer(mock_reader, mock_writer, mock_obfuscate):
    output_stream = StringIO()
    expected_delimiter = '|'
    config = ConfigBuilder().with_delimiter(expected_delimiter).config()
    process(config, StringIO(), output_stream)
    mock_writer.assert_called_once_with(output_stream, delimiter=expected_delimiter)


@patch('csv_obfuscator.obfuscate')
def test_process_will_write_header_line(mock_obfuscate):
    header = 'f_name, l_name'
    line1 = 'john, jones'
    input_stream = StringIO('\n'.join([header, line1]))
    output_stream = StringIO()
    process(ConfigBuilder().config(), input_stream, output_stream)
    assert output_stream.getvalue() == (header +'\r\n')


@patch('csv_obfuscator.obfuscate')
def test_process_will_delegate_to_obfuscate_and_pass_required_arguments(mock_obfuscate):
    fake = FakeObfuscate()
    mock_obfuscate.side_effect = fake.obfuscate
    header = 'garbage_in'
    line1 = 'garbage_out'
    output_stream = StringIO()
    position = 1
    strategy_arguments = {'strategy': 'md5'}
    config = ConfigBuilder().with_column_to_obfuscate(str(position), strategy_arguments).config()
    process(config, StringIO('\n'.join([header, line1])), output_stream)
    assert type(fake.strategies[1]) == md5.MD5
    assert output_stream.getvalue() == '\r\n'.join([header, line1,''])
