#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import chardet
import math

class TrieNode:  
    __slots__ = ['letters', 'word_count', 'ends_word']

    def __init__(self):
        self.letters = {}
        self.word_count = 0
        self.ends_word = False


class Contacts:  
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current = self.root
        for ch in word:
            current.word_count += 1
            if ch not in current.letters:
                current.letters[ch] = TrieNode()
            current = current.letters[ch]

        current.word_count += 1
        current.ends_word = True

    def partial(self, prefix):
        """
        Returns the number of words containing this prefix.
        :param prefix:
        :return:
        """
        current = self.root
        for ch in prefix:
            if ch in current.letters:
                current = current.letters[ch]
            else:
                # prefix was not found
                return 0

        return current.word_count

def log(x):
	print x

def cut_words(strs):
	nums = range(len(strs))
	single_words = [strs[i] for i in nums]
	three_gram = [strs[i:i+3] for i in nums[:len(strs) - 3]]
	# map(lambda x: log(x), three_gram)
	two_words = set([strs[i] + strs[j] for i in nums for j in nums if i != j])
	two_words = {x:0 for x in two_words}
	# map(lambda x: log(x), two_words.itervalues())
	return three_gram, two_words

def cal_entropy(total, data):
	sum_entropy = 0
	for i in data:
		a = float(i) / float(total)
		sum_entropy += -1 * a * math.log(a, 2)
	return sum_entropy


def get_base_data(dict_three_gram, key):
	base = []
	for k in dict_three_gram.iterkeys():
		if key == k[0:2]:
			# print k
			base.append(dict_three_gram[k])
	return base


if __name__ == '__main__':
	# obj = Contacts()
	# obj.add('word')
	# if obj.contains('word'):
	# 	print 'easy'
	test_str = '''每天都有网友问我：2017年做淘宝客还赚钱吗？我：2017年做淘宝客还可以继续好好做。各大门户虽然也跟我们小站长共分一杯羹，但是毕竟我们可以推广的商品太多了，现在网民购物的也越来越多了，所以淘宝客依然还有很大的发展空间。至少未来两三年内淘宝客大格局估计不会有太大变化。所以就淘宝客赚钱的这一话题，谈谈自己的一些看法。纵观这两年的所有网上兼职的工作，淘宝客算的上是最给力的，是最适合个人站长操作的项目，它实现了淘宝、网店商家、个人站长（淘宝客）三方共赢的良好局面，就连各大门户现在也在操作淘宝客。但很多人都在说淘客赚不到钱了，为什么做了那么多淘宝客的网站，最后赚钱的就一个呢？让我来跟大家分析一下原因。'''
	
	three_gram, two_words = cut_words(test_str.decode("utf-8"))
	# print test_str.decode("utf-8")
	preTrie = Contacts()
	postTrie = Contacts()
	map(lambda x: preTrie.add(x), three_gram)
	map(lambda x: postTrie.add(x[::-1]), three_gram)
	reversed_three_gram = [x[::-1] for x in three_gram]
	dict_reversed_three_gram = {}
	dict_three_gram = {}
	for key in reversed_three_gram:
		dict_reversed_three_gram.setdefault(key, 0)
		dict_reversed_three_gram[key] += 1
	for key in three_gram:
		dict_three_gram.setdefault(key, 0)
		dict_three_gram[key] += 1
	a = preTrie.partial('淘宝'.decode("utf-8"))
	b = get_base_data(dict_three_gram, '淘宝'.decode("utf-8"))
	c = postTrie.partial('淘宝'.decode("utf-8")[::-1])
	d = get_base_data(dict_reversed_three_gram, '淘宝'.decode("utf-8")[::-1])
	print cal_entropy(a, b)
	print cal_entropy(c, d)