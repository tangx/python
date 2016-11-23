#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# File Name: pypaste.py
# Author: uyinn
# mail: uyinn@live.com
# Created Time: Sat 19 Apr 2014 11:27:24 AM CST
#########################################################################

import os
import sys


def usage(command_name):
    print ur"""
        将两个文件合并左右合并为一个文件
        $ cat file1.txt  file2.txt
        Tue Sep  8 14:41:55 HKT 2015
        Tue Sep  8 14:41:59 HKT 2015

        $ python pypaste.py -d \- file1.txt  file2.txt
        Tue Sep  8 14:41:59 HKT 2015 - Tue Sep  8 14:41:55 HKT 2015

        Usage:
            %s -d sep file1 file2
            + 如果分隔符为特殊字符(空格、引号)时，需要用使用跳脱符号

    """ % command_name

# 三元运算符表达式
# def trans(a,b):
#     return a if a > b else b

def main(file1, file2, sep='\t'):
    # 判断给予的文件是否存在
    for path in file1, file2:
        if not os.path.isfile(path):
            print '%s : is not a file or not exist' % path
            sys.exit(1)

    # 创建两个列表文件
    f1list = list()
    f2list = list()

    # 向之前的两个列表文件中各自添加file1 and file2 的行。
    f = open(file1, 'r')
    f1width = 0
    for line in f.readlines():
        f1list.append(line.strip('\n'))
        # 获取file1的最长行宽度
        f1width = f1width if f1width > len(f1list[-1]) else len(f1list[-1])
        # print f1width
    f.close()

    f = open(file2, 'r')
    for line in f.readlines():
        f2list.append(line.strip('\n'))
    f.close()

    # 获取两个文件最大行数
    maxraw = len(f1list) if len(f1list) > len(f2list) else len(f2list)

    # 输出结果
    for x in xrange(maxraw):
        try:
            # 如果file1是空行，使用空格补全
            # if len(f1list[x]) == 0:
                # print len(f1list[x])
                # print ' ' * f1width-1,
            print f1list[x],
        except:
            # 如果file1无此行，使用空格补全
            # print ' ' * f1width,
            pass
        print sep,
        try:
            print f2list[x],
        except:
            pass
        print ''


if __name__ == "__main__":
    if len(sys.argv) == 5:
        if sys.argv[1] == '-d':
            sep = sys.argv[2]
    elif len(sys.argv) == 3:
        sep = '\t'
    else:
        usage(sys.argv[0])

    file1 = sys.argv[-2]
    file2 = sys.argv[-1]

    main(file1, file2, sep)
