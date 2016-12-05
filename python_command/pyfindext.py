#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@python_version: python_x86 3.5.2
@site: octowahle@github
@software: PyCharm Community Edition
@file: pyfindext.py
@time: 2016/12/5 16:39
"""

__doc__ = '''find file by specify file extension'''

import os
import sys


def usage():
    print __doc__
    print "Usage pyfindext.py path ext1 ext2"
    sys.exit(1)


def _init(ext):
    ext = ext.lstrip('.')
    ext = '.' + ext

    return ext.lower()


def find_ext(path, ext):
    ext = _init(ext)

    for dir_name, sub_dirs, sub_files in os.walk(path):

        for sub_file in sub_files:
            file_ext = os.path.splitext(sub_file)[-1]
            # print file_ext
            file_ext = file_ext.lower()
            if ext == file_ext:
                file_path = os.path.join(dir_name, sub_file)
                print os.path.normcase(file_path)


def main(path, exts):
    for ext in exts:
        find_ext(path, ext)


if __name__ == '__main__':
    # path = r'E:\Documents\GitHub\python'
    # ext = 'Py'
    # l = ['', path, 'pY', '.XML']
    # main(l[1], l[2:])

    if len(sys.argv) < 3:
        usage()

    path = sys.argv[1]
    exts = sys.argv[2:]
    main(path, exts)
