#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
import jieba
import jieba.posseg
import logging

#结巴分词设定
jieba.setLogLevel(logging.INFO)
jieba.load_userdict("userdict_10_re.txt")

def cutstr(string): #参数为一列字符串
    body = urllib.parse.urlencode({'text':string}).encode('utf-8')
    word={}

    url = 'http://ltpapi.xfyun.cn/v1/cws'
    api_key = '1a41ee3c2bc04f3dcb03f7bba41b932b'
    param = {'type': 'dependent'}

    x_appid = '5be3c2ec'
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}

    #中文分词(cws)
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read() 
#    print(result.decode('utf-8'))
    word['cws']=json.loads(result.decode('utf-8'))['data']['word'] #字符串->字典->列表
   
   #词性标注(pos)
    url = 'http://ltpapi.xfyun.cn/v1/pos'
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read() 
#    print(result.decode('utf-8'))
    word['pos']=json.loads(result.decode('utf-8'))['data']['pos'] #字符串->字典->列表
    return word #返回值为字典

def reduce(word):       #排除名词动词形容词以外的部分
    k=[]
    keep=['v','a','n','ns','nz','vn','zn','l','b','f','q','t','zs']
    for i in range(len(word['pos'])):
        if word['pos'][i] not in keep:
            k.append(i)
    k=list(reversed(k))
    for i in k:
        del word['cws'][i]
        del word['pos'][i]
        del word['use'][i]
    return word

def jbcut(string):
    count=0
    word={}
    word['cws']=[]
    word['pos']=[]
    word['use']=[]
    tmp = jieba.posseg.cut(string)
    for w in tmp:
        word['cws'].append(w.word)
        word['pos'].append(w.flag)
        word['use'].append(False)
        count+=1
    return word

#string='伪分布式安装是指在一台机器上模拟一个小——的集群。'
#word=cutstr(string)
#reduce(word)
#print(word)
#word=jbcut(string)
#reduce(word)
#print(word)
#print(word['cws'][5])