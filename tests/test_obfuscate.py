import csv
from io import StringIO
from unittest.mock import Mock, call
from csv_obfuscator import obfuscate


row1 = 'value1,value2,value3'
row2 = 'value4,value5,value6'
modifier = '_hashed'


class FakeStrategy:

    def obfuscate(self, value):
        return value+modifier


def reader(data_list):
    fake_file_io = StringIO('\n'.join(data_list))
    return csv.reader(fake_file_io, delimiter=',')


def test_will_call_strategy_with_designated_column():
    strategy = Mock()
    strategies = { 0: strategy }
    obfuscate(reader([row1]), Mock(), strategies)
    strategy.obfuscate.assert_called_once_with('value1')


def test_will_call_strategy_with_multiple_columns():
    strategy1 = Mock()
    strategy2 = Mock()
    strategies = { 0: strategy1, 2: strategy2 }
    obfuscate(reader([row1]), Mock(), strategies)
    strategy1.obfuscate.assert_called_once_with('value1')
    strategy2.obfuscate.assert_called_once_with('value3')


def test_will_return_results_of_strategy():
    csv_output_stream = Mock()
    fake_strategy = FakeStrategy()
    strategies = { 0: fake_strategy, 2: fake_strategy }
    expected_result = [fake_strategy.obfuscate('value1'), 'value2', fake_strategy.obfuscate('value3')]
    obfuscate(reader([row1]), csv_output_stream, strategies)
    csv_output_stream.writerow.assert_called_once_with(expected_result)


def test_will_return_results_of_strategy():
    csv_output_stream = Mock()
    fake_strategy = FakeStrategy()
    strategies = { 0: fake_strategy, 2: fake_strategy }
    expected_result1 = [fake_strategy.obfuscate('value1'), 'value2', fake_strategy.obfuscate('value3')]
    expected_result2 = [fake_strategy.obfuscate('value4'), 'value5', fake_strategy.obfuscate('value6')]
    obfuscate(reader([row1, row2]), csv_output_stream, strategies)
    csv_output_stream.writerow.assert_has_calls([call(expected_result1), call(expected_result2)])
