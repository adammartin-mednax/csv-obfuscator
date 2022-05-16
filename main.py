import sys
from csv_obfuscator import process


def main():
    input_file_name = sys.argv[1]
    columns_to_obfuscate = map(int, sys.argv[2].split(","))
    delimiter = (sys.argv[3] if len(sys.argv) > 3 else ",")

    process(input_file_name, "output.csv", delimiter, columns_to_obfuscate)


if __name__ == "__main__":
    main()
