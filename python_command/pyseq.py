#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        pyseq
# Author:      uyinn
# Mailto:      uyinn@live.com
# Created:     21/04/2014
# version:     python2.7
#-------------------------------------------------------------------------------
import sys

if __name__ == '__main__':
    sysargv=sys.argv
#    print sysargv
# get paraments
    westr='%d'
    sep='\n'

    try:
    #   to get paraments by overview arguments
        for x in xrange(len(sysargv)):
            if sysargv[1] =='-w':
                sysargv.pop(1)
                we=len(str(sysargv[-1]))
                westr='%0'+str(we)+'d'

            elif sysargv[1] == '-s':
                sysargv.pop(1)
                sep=sysargv.pop(1)

    # get start-point,stop-point,and step
        start,step=1,1

        if len(sysargv) == 2:
            stop=sysargv[1]
        elif len(sysargv) == 3 or len(sysargv)==4:
            start=sysargv[1]
            stop=sysargv[2]
            try:
                step=sysargv[3]
            except:
                pass
        else:
            print 'error argvs'
            sys.exit(1)

        wesep=westr+sep

    # call pyseq
        output=''
        for x in xrange(int(start),int(stop)+1,int(step)):
            output+=(wesep % x)
        print output
    except:
        print 'Usage: %s [[-w] [-f sepchar]] [start] stop [step]'


