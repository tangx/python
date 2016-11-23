#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  ??
@author: TangHsin
@license: Apache Licence
@mailto: uyinn28@gmail.com
@site: 
@software: PyCharm Community Edition
@FILE: pyurldownload.py
@time: 2016/7/9 9:45
"""

import urllib
import urllib2
# import requests
import os


def urllib_down(url):
    # 获取文件名
    file_list = os.path.split(url)
    filename = file_list[-1]

    # 创建保存目录
    file_dir = os.path.join('e:', 'pydown')
    try:
        os.makedirs(file_dir)
    except Exception as err:
        pass
    file_full_name = os.path.join(file_dir, filename)

    # 下载文件
    urllib.urlretrieve(url, file_full_name)

    print os.listdir(file_dir)
    pass


def urllib2_down(url):
    # 获取文件名
    filename = os.path.split(url)[-1]
    # 创建保存路径
    file_fullpath = os.path.join('e:', 'pydown', filename)
    try:
        os.makedirs(os.path.split(file_fullpath)[0])
    except:
        pass

    f = urllib2.urlopen(url)        # 打开一个文件
    data = f.read()             # 读取文件

    with open(file_fullpath, 'wb') as code:     # 以二进制方式写入文件
        code.write(data)

    print os.listdir(os.path.split(file_fullpath)[0])
    pass

def request_down(url):
    r = requests.get(url)
    with open("code3.zip", "wb") as code:
        code.write(r.content)

def main():
    file_url = ur'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'

    urllib2_down(file_url)
    # urllib_down(file_url)

    pass


if __name__ == '__main__':
    main()
