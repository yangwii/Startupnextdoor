# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:38:24 2017

@author: yangpengjs
"""

import jieba
import pandas as pd
import numpy as np
from collections import Counter

neg = pd.read_excel('data/neg.xls', header=None, index=None)
pos = pd.read_excel('data/pos.xls', header=None, index=None)

# print neg.head()

pos['mark'] = 1
neg['mark'] = 0
pn = pd.concat([pos, neg], ignore_index=True)
neglen = len(neg)
poslen = len(pos)

cw = lambda x: list(jieba.cut(x))
pn['words'] = pn[0].apply(cw)
pn = pn.reindex(np.random.permutation(pn.index))

# print pn.head()

positive_counters = Counter()
negative_counters = Counter()
total_counters = Counter()

for i in range(len(pn['words'])):
    if pn['mark'][i] == 1:
        for word in pn['words'][i]:
            positive_counters[word] += 1
            total_counters[word] += 1
    else:
        for word in pn['words'][i]:
            negative_counters[word] += 1
            total_counters[word] += 1
            
# print positive_counters.most_common(10)
pos_neg_ratios = Counter()
for term, cnt in list(total_counters.most_common()):
    if cnt > 100:
        pos_neg_ratio = positive_counters[term] / float(negative_counters[term] + 1)
        pos_neg_ratios[term] = pos_neg_ratio
        
for word, ratio in pos_neg_ratios.most_common():
    if ratio > 1:
        pos_neg_ratios[word] = np.log(ratio)
    else:
        pos_neg_ratios[word] = -np.log((1 / (ratio + 0.01)))
    
vocab = set(total_counters.keys())
vocab_size = len(vocab)

layers_0 = np.zero((1, vocab_size))

word2index = {}
for i, word in enumerate(vocab):
    word2index[word] = i
    
def update_input_layer(reviews):
    global layer_0
    
    layer_0 *= 0
    for word in reviews:
        layer_0[0][word2index[word]] += 1
        

            