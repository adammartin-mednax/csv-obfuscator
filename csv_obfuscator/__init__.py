import csv
from .strategy import md5_strategy


__version__ = '0.1.0'


def obfuscate(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy):
    for row in csv_input_stream:
        current_column_index = 0
        new_row = []
        for column in row:
            if current_column_index in colums_to_obfuscate:
                column = strategy(column)
            current_column_index += 1
            new_row.append(column)
        csv_output_stream.writerow(new_row)


def orchestrator(csv_input_file, csv_output_file, delimiter, columns_to_obfuscate):
    with open(csv_output_file, mode='w') as output:
        with open(csv_input_file) as csv_input:
            csv_output = csv.writer(output, delimiter=delimiter)
            csv_reader = csv.reader(csv_input, delimiter=delimiter)
            obfuscate(csv_reader, csv_output, columns_to_obfuscate, md5_strategy)
