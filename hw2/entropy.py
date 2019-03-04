from math import log2

def entropy(corpus):
    entropy = 0
    textSize = sum(corpus.values())
    for word, frequency in corpus.items():
        probability = frequency / textSize
        entropy += (probability * log2(probability))
    return entropy * -1

# https://stackoverflow.com/a/1884277
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
    