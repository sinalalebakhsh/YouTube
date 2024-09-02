import os
import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        pretty(sys.argv[1])


def pretty(user_input):
    with open(user_input, "r") as csv_file:
        table = csv.DictReader(csv_file, delimiter=",")
        print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
