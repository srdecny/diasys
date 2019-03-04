THe vystadial dataset consists of transcriptions of conversations between seniors, news report and queries to a chatbox for finding optimal public transport routes. 

The average cross-entropy using log2 of a sentence using bigrams for the whole dataset is 15.92.
The cross-entropy of a first line of the training set ("JEŠTĚ JEDNOU ŽE JSI ŠPATNĚ SPALA V NOCI NEBO") is 21.07 - higher than the dataset, since it's a relatively long sequence and also because the sentence comes from a senior dialogue part of the dataset, which is probably the most complex.
THe cross-entropy for a dev set is 17.78. I'm not sure why is this the case - I can only guess the distribution of transcription types wasn't the same as in the training set - after all, it does contain only 2k sentences, compared to the 22k lines of the training set.
