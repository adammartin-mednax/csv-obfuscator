__version__ = '0.1.0'


def process_csv(csv_input_stream, csv_output_stream, colums_to_obfuscate, strategy):
    for row in csv_input_stream:
        current_column_index = 0
        new_row = []
        for column in row:
            if current_column_index in colums_to_obfuscate:
                column = strategy(column)
            current_column_index += 1
            new_row.append(column)
        csv_output_stream.writerow(new_row)
