# -*- coding: utf-8 -*-

import pickle

pickle_file = open('level-5-banner.p', 'rb')
data = pickle.load(pickle_file)
print(data)
print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data]))
# 这个列表推导式是怎么处理的？
