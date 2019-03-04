#!/usr/bin/python3

import os
import kenlm
import sys
from math import log2
from math import log10

data = sys.argv[1]
lm = sys.argv[2]

model = kenlm.LanguageModel(lm)

entropy = 0
lines_count = 0

# the model will return probabilities in base10, we will convert them to base2
logarithm_convert_constant = log10(2)

with open(data) as lines:
    for line in lines:
        lines_count += 1
        words = line.split()
        probability = model.score(words[0]) / logarithm_convert_constant # probability of the first word
        for v, w in zip(words[:-1], words[1:]):
            probability += model.score(v + " " + w) / logarithm_convert_constant
        probability *= 1/len(words)
        entropy += probability
    
entropy = entropy / lines_count # average entropy of a sentence
print (-entropy) 




