## Overview
This is a single command line utility for printing minimum edit distance, alignment and WER of two strings. The edit distance is calculated using Levenshtein distance. The cost for substitute operation is 2.


## Usage
```$ python3 minDistUtil.py [flags] [string1] [string2]```

For the description of flags, use the ```-h``` flag to see help info.

## Examples
```$ python3 minDistUtil.py -D "foo" "bar"```


Other examples are in the ```tests.py``` file.

## Code structure

```minDistUtil.py``` contains the arguments parser.

```levenshtein.py``` contains the actual implementation for calculating Levenshtein distance and other stats.

```tests.py``` contains unit tests.