#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        pyFileFinder.py
# Purpose:
#
# Author:      uyinn
# Mailto:      uyinn@live.com
#
# Created:     18/04/2014
# Copyright:   (c) uyinn 2014
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import os  # import libs
import sys

def main(path, types):

    try:
        # 获取目录中的文件名
        folder_lists = os.listdir(path)

        for folder_list in folder_lists:
            son_path = os.path.join(path, folder_list)  # 组合原目录路径和文件名
            if os.path.isdir(son_path):  # get new path is a directory or not
                main(son_path, types)  ## true: use main function again
            else:
                ##            print son_path
                file_type = son_path.split('.')[-1].lower()  ## false: 获取文件后缀名
                ##            print file_type
                if file_type in types:  # 如果后最匹配。则输出结果
                    print son_path
    except:
        pass

def usage(command_name):
    print """
    在指定目录中path中查找包含指定后缀的文件
    Usage:
        %s path pf1 [ pf2 pf3]
    """ % command_name

if __name__ == '__main__':
    ##    main(u'd:\python',('pyc','gz'))
    if len(sys.argv) < 3:
        # print "Usage: %s path postfix1[ pf2 pf3 ] " % sys.argv[0]
        usage(sys.argv[0])
        sys.exit(1)

    path = sys.argv[1]  # 获取所需查找路径
    types = []          # 创建后缀列表
    for x in xrange(2, len(sys.argv)):
        types.append(sys.argv[x].lower())  # 通过参数获取后缀

    main(path, types)
