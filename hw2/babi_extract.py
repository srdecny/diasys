#!/usr/bin/python3

import os
import nltk

from entropy import entropy

def parse_corpus(path, task_number):
    corpus = {}
    sentences_count = 0

    for dataset in os.listdir(path):
        if str(task_number) in dataset and "dev" in dataset:
            with open(path + "/" + dataset) as data_file:
                for sentence in data_file:
                    if not sentence == "":
                        sentences_count += 1
                        for word in nltk.word_tokenize(sentence):
                            if word == "<SILENCE>":
                                continue
                            if word in corpus:
                                corpus[word] += 1
                            else:
                                corpus[word] = 1
                        if sentences_count > 10000:
                            return corpus
    return corpus

path = "/home/srdecny/Downloads/dialog-bAbI-tasks"
for i in range(1, 7):
    corpus = parse_corpus(path, i)
    print(f"Entropy of a task #{i}: " + str(entropy(corpus)))