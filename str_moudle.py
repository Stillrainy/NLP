#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


def paragraph2sentences(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    return sentences


def sentence2words(str):
    words = {'cws': [], 'use': []}
    tokenizer = RegexpTokenizer(r'\w+')
    stopWords = set(stopwords.words('english'))

    for w in tokenizer.tokenize(str):
        words['cws'].append(w)

    wordsFiltered = []
    for word in words['cws']:
        if word not in stopWords:
            wordsFiltered.append(word.lower())
    words['cws'] = wordsFiltered
    for i in words['cws']:
        words['use'].append(False)
    return words


# print(sentence2words("To maintain the privilege of using the ArgoNet account to access UWF eLearning online courses, STUDENT acknowledges that he or she is responsible for maintaining the confidentiality of the password and account, and that he or she is fully responsible for all activities that occur under his or her account."))
