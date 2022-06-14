import csv
import json
from json.decoder import JSONDecodeError
from .strategy import factory
from .utility import new_value


__version__ = '0.1.0'


def load():
    try:
        config = load_config()
        with open(config['output_file'], mode='w', newline='') as output_stream:
            with open(config['input_file']) as input_stream:
                process(config, input_stream, output_stream, )
    except (FileNotFoundError, JSONDecodeError, KeyError):
        print(factory.configuration())


def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)


def process(config, input_stream, output_stream):
    csv_reader = csv.reader(input_stream, delimiter=config['delimiter'])
    csv_writer = csv.writer(output_stream, delimiter=config['delimiter'])
    csv_writer.writerow(next(csv_reader))
    obfuscate(csv_reader, csv_writer, factory.build(config))


def obfuscate(csv_input_stream, csv_output_stream, strategies):
    for row in csv_input_stream:
        new_row = [new_value(value, index, strategies) for index, value in enumerate(row)]
        csv_output_stream.writerow(new_row)
