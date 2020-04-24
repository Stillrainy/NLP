#!/usr/bin/python
# -*- coding: UTF-8 -*-

import str_moudle as sm
from word2vec import word_similarity


def sentence_similarity(str1=None, str2=None):
    if(str1 == None and str2 == None):
        str1 = input('输入标准答案：')
        str2 = input('输入学生答案：')
    word1 = sm.sentence2words(str1)
    word2 = sm.sentence2words(str2)

    def max_similarity(word1, word2):
        total = 0
        match = len(word1['cws'])
        for i in range(len(word1['cws'])):
            max = 0
            word2_id = 0
            max_id = -1
            for j in range(len(word2['cws'])):
                if(word2['use'][word2_id] == False):
                    tmp = word_similarity(word1['cws'][i], word2['cws'][j])[
                        'data']['similarity']
                    if(tmp > max and tmp > 0.6):
                        max = tmp
                        max_id = word2_id
                word2_id += 1
            if(max_id != -1):
                word2['use'][max_id] = True
            total += max
        if(match != 0):
            match = total / match
        else:
            match = 0
        return match

    match = max_similarity(word1, word2)
#    match = match * match
    print('两字符串的匹配度：{:.2%}'.format(match))
    return match


def section_similarity(str1=None, str2=None):
    if(str1 == None and str2 == None):
        str1 = input('输入标准答案：')
        str2 = input('输入学生答案：')
    rs1 = str1.split('。')
    rs2 = str2.split('。')
    while '' in rs1:
        rs1.remove('')
    while '' in rs2:
        rs2.remove('')
    sentence1 = {}
    sentence2 = {}
    sentence1['word'] = []
    sentence1['ues'] = []
    sentence2['word'] = []
    sentence2['ues'] = []
    for s in rs1:
        sentence1['word'].append(s)
        sentence1['ues'].append(False)
    for s in rs2:
        sentence2['word'].append(s)
        sentence2['ues'].append(False)

    total = 0
    match = len(sentence1['word'])
    for s2 in sentence2['word']:
        max = 0
        tmp_id = 0
        max_id = 0
        for s1 in sentence1['word']:
            if(sentence1['ues'][tmp_id] == False):
                tmp = sentence_similarity(s1, s2)
                if(tmp > max):
                    max = tmp
                    max_id = tmp_id
            tmp_id += 1
        total += max
        sentence1['ues'][max_id] = True
    if(match != 0):
        match = total / match
    else:
        match = 0
    return match


if __name__ == '__main__':
    ctu = 'yes'
    while ctu == 'yes':
        print(sentence_similarity())
        ctu = input('是否继续(yes/no)：')
