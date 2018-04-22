import re
import csv
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

def removeNonLetter(sentence):
	filteredSentence = []
	sentence = word_tokenize(sentence)
	for word in sentence:
		if word.isalpha():
			filteredSentence.append(word)
	filteredSentence = " ".join(filteredSentence)
	return filteredSentence

def preProcessing(sentence):
	sentence = removeNonLetter(sentence)
	return sentence

#main program
fp = open('reviews.csv','r')
line = fp.readline()
dataset = []
for i in range(0,1600):
	line = fp.readline()
	dataset.append(preProcessing(line))
fp.close()

text = dataset

# create the transform
#vectorizer = CountVectorizer(max_df=0.95,min_df=2, max_features=100,stop_words='english')
vectorizer = CountVectorizer()

# tokenize and build vocab
vectorizer.fit(dataset)

# summarize
uniqueWords = sorted(vectorizer.vocabulary_)

# encode document
vector = vectorizer.transform(text)

# summarize encoded vector
print(vector.shape)
countvector = vector.toarray()

#write to file
f = open("countVector.csv", 'w')
with f:
	f.write(",")
	for word in uniqueWords:
		f.write(word+",")
	f.write("\n")
	for i in range(len(text)):
		f.write(text[i]+",")
		for j in countvector[i]:
			f.write(str(j)+",")
		f.write("\n")
f.close
