from math import log2

def entropy(corpus):
    entropy = 0
    textSize = sum(corpus.values())
    for word, frequency in corpus.items():
        probability = frequency / textSize
        entropy += (probability * log2(probability))
    return entropy * -1

