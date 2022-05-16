import csv
from .strategy import md5_strategy


__version__ = '0.1.0'


def orchestrator(input_file_name, output_file_name, delimiter, columns_to_obfuscate):
    with open(output_file_name, mode='w') as output_stream:
        with open(input_file_name) as input_stream:
            csv_writer = csv.writer(output_stream, delimiter=delimiter)
            csv_reader = csv.reader(input_stream, delimiter=delimiter)
            obfuscate(csv_reader, csv_writer, columns_to_obfuscate, md5_strategy)


def obfuscate(csv_input_stream, csv_output_stream, columns_to_obfuscate, strategy):
    for row in csv_input_stream:
        new_row = [_new_value(value, index, columns_to_obfuscate, strategy) for index, value in enumerate(row)]
        csv_output_stream.writerow(new_row)


def _new_value(value, index, columns_to_obfuscate, strategy):
    if index in columns_to_obfuscate:
        return strategy(value)
    return value
