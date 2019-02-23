import argparse
from levenshtein import Levenshtein

parser = argparse.ArgumentParser(description="Find the Levenshtein distance between two strings.")
parser.add_argument("string1", help="First string.")
parser.add_argument("string2", help="Second string.")
parser.add_argument("-d", "--delimiter", help="Word delimiter. Default value: space")
parser.add_argument("-A", "--alignment", help="Print alignment.", action="store_true")

args = parser.parse_args()

Levenshtein(args.string1, args.string2, args.delimiter, args.alignment)

