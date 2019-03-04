#!/usr/bin/python3

import os
import sys

# collapse all transcriptions into one file for training
# probably could be more efficient using bash. oh well.
for train_file in os.listdir(sys.argv[1]):
    if ".trn" in train_file:
        sentence = open(sys.argv[1] + '/' + train_file).read()
        if sentence != "":
            print(sentence)

