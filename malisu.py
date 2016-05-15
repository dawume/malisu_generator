#!/usr/bin/env python
#coding:utf-8

import random
import base64

class Malisu(object):
	def __init__(self, ori_name):
		random.seed(base64.b16encode(ori_name))
		self.dict = {}
		self.dict['adj'] = [term.strip().split('\t')[0] for term in open('new_adj.txt')]
		self.dict['name'] = [term.strip() for term in open('name.txt')]
		self.dict['title'] = [term.strip() for term in open('title.txt')]

	def get_name_string(self, min_n, max_n):
		return '·'.join(random.sample(self.dict['name'], random.randint(min_n, max_n)))

	def get_adj_string(self, min_n, max_n):
		return ','.join(random.sample(self.dict['adj'], random.randint(min_n, max_n)))

	def get_title(self):
		return random.choice(self.dict['title'])

	def pattern(self):
		name = self.get_name_string(10, 15)
		adj = self.get_adj_string(8, 10)
		title = self.get_title()
		age = random.randint(1,5)

		name_pattern = '听好了, 我的名字是%s, 叫我%s好了' % (name, name.split('·')[0])
		adj_pattern = '在我%d岁的时候, 已经有了%s%s称号了' % (age, adj, title)
		return '\n'.join([name_pattern, adj_pattern])

if __name__ == '__main__':
	ori_name = 'dawu'
	malisu = Malisu(ori_name)
	print malisu.pattern()
