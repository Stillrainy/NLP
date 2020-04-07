#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Author: Shuyuan Yang
# Filename: word2vec.py


import json
import numpy as np
import gensim
import math


"""global variable
"""
model_file = 'news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(
    model_file, binary=True, limit=50000)


def word_similarity(word_1, word_2):
    # Initialize the higher-dimensional vector
    word_1_vec = word_2_vec = np.zeros((64), dtype='float32')

    try:
        word_1_vec = model.__getitem__(word_1)
        word_2_vec = model.__getitem__(word_2)

        # Normalized cosine distance [-1, 1] -> [0, 1]
        similarity = 1-math.acos(model.similarity(word_1, word_2))/math.pi
    except KeyError:
        similarity = 0
    return {
        'status': True,
        'data': {'similarity': similarity, 'word1_weight': word_1_vec.tolist(), 'word2_weight': word_2_vec.tolist()}
    }


if __name__ == '__main__':
    print(word_similarity(input('1: '), input('2: '))['data']['similarity'])
