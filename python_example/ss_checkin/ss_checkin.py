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
@FILE: pyspider_s3_feng666.py.py
@time: 2016/8/6 23:12
"""

import os
import sys

import cookielib
import urllib, urllib2
import re


def get_opener():
    cj = cookielib.CookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    # opener = urllib2.build_opener(cookie_support, urllib2.HTTPSHandler, urllib2.HTTPSHandler)
    opener = urllib2.build_opener(cookie_support)
    opener.add_handler(urllib2.HTTPSHandler())
    opener.add_handler(urllib2.HTTPHandler())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        # 'X-Forwarded-For': '171.212.113.133',  # 伪装IP地址
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Content-Type': 'application/html',
    }

    header_list = []
    for key, value in headers.items():
        header_list.append((key, value))

    opener.addheaders = header_list

    return opener


def do_login(username, password):
    loginURI = 'auth/login'
    loginInfo = {
        'email': username,
        'passwd': password,
        'code': '',
        'remember_me': 'week',
    }
    login_paras = urllib.urlencode(loginInfo)
    opener = get_opener()

    try:
        print 'use https'
        loginURL = 'https://%s/%s' % (hostname, loginURI)
        # resp = urllib2.urlopen(loginURL, login_paras, timeout=3)
        resp = opener.open(loginURL, login_paras, timeout=3)
        data = resp.read()
        print data
        if data == '{"ret":1,"msg":"\u6b22\u8fce\u56de\u6765"}':
            return {
                'http_type': 'https',
                'opener': opener,
            }
    except Exception as err:
        print err

    try:
        print 'use http'
        loginURL = 'http://%s/%s' % (hostname, loginURI)
        resp = opener.open(loginURL, login_paras, timeout=3)
        data = resp.read()
        print data
        if data == '{"ret":1,"msg":"\u6b22\u8fce\u56de\u6765"}':
            return {
                'http_type': 'http',
                'opener': opener,
            }
    except Exception as err:
        print err


def do_checkin(opener, http_type):
    checkinURI = 'user/checkin'
    checkinURL = "%s://%s/%s" % (http_type, hostname, checkinURI)

    try:
        # 签到
        resp = opener.open(checkinURL, '')
        print resp.read()
    except:
        pass


def get_ss_node_info(content):
    # print type(content)
    content = content.decode('utf8')
    # server_str = u'\<div.*?\<a.*?\>([\d\w\uff0c\u4e00-\u9fff]+-SS)\<\/a\>.*?\<p\>地址：\<span.*?(\d+\.\d+\.\d+\.\d+).*?\<\/span\>\<\/p\>.*?\<p\>加密方式：\<span.*?\t([\w\d-]+).*?\<p\>协议：\<span.*?\t(\w+).*?\<p\>混淆方式：\<span.*?\t(\w+).*?'
    # server_str = u'\<div.*?\<a.*?\>([\d\w\uff0c\u4e00-\u9fff]+-SS)\<\/a\>.*?\<span class=\"label label-green\"\>OK\<\/span\>.*?\<p\>地址：\<span.*?(\d+\.\d+\.\d+\.\d+).*?\<\/span\>\<\/p\>.*?\<p\>加密方式：\<span.*?\t([\w\d-]+).*?\<p\>协议：\<span.*?\t(\w+).*?\<p\>混淆方式：\<span.*?\t(\w+).*?'
    server_str = u'\<span class=\"icon text-green\"\>backup\<\/span\>.*?\<div.*?\<a.*?\>([\d\w\uff0c\u4e00-\u9fff]+-SS)\<\/a\>.*?\<p\>地址：\<span.*?(\d+\.\d+\.\d+\.\d+).*?\<\/span\>\<\/p\>.*?\<p\>加密方式：\<span.*?\t([\w\d-]+).*?\<p\>协议：\<span.*?\t(\w+).*?\<p\>混淆方式：\<span.*?\t(\w+).*?'

    server_patt = re.compile(server_str, flags=re.DOTALL + re.MULTILINE)
    nodes_info = server_patt.findall(content)

    print nodes_info
    return nodes_info


def get_ss_user_info(content):
    ss_port_str = '\<dt\>端口\</dt\>.*\<dd\>(\d+?)\</dd\>'
    ss_port_patt = re.compile(ss_port_str, flags=re.MULTILINE + re.DOTALL)

    pwd_str = '\<dt\>密码\</dt\>.*\<dd\>([\d\w\s]+?)\</dd\>'
    pwd_patt = re.compile(pwd_str, flags=re.MULTILINE + re.DOTALL)

    ss_passwd = pwd_patt.findall(content)
    ss_port = ss_port_patt.findall(content)

    user_info = {
        'ss_port': ss_port[0],
        'ss_passwd': ss_passwd[0],
    }

    return user_info


def do_setup_json(opener, http_type):
    userURL = '%s://%s/user' % (http_type, hostname)
    nodeURL = '%s://%s/user/node' % (http_type, hostname)

    user_info = get_ss_user_info(opener.open(userURL).read())
    nodes_infos = get_ss_node_info(opener.open(nodeURL).read())

    import ss_config_setup
    ss_config_setup.setup_ss_json(user_info, nodes_infos)


def main(username, password):
    login_stat = do_login(username, password)

    http_type = login_stat['http_type']
    opener = login_stat['opener']

    do_checkin(opener, http_type)  # 签到
    # do_setup_json(opener, http_type)  # 生成当日服务器列表


if __name__ == '__main__':
    try:
        import user_cfg
    except ImportError as err:
        print err

    main(username, password)
