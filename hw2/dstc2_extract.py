#!/usr/bin/python3

import json
import os
import nltk

from entropy import entropy

path = "/home/srdecny/Downloads/data"

def parse_corpus(path_to_root):
    corpus = {}
    sentences_count = 0

    for day in os.listdir(path_to_root):
        path_to_day = path_to_root + "/" + day
        for call in os.listdir(path_to_day):
            path_to_call = path_to_day + "/" + call
            with open(path_to_call + "/log.json") as data_file:
                data = json.loads(data_file.read())
                for turn in data["turns"]:
                    sentence = nltk.word_tokenize(turn["output"]["transcript"])
                    sentences_count += 1
                    for word in sentence:
                        if word in corpus:
                            corpus[word] += 1
                        else:
                            corpus[word] = 1
                    if sentences_count > 10000:
                        return corpus
    return corpus

corpus = parse_corpus(path)
print(entropy(corpus))