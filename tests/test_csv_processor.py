import csv
from io import StringIO
from unittest.mock import patch, mock_open, call
from csv_obfuscator import orchestrator
from csv_obfuscator.strategy import md5_strategy


file_stream = 'blah'


@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.process_csv')
@patch('csv.writer')
@patch('csv.reader')
def test_orchestrator_will_open_file_to_write_to_and_read_from(mock_reader, mock_writer, mock_processor, mock_file):
    csv_input_file = 'input'
    csv_output_file = 'output'
    delimiter = ','
    columns_to_obfuscate = [1, 7, 9]
    orchestrator(csv_input_file, csv_output_file, delimiter, columns_to_obfuscate)
    mock_file.assert_has_calls([call(csv_output_file, mode='w'), call(csv_input_file)], any_order=True)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.process_csv')
@patch('csv.writer')
@patch('csv.reader')
def test_orchestrator_will_create_a_csv_writer(mock_reader, mock_writer, mock_processor, mock_file):
    csv_input_file = 'input'
    csv_output_file = 'output'
    delimiter = ','
    columns_to_obfuscate = [1, 7, 9]
    orchestrator(csv_input_file, csv_output_file, delimiter, columns_to_obfuscate)
    mock_writer.assert_called_once_with(mock_file.return_value, delimiter=delimiter)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.process_csv')
@patch('csv.writer')
@patch('csv.reader')
def test_orchestrator_will_create_a_csv_reader(mock_reader, mock_writer, mock_processor, mock_file):
    csv_input_file = 'input'
    csv_output_file = 'output'
    delimiter = ','
    columns_to_obfuscate = [1, 7, 9]
    orchestrator(csv_input_file, csv_output_file, delimiter, columns_to_obfuscate)
    mock_reader.assert_called_once_with(mock_file.return_value, delimiter=delimiter)

@patch('builtins.open', new_callable=mock_open, read_data=file_stream)
@patch('csv_obfuscator.process_csv')
@patch('csv.writer')
@patch('csv.reader')
def test_orchestrator_will_process_the_files(mock_reader, mock_writer, mock_processor, mock_file):
    csv_input_file = 'input'
    csv_output_file = 'output'
    delimiter = ','
    columns_to_obfuscate = [1, 7, 9]
    orchestrator(csv_input_file, csv_output_file, delimiter, columns_to_obfuscate)
    mock_processor.assert_called_once_with(mock_reader.return_value,
                                           mock_writer.return_value,
                                           columns_to_obfuscate,
                                           md5_strategy)
