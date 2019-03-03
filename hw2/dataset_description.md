## DSTC2
Entropy: 6.758144480444949

## Babi
Entropy of a task #1: 6.126947578998473

Entropy of a task #2: 8.3580746906244

Entropy of a task #3: 7.553446152311607

Entropy of a task #4: 6.965645120010741

Entropy of a task #5: 7.726818893490705

Entropy of a task #6: 8.3580746906244

## All the news
Entropy: 9.971523864279035

# Summary
The DSTC2 dataset consists of dialogues between an user and a restaurant recommendation chatbot, so the language used is limited, thus the relatively low entropy score.

Babi dataset was similar to the DSTC2 one, but used more situations, some more complicated than others, however the dataset quality is not very good. The references to API calls and variable names brought the entropy down.

All the news dataset has the largest entropy, since the content range is much more varied compared to the other datasets, even though it seems to be focused on politics and the articles are from a relatively narrow time span, since only first 10k sentences was used. Thus, the entropy is still relatively low, compared to the average entropy of an English word, which is around 12 bits (Shannon).