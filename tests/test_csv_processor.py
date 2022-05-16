import csv
from io import StringIO
from unittest.mock import patch, mock_open, call
from csv_obfuscator import process
from csv_obfuscator.strategy import md5_strategy


file_stream = 'blah'


@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
def test_process_will_open_file_to_write_to_and_read_from(mock_reader, mock_writer, mock_obfuscate, mock_file):
    csv_input_file = 'input'
    csv_output_file = 'output'
    process(csv_input_file, csv_output_file, ',', [1, 7, 9])
    mock_file.assert_has_calls([call(csv_output_file, mode='w'), call(csv_input_file)], any_order=True)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
def test_process_will_create_a_csv_writer(mock_reader, mock_writer, mock_obfuscate, mock_file):
    delimiter = ','
    process('input', 'output', delimiter, [1, 7, 9])
    mock_writer.assert_called_once_with(mock_file.return_value, delimiter=delimiter)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
def test_process_will_create_a_csv_reader(mock_reader, mock_writer, mock_obfuscate, mock_file):
    delimiter = ','
    process('input', 'output', delimiter, [1, 7, 9])
    mock_reader.assert_called_once_with(mock_file.return_value, delimiter=delimiter)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
def test_process_will_pass_the_data_to_the_strategy_to_be_obfuscated(mock_reader, mock_writer, mock_obfuscate, mock_file):
    columns_to_obfuscate = [1, 7, 9]
    process('input', 'output', ',', columns_to_obfuscate)
    mock_obfuscate.assert_called_once_with(mock_reader.return_value,
                                           mock_writer.return_value,
                                           columns_to_obfuscate,
                                           md5_strategy)


@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
@patch('csv_obfuscator.next') # this is really a builtin function but this mocks it at an easier point
def test_process_will_skip_header_line(mock_next, mock_reader, mock_writer, mock_obfuscate, mock_file):
    process('input', 'output', ',', [1, 7, 9])
    mock_next.assert_called_once_with(mock_reader.return_value)


@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.obfuscate')
@patch('csv.writer')
@patch('csv.reader')
@patch('csv_obfuscator.next') # this is really a builtin function but this mocks it at an easier point
def test_process_will_write_header_line(mock_next, mock_reader, mock_writer, mock_obfuscate, mock_file):
    process('input', 'output', ',', [1, 7, 9])
    mock_writer.return_value.writerow.assert_called_once_with(mock_next.return_value)
