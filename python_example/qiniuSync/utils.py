"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@python_version: python_x86 3.5.2
@site: octowahle@github
@software: PyCharm Community Edition
@file: utils.py
@time: 2016/12/1 18:25
"""

import os
import sys


def _uri_encode_win32(f):
    # f=r".\path\filename.png"
    # f=r".filename.png"

    f = f[2:]

    # '/'.join(os.path.split(f))

    f_tuple = os.path.split(f)
    if len(f_tuple[0]) == 0:
        # print f
        return f
    else:
        # print '/'.join(f_tuple)
        return '/'.join(f_tuple)


def _uri_encode_posix(f):
    # f = './path/filename.png'
    # f = './filename.png'

    return f[2:]
