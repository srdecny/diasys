from collections import deque
import itertools
import sys

def Levenshtein(firstString, secondString, delimiter, printDistance, printAlignment, printError, out=sys.stdout):

    wer = {"sub" : 0, "add" : 0, "remove" : 0}
    correctWords = 0
    minimumDistance = 0

    words_first = firstString.split(delimiter)
    words_second = secondString.split(delimiter)

    for first, second in itertools.zip_longest(words_first, words_second, fillvalue=""):

        len1 = len(first) + 1
        len2 = len(second) + 1
        distance = [[0 for x in range(len2)] for y in range(len1)]
        backtrack = [[0 for x in range(len2)] for y in range(len1)]

        for i in range(0, len1):
            distance[i][0] = i
            backtrack[i][0] = "DOWN"
        
        for j in range(0, len2):
            distance[0][j] = j
            backtrack[0][j] = "LEFT"

        for i in range(1, len1):
            for j in range(1, len2):
                if first[i-1] == second[j-1]:
                    subCost = 0
                else:
                    subCost = 2
                mindistance = min(
                    distance[i-1][j] + 1,
                    distance[i][j-1] + 1,
                    distance[i-1][j-1] + subCost
                )

                distance[i][j] = mindistance

                if mindistance == distance[i-1][j-1] + subCost:
                    backtrack[i][j] = "DIAG"
                elif mindistance == distance[i-1][j] + 1: # deletion
                    backtrack[i][j] = "DOWN"
                else:
                    backtrack[i][j] = "LEFT"

        minimumDistance = distance[len1-1][len2-1]

        i = len1 - 1
        j = len2 - 1
        alignment = deque()

        while not (i == 0 and j == 0):
            previousCell = backtrack[i][j]
            if previousCell == "DOWN":
                alignment.append(f"Remove letter {first[i-1]} at index {j-1}")
                wer["remove"] += 1
                i-=1
            elif previousCell == "LEFT":
                alignment.append(f"Add letter {second[j-1]} at index {j-1}")
                wer["add"] += 1
                j-=1
            elif previousCell == "DIAG":
                if first[i-1] != second[j-1]:
                    alignment.append(f"Substitute character {first[i-1]} for character {second[j-1]} at index {j-1}")
                    wer["sub"] += 1
                i-=1
                j-=1

        if (len(alignment)) == 0:
            correctWords += 1
            
    if (printDistance):
        out.write(f"Minimum edit distance: {minimumDistance}")

    if (printAlignment):
        if len(alignment) > 0:
            out.write(f"Alignment for {first} -> {second}")
        while len(alignment) > 0:
            out.write(alignment.pop())
    
    if (printError):
        ratio = (wer["sub"] + wer["add"] + wer["remove"])/(wer["sub"] + wer["remove"] + correctWords)
        out.write (f"WER: {ratio}")

    out.write('\n')




