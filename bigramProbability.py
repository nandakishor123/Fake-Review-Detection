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
bigramProbability = {}

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


def getUnigrams(token):
	unigramsDictionary.update(Counter(token))
	return

def getBigrams(token):
	grams = ngrams(token,2)
	bigramsDictionary.update(Counter(token))
	return


for token in tokensFiltered:
	getUnigrams(token)
	getBigrams(token)

for key,val in bigramsDictionary.items():
	p = "p("+key[1]+"/"+key[0]+")"
	bigramsProbability[p] = val/unigramsDictionary[key[0]]
# f = open('bigrams.csv', 'w')    #creating csv file for storing bigrams
# with f:
# 		writer = csv.writer(f)
# 		writer.writerows(fdist.most_common())
# f.close
#
# f = open('bigramProbability.csv', 'w')   #Creating csv file for bigram probability
# with f:
# 	writer = csv.writer(f)
# 	writer.writerows(bigramsProbability.items())
# f.close()
