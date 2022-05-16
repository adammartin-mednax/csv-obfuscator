__version__ = '0.1.0'


def csv_processor(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy):
    for row in csv_input_stream:
        current_column_index = 0
        for column in row:
            if current_column_index in colums_to_obfuscate:
                strategy(column)
            current_column_index += 1
