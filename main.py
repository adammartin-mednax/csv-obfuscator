import sys
from csv_obfuscator import process


def main():
    columns_to_obfuscate = list(map(int, sys.argv[1].split(",")))

    process(columns_to_obfuscate)


if __name__ == "__main__":
    main()
