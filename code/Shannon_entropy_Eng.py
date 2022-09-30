#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 02:58:22 2022

@author: renee
"""
import re
import math
from prettytable import PrettyTable
import numpy
#import random
#import time

entropy_0 = []

for i in range(1, 46):
    print(i)
    path = '/Users/renee/Documents/Eng/' + str(i) + '.txt'
    with open(path) as data:
        datacontext = data.read()
    data.close()
    with open("/Users/renee/Documents/Eng/d2.txt", 'a') as data_1:
        data_1.write(datacontext)
        data_1.close()
    with open("/Users/renee/Documents/Eng/d2.txt", 'r', encoding='UTF-8') as f:
        content = f.read()

    # print('预处理前的字符串：')
    #print(content)
    # Str =content#引入数据
    content = content.replace("Please go to", '')
    content = content.replace("install our App to read the latest chapters for free", '')
    content = content.replace("Previous Chapter", '')
    content = content.replace("Next Chapter", '')
    content = content.replace("E.3.3.", '')
    content = content.replace("Chapter", '')
    a = re.findall(r'[^\*"/:?|,!-.%‘—;()’“”‘’。°【0123–456789】<>\[\]]', content, re.S)  #
    a1 = "".join(a)  # 去掉特殊字符
    b = a1.lower()  # 大写变小写
    c = ' '.join(b.split())  # 去连续的空格
    '''fh = open('/Users/renee/Documents/'+title+'Res.txt', 'w', encoding='utf-8')#写操作
    fh.write(c)
    fh.close()

    with open('/Users/renee/Documents/'+title+'Res.txt','r',encoding='UTF-8') as f:  # 遍历
    content1 = f.read()'''
    Str1 = c
    # print('预处理后的字符串：')
    # print(Str1)
    sum_1 = 0
    Hx = 0
    k = 0
    j = 0
    s = 0
    Hx = []
    for a1 in Str1:
        if a1 in 'abcdefghijklmnopqrstuvwxyz ':
            sum_1 += 1
    print(f'"字符总数为":{sum_1}个')
    # strfloat=numpy.empty(27,dtype=float)
    # strArr=numpy.empty(27,dtype=str)
    resoult = {} # 定义一个空字典
    for i in 'abcdefghijklmnopqrstuvwxyz ':  # 遍历输入的字符串，以键值对的方式存储在字典中
        resoult[i] = Str1.count(i)
        # print(type(Str1.count))
    for key in resoult:  # 遍历字典，格式化输出结果
        Hx.append((resoult[key] / sum_1) * math.log((sum_1 / resoult[key]), 2))  # 信
    print(Hx)
    Hx_1 =round(sum(Hx),5)
    print(Hx_1)
    entropy_0.append(Hx_1)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2, 92, 45)
plt.title('Change of Shannon Entropy for English texts')
plt.xlabel('File Size(M)')
plt.ylabel('Shannon Entropy(Bits/letter)')
plt.plot(x, entropy_0, color='purple'
         )
