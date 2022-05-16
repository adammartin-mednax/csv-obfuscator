import csv
import json
from .strategy import md5


__version__ = '0.1.0'


def process(columns_to_obfuscate):
    config = load_config()
    with open(config['output_file'], mode='w') as output_stream:
        with open(config['input_file']) as input_stream:
            csv_writer = csv.writer(output_stream, delimiter=config['delimiter'])
            csv_reader = csv.reader(input_stream, delimiter=config['delimiter'])
            csv_writer.writerow(next(csv_reader))
            obfuscate(csv_reader, csv_writer, columns_to_obfuscate, md5)


def obfuscate(csv_input_stream, csv_output_stream, columns_to_obfuscate, strategy):
    for row in csv_input_stream:
        new_row = [_new_value(value, index, columns_to_obfuscate, strategy) for index, value in enumerate(row)]
        csv_output_stream.writerow(new_row)


def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)


def _new_value(value, index, columns_to_obfuscate, strategy):
    if index in columns_to_obfuscate:
        return strategy.obfuscate(value)
    return value
