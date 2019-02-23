import argparse

parser = argparse.ArgumentParser(description="Find the Levenshtein distance between two strings.")
parser.add_argument("string1", help="First string.")
parser.add_argument("string2", help="Second string.")

args = parser.parse_args()

print(args.string1)
print(args.string2)