import csv
from io import StringIO
from unittest.mock import patch, mock_open, call
from csv_obfuscator import load, process
from csv_obfuscator.strategy import md5


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

    def with_column_to_obfuscate(self, column_configuration):
        self._columns_to_obfuscate.add(column_configuration)
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
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
@patch('csv_obfuscator.load_config', return_value=ConfigBuilder().with_input_file('input').with_output_file('output').config())
def test_process_will_open_file_to_write_to_and_read_from(mock_load_config, mock_reader, mock_writer, mock_obfuscate, mock_file):
    load([1, 7, 9])
    mock_file.assert_has_calls([call('output', mode='w'), call('input')], any_order=True)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
@patch('csv_obfuscator.load_config', return_value=ConfigBuilder().with_delimiter('|').config())
def test_process_will_create_a_csv_writer(mock_load_config, mock_reader, mock_writer, mock_obfuscate, mock_file):
    load([1, 7, 9])
    mock_writer.assert_called_once_with(mock_file.return_value, delimiter='|')

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
@patch('csv_obfuscator.load_config', return_value=ConfigBuilder().with_delimiter(',').config())
def test_process_will_create_a_csv_reader(mock_load_config, mock_reader, mock_writer, mock_obfuscate, mock_file):
    load([1, 7, 9])
    mock_reader.assert_called_once_with(mock_file.return_value, delimiter=',')


@patch('csv_obfuscator.obfuscate')
def test_process_will_write_header_line(mock_obfuscate):
    header = 'f_name, l_name'
    line1 = 'john, jones'
    input_stream = StringIO('\n'.join([header, line1]))
    output_stream = StringIO()
    process(ConfigBuilder().config(), input_stream, output_stream, [1, 2])
    assert output_stream.getvalue() == (header +'\r\n')


class FakeObfuscate():
    def __init__(self):
        self.columns_to_obfuscate = None
        self.strategy = None

    def obfuscate(self, reader, writer, columns_to_obfuscate, strategy):
        print('******* IN OBSFUCATE ********')
        writer.writerow(next(reader))
        self.columns_to_obfuscate = columns_to_obfuscate
        self.strategy = strategy



@patch('csv_obfuscator.obfuscate')
def test_process_will_pass_the_input_stream_to_be_obfuscated(mock_obfuscate):
    fake = FakeObfuscate()
    mock_obfuscate.side_effect = fake.obfuscate
    header = 'garbage_in'
    line1 = 'garbage_out'
    output_stream = StringIO()
    columns_to_obfuscate = [1, 7, 9]
    process(ConfigBuilder().config(), StringIO('\n'.join([header, line1])), output_stream, columns_to_obfuscate)
    assert fake.columns_to_obfuscate == columns_to_obfuscate
    assert fake.strategy == md5
    assert output_stream.getvalue() == '\r\n'.join([header, line1,''])
