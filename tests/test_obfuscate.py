import csv
from io import StringIO
from unittest.mock import Mock, call
from csv_obfuscator import obfuscate


row1 = 'value1,value2,value3'
row2 = 'value4,value5,value6'
modifier = '_hashed'


class fake_strategy:

    @classmethod
    def obfuscate(self, value):
        return value+modifier


def reader(data_list):
    fake_file_io = StringIO('\n'.join(data_list))
    return csv.reader(fake_file_io, delimiter=',')


def test_will_call_strategy_with_designated_column():
    strategy = Mock()
    csv_input_stream = reader([row1])
    csv_output_stream = Mock()
    colums_to_obfuscate = [0]
    obfuscate(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy)
    strategy.obfuscate.assert_called_once_with('value1')


def test_will_call_strategy_with_multiple_columns():
    strategy = Mock()
    csv_input_stream = reader([row1])
    csv_output_stream = Mock()
    colums_to_obfuscate = [0, 2]
    obfuscate(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy)
    strategy.obfuscate.assert_has_calls([call('value1'), call('value3')])


def test_will_return_results_of_strategy():
    csv_input_stream = reader([row1])
    csv_output_stream = Mock()
    colums_to_obfuscate = [0, 2]
    expected_result = [fake_strategy.obfuscate('value1'), 'value2', fake_strategy.obfuscate('value3')]
    obfuscate(csv_input_stream, csv_output_stream, colums_to_obfuscate, fake_strategy)
    csv_output_stream.writerow.assert_called_once_with(expected_result)


def test_will_return_results_of_strategy():
    csv_input_stream = reader([row1, row2])
    csv_output_stream = Mock()
    colums_to_obfuscate = [0, 2]
    expected_result1 = [fake_strategy.obfuscate('value1'), 'value2', fake_strategy.obfuscate('value3')]
    expected_result2 = [fake_strategy.obfuscate('value4'), 'value5', fake_strategy.obfuscate('value6')]
    obfuscate(csv_input_stream, csv_output_stream, colums_to_obfuscate, fake_strategy)
    csv_output_stream.writerow.assert_has_calls([call(expected_result1), call(expected_result2)])
