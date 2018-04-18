from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pa
from sklearn.feature_extraction.text import CountVectorizer
import csv

def to_lower(text):
    sentence = []
    for w in text:
        sentence += w.lower()
    return sentence

def remove_stopwords(sentence):
    word_tokens = []
    stop_words = set(stopwords.words('english'))
    for text in sentence:
        word_tokens += word_tokenize(text)
    filtered_sentence = []
    for w in word_tokens:
        text = ''
        for word in w:
            if w not in stop_words:
                text += w + ' '
        filtered_sentence += text
    return filtered_sentence

def nonletter_removal(sentence):
    filtered_sentence = []
    for i in sentence:
        text = ''
        for char in i:
            if char.isalpha():
                text += char
        filtered_sentence+=text
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
    vectorizer = CountVectorizer()
    vectorizer.fit(processed_text)
    vector = vectorizer.transform(processed_text)
    numerical_feature_vectors = vector.toarray()

def pre_processing(data):
    sentence = to_lower(data)
    sentence = nonletter_removal(sentence)
    filtered_sentence = remove_stopwords(sentence)
    getNgrams(filtered_sentence,2)
    NumericalFeatureVector(filtered_sentence)

token = []
with open('reviews.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        token += list(row)
    pre_processing(token)
f.close()
