import re
from nltk.corpus import movie_reviews
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import ngrams
all_words = []

for w in movie_reviews.words():
	all_words.append(w.lower())

#print all_words

new_words = []
for w in all_words:
	if w.isalpha():
		new_words.append(w)

stopWords = set(stopwords.words("english"))
tokensFiltered = []

for token in new_words:
    if token not in stopWords:
        tokensFiltered.append(token)

grams = ngrams(tokensFiltered,2)
fdist = FreqDist(grams)
f = open('bigrams1.csv', 'w')
with f:
    writer = csv.writer(f)
    writer.writerows(fdist.most_common())
f.close
