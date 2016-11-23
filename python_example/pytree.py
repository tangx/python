#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# File Name: pytree.py
# Author: uyinn
# mail: uyinn@live.com
# Created Time: Sat 19 Apr 2014 09:59:56 AM CST
#########################################################################

import os
import sys

# print 'hello world'

def main(path,pushcount):
    pushcount=pushcount+1
    dirLists=os.listdir(path)
    for dirlist in dirLists:
        son_path=os.path.join(path,dirlist)
        print ' |'*(pushcount),
        if os.path.isdir(son_path):
            print '--*',dirlist
            main(son_path,pushcount)
#        else:
#            print  '|__',dirlist
        if os.path.isfile(son_path):
            print '|__',dirlist



if __name__=="__main__":
    if len(sys.argv)==1:
        path=os.getcwdu()
    elif len(sys.argv)>1:
        path=sys.argv[1]
    else:
        print 'Usage: %s [path]' % sys.argv[0]
    print '%s' % path
    main(path,pushcount=-1)
