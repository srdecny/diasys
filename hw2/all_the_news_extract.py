#!/usr/bin/python3

import os
import nltk

from entropy import entropy
from entropy import find_nth

def parse_corpus(path):
    corpus = {}
    sentences_count = 0

    with open(path) as articles:
        for sentence in articles:
            sentences_count += sentence.count(".") # an article can contain multiple sentences
            content_comma_index = find_nth(sentence, ",", 9) # because the content itself can contain commas
            for word in nltk.word_tokenize(sentence[content_comma_index:]):
                if word in corpus:
                    corpus[word] += 1
                else:
                    corpus[word] = 1
            if sentences_count > 10000:
                return corpus

    return corpus

path = "/home/srdecny/Downloads/all-the-news/articles1.csv"
corpus = parse_corpus(path)
print(entropy(corpus))
