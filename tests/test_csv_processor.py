import csv
from io import StringIO
from unittest.mock import Mock, call
from csv_obfuscator import csv_processor


row1 = 'value1,value2,value3'
row2 = 'value4,value5,value6'

def reader(data_list):
    fake_file_io = StringIO('\n'.join(data_list))
    return csv.reader(fake_file_io, delimiter=',')

def test_will_call_strategy_with_designated_column():
    strategy = Mock()
    csv_input_stream = reader([row1])
    csv_output_stream = None
    colums_to_obfuscate = [0]
    csv_processor(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy)
    strategy.assert_called_once_with('value1')

def test_will_call_strategy_with_multiple_columns():
    strategy = Mock()
    csv_input_stream = reader([row1])
    csv_output_stream = None
    colums_to_obfuscate = [0, 2]
    csv_processor(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy)
    strategy.assert_has_calls([call('value1'), call('value3')])
