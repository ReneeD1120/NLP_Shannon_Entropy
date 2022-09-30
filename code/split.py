#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:22:20 2022

@author: renee
"""

def split():
    # 读取源文件，文件名最好加上绝对路径
    title='Hellbound-With-You'
    with open('/Users/renee/Desktop/'+title+'.txt', 'r') as f:
        # 把数据写入列表
        wordlist = f.read()
        # 算出总字数
        length = len(wordlist)
    # 设置每个拆分文件的字数
    unit = int(1024*1024*2)
    # 计算新文件的个数，如果总行数整除新文件行数，就取这个商的值，如果不整除，取商加1的值
    file_amount = length // unit + 1 if length % unit > 0 else length // unit
    # 遍历所有新文件
    for num in range(file_amount):
        # 计算新文件中第一行在源文件中对应的行号
        start = num * unit
        # 计算新文件中最后一行在源文件中对应的行号
        end = length if length < (num + 1) * unit else (num + 1) * unit
        # 写入新文件，文件名最好加上绝对路径
        with open(title+str(num + 1) + '.txt', 'w+') as f:
            # 遍历新文件的所有行
            for i in range(start, end):
                # 把列表中的数据写入新文件
                f.write(wordlist[i])
 
if __name__ == '__main__':
    split()

