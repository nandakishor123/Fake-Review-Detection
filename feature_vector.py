from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pa
from sklearn.feature_extraction.text import CountVectorizer
import csv

def to_lower(sentence):
    filtered_sentence = []
    for text in sentence:
        temp = []
        for w in word_tokenize(text):
            temp.append(w.lower())
        filtered_sentence.append(' '.join(temp))
    return filtered_sentence

def remove_stopwords(sentence):
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []
    for text in sentence:
        temp = []
        for w in word_tokenize(text):
            if w not in stop_words:
                temp.append(w)
        filtered_sentence.append(' '.join(temp))
    return filtered_sentence

def nonletter_removal(sentence):
    filtered_sentence = []
    for text in sentence:
        temp = []
        for w in word_tokenize(text):
            if w.isalpha():
                temp.append(w)
        filtered_sentence.append(' '.join(temp))
    return filtered_sentence

def getNgrams(filtered_sentence,n):
    counts = dict()
    for i in range(len(filtered_sentence) - n):
        grams = [' '.join(filtered_sentence[i:i + n])]
    for gram in grams:
        if gram not in counts:
            counts[gram] = 1
        else:
            counts[grams]+=1
    with open('bigramcount.csv','w+') as f:
        w = csv.writer(f)
        w.writerows(counts.items())
    f.close()
    return

def NumericalFeatureVector(processed_text):
    for word in processed_text:
        for w in word:
            vectorizer = CountVectorizer()
            vectorizer.fit(w)
            vector = vectorizer.transform(w)
            numerical_feature_vectors = vector.toarray()

def pre_processing(data):
    sentence = to_lower(data)
    sentence = nonletter_removal(sentence)
    filtered_sentence = remove_stopwords(sentence)
    #getNgrams(filtered_sentence,2)
    NumericalFeatureVector(filtered_sentence)

token = []
with open('reviews.csv','r') as f:
    reader = csv.reader(f)
    for i in range(5):
        row = f.readline()
        token.append(row)
        print("\n\n",row)
    pre_processing(token)
f.close()
