# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:45:45 2018

@author: cc
"""
from __future__ import absolute_import
#from NER import rnn
import textrank_w2vec as tw
import jieba
import jieba.analyse
import json
import sys  
reload(sys)
sys.setdefaultencoding('utf-8')

file_name = "cfp_.txt"

content = open(file_name, 'rb').read()
#添加新词
with open("keywords.txt",'rb') as f:
    kwords=f.readlines()
for i in kwords:
    jieba.add_word(i)  
keywords=[]
for x in jieba.analyse.textrank(content,topK=10,withWeight=True,allowPOS=('ns')):
    print('%s%f' % (x[0],x[1]))
    keywords.append(x[0])
keywords = ','.join(keywords)
key_sent = tw.key_sent()
write_data = dict()
write_data[u"keywords"] = keywords
write_data[u"key_sentence"] = key_sent

with open("key.json",'wb') as f:
    purpose=json.dumps(write_data,encoding='UTF-8',ensure_ascii=False)
    f.write(purpose)
print ("写入完成")
