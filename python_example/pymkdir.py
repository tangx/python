#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: octowahle@github
@software: PyCharm Community Edition
@file: pymkdir.py
@time: 2016/11/23 18:48
"""

import os
import sys


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print "%s: cannot create directory '%s': No such file or directory" % (sys.argv[0], path)


def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)


def print_help():
    print '''Usage: mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
  -p, --parents     no error if existing, make parent directories as needed
  -v, --verbose     print a message for each created directory
  -Z, --context[=CTX]  set the SELinux security context of each created
                         directory to default type or to CTX if specified
      -h, --help     display this help and exit
      -v, --version  output version information and exit
    '''
    sys.exit(0)


def print_version():
    print "pymkdir 0.1"


def main():
    # print out help infomation
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()

    # print out version infomation
    if "-v" in sys.argv or "--version" in sys.argv:
        print_version()

    if '-p' == sys.argv[1] or '--parents' == sys.argv[1]:
        # create dir even if it's parent dir is not exist
        for path in sys.argv[2:]:
            mkdir_p(path)
    else:
        # create dir
        for path in sys.argv[1:]:
            mkdir(path)


if __name__ == '__main__':
    main()
