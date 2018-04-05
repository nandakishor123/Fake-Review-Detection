import re
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import ngrams
from nltk.corpus import movie_reviews
from collections import Counter

bigramsDictionary = Counter()
unigramsDictionary = Counter()
bigramsProbability = {}

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

new_words = []
for w in all_words:
	if w.isalpha():
		new_words.append(w)

stopWords = set(stopwords.words("english"))
character = {'u'}
tokensFiltered = []

for token in new_words:
	if token not in stopWords:
		tokensFiltered.append(token)


unigramsDictionary.update(Counter(tokensFiltered))
grams = ngrams(tokensFiltered,2)
bigramsDictionary.update(Counter(grams))

for key,val in bigramsDictionary.items():
	p = "p("+key[0]+"/"+key[1]+")"
	bigramsProbability[p] = float(val)/unigramsDictionary[key[0]]

f = open('bigramsProbability.csv','w')
with f:
	writer =csv.writer(f)
	writer.writerows(bigramsProbability.items())
f.close
