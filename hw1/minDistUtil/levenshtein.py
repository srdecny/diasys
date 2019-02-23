def Levenshtein(string1, string2, printAlignment):
    len1 = len(string1) + 1
    len2 = len(string2) + 1
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
            if string1[i-1] == string2[j-1]:
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

    print(distance[len1-1][len2-1])

    if (printAlignment):
        i = len1 - 1
        j = len2 - 1
        alignment = []

        while not (i == 0 and j == 0):
            previousCell = backtrack[i][j]
            if previousCell == "DOWN":
                #alignment.append(f"Remove letter {string1[i]} at index {i-1}")
                alignment.append("REMOVE")
                i-=1
            elif previousCell == "LEFT":
                #alignment.append(f"Add letter {string2[j]} at index {j-1}")
                alignment.append("ADD")
                j-=1
            elif previousCell == "DIAG":
                if string1[i-1] != string2[j-1]:
                    alignment.append(f"Substitute letter {string1[i]} for letter {string2[j],} at index {i-1}")
                    #alignment.append("SWAP")
                i-=1
                j-=1
        for a in alignment:
            print(a)


        




                


    