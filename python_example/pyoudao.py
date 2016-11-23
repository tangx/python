#!/usr/bin/evn python
# encoding:utf-8
#
#  有道词典
#
import urllib
import re
import os
import sys

'''
2016-11-08:
  + 增加 getopt 参数选择
  + "-s / --split " 分别查询参数
  + 默认，将所有参数当成一个短语来查询

2016-11-07:
  + 增加查询短语
  + 增加分别查询单词中的所有参数
  to do: 增加参数 -s --split , 判断选择查询短语或单词
'''


def get_youdao(word):
    word = to_remove_blank(word)
    youdaoDict_url = r'http://youdao.com/w/eng/%s/' % word

    # print youdaoDict_url
    content = urllib.urlopen(youdaoDict_url).read()

    # dict_patt = r'<li> \w*?</li>'
    dict_patt = r'<li>(.*?)</li>'

    patt = re.compile(dict_patt)

    results = patt.findall(content)

    # print results

    for result in results:
        #
        # print result      //
        '''
        result=ur'<li>num. 一；一个</li>'

        分解步骤：
        result2=result.split('<li>')[1]
        设<li>为分隔符，对result进行分割，获得一个数组，取右边得result2
        result3=result2.rsplit('</li>')[0]
        设</li>为分隔符，对result2进行分割，获得一个数组，取左边得result3
        '''
        try:
            # print "    %s" % result.split('<li>')[1].rsplit('</li>')[0]
            # print result[0]
            if result[0] != r'<':
                # print result
                print result.decode('utf-8')  # 强制使用utf-8编码

        except:
            pass


def to_remove_blank(string):
    '''
    删除左右空格并将中间空格转换成为 '%20'
    :param string:  一个包含空格的字符串
    :return: 字符串
    '''
    return '%20'.join(string.strip(' ').split(' '))


def to_translate_phrase(args):
    '''
    :param argvs:  系统参数
    :return: 将参数列表转换为字符串并返回
    '''
    try:
        # print str(argvs)
        print "\n%s : " % ' '.join(args)
        # return '%20'.join(argvs)
        get_youdao('%20'.join(args))
        # get_youdao(args)
    except:
        pass


def to_translate_every_word(args):
    for word in args:
        print "\n%s : " % word
        get_youdao(word)


def to_switch(opts, args):
    try:
        # print opts
        # print args
        if len(opts) == 0:
            to_translate_phrase(args)
            sys.exit(0)
        if opts[0][0] in ('-s', '--split'):
            # print "opt is not none"
            to_translate_every_word(args)
            sys.exit(0)
    except:
        pass


if __name__ == "__main__":
    # sys.argv 是一个数组，包含文件本身所有变量。
    # py文件本身为sys.argv[0]

    # if len(sys.argv) == 2:
    #     word = sys.argv[1]
    #     print "%s : " % word
    # get_youdao(word)

    # get_youdao(to_remove_blank(word))

    # word = "go on"
    # get_youdao(to_remove_blank(word))

    # get_youdao(to_list2string(sys.argv))

    # to_translate_phrase(sys.argv)

    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s", "split")
        to_switch(opts, args)
        # print opts
        # print args
    except getopt.GetoptError, err:
        print err
