#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: octowahle@github
@software: PyCharm Community Edition
@file: batch_files_rename.py
@time: 2016/11/23 15:56
"""

import os
import sys


def rename_file(work_dir, old_ext, new_ext):
    for old_name in os.listdir(work_dir):
        # print old_name

        file_name, file_ext = os.path.splitext(old_name)
        # print file_name, file_ext

        # file extension matched
        if file_ext == old_ext:
            # print old_name

            # 2 ways to get new_name
            new_name = old_name.replace(old_ext, new_ext)
            # new_name = filename + new_ext

            # print old_name, new_name

            # have to use os.path.join()
            # otherwise may missing file
            os.renames(
                os.path.join(work_dir, old_name),
                os.path.join(work_dir, new_name)
            )


def usage():
    print "Usage: %s work_dir old_ext new_ext" % (sys.argv[0])


def main():
    # work_dir = r'E:\Documents\GitHub\python'
    # old_ext = '.bak'
    # new_ext = '.ori'

    try:
        # the files in which folder
        work_dir = sys.argv[1]

        # which kind of files to rename
        old_ext = sys.argv[2]

        # the new extension for files
        new_ext = sys.argv[3]

        # do rename
        rename_file(work_dir, old_ext, new_ext)

    except:
        usage()


if __name__ == '__main__':
    main()
