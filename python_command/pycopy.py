#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: octowahle@github
@software: PyCharm Community Edition
@file: pycopy.py
@time: 2016/11/24 10:22
"""

import os
import sys
import shutil
import getopt


def usage():
    print '''
    Usage:
        pycopy.py [OPTIONS] src dst
        pycopy.py [OPTIONS] src1 src2 src3  directory

    OPTIONS:
        '-f' : force to overwrite dst
        '-i' : interactive to overwrite dst
        '-r' : recutive copy directory # didn't use
    '''


def copy(src, dst):
    if os.path.isdir(src):
        if os.path.exists(dst):
            print "Error: Directory %s already exists!"
        else:
            shutil.copytree(src, dst)
    elif os.path.isfile(src):
        shutil.copy(src, dst)
    else:
        pass

    print "%s -> %s" % (src, dst)


def overwrite(dst, flag):
    if flag:
        return True

    ans = raw_input("pycopy.py: overwrite '%s' , Y or N ? " % dst)
    if ans in "Yy":
        return True
    else:
        return False


def copy_files(src, dst, ow_flag=False):
    # copy multipule files
    print src

    if len(src) == 1:
        fd = src[0]
        if os.path.isdir(dst):
            base_name = os.path.basename(fd)
            dst = os.path.join(dst, base_name)

        if os.path.exists(dst) and not overwrite(dst, ow_flag):
            # don't overwrite, next one
            sys.exit(0)

        copy(fd, dst)

    elif len(src) > 1:
        if not os.path.isdir(dst):
            print "Error: %s is not exist or not a directory."
            sys.exit(1)

        for fd in src:
            dst_new = os.path.join(dst, os.path.basename(fd))
            if os.path.exists(dst_new) and not overwrite(dst_new, ow_flag):
                # don't overwrite, next one
                continue

            copy(fd, dst_new)


def copy_dir(src, dst):
    pass


def main():
    if '-h' in sys.argv:
        usage()
        sys.exit(0)

    opts, args = getopt.getopt(sys.argv[1:], "hifr")

    if len(args) < 2:
        print "Error: not enough arguments"
        sys.exit(1)
    else:
        src = args[:-1]
        dst = args[-1]

    for o, a in opts:
        if '-f' in o:
            ow_flag = True
            copy_files(src, dst, ow_flag)
            return None
        if '-i' in o:
            ow_flag = False
            copy_files(src, dst, ow_flag)
            return None
        if '-r' in o:
            pass

    copy_files(src, dst)


if __name__ == '__main__':
    main()
