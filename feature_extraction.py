import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
from collections import Counter

bigramsDictionary = Counter()
unigramsDictionary = Counter()
bigramsProbability = {}

def tolower(sentence):
    for w in sentence:
        sentence = w.lower()
    return sentence

def remove_nonletter(sentence):
    filtered_sentence = []
    for w in sentence:
        if w.isalpha:
            filtered_sentence.append(w)
    return filtered_sentence

def stopword_removal(sentence):
    filtered_sentence =[]
    stopWords = set(stopwords.words('english'))
    for word in sentence:
        if word not in stopWords:
            filtered_sentence.append(word)
    return filtered_sentence

def getUnigrams(token):
	unigramsDictionary.update(Counter(token))
	return

def getBigrams(token):
    bigramsDictionary.update(Counter(token))
    return

def pre_processing(token):
    sentence = tolower(token)
    sentence = remove_nonletter(sentence)
    filtered_sentence = stopword_removal(sentence)
    return filtered_sentence

fp = open('reviews.csv','r')
line = fp.readline()
for line in fp:
    token = pre_processing(line)
    getUnigrams(token)
    getBigrams(token)
fp.close()

for key,val in bigramsDictionary.items():
	p = "p("+key[1]+"/"+key[0]+")"
	bigramsProbability[p] = float(val)/unigramsDictonary[key[0]]
