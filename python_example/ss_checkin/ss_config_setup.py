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
@FILE: py_setup_config.py
@time: 2016/8/7 11:19
"""

import os
import sys
import re

#################
json_tmpl_abs = 'gui-config.json.tmpl'
# json_setup_abs = 'gui-config.json'
if os.name == 'nt':
    json_setup_abs = r'E:\Documents\OneDrive\tools\shadowsocks-win-3.0\gui-config.json'
else:
    json_setup_abs = r'/mnt/e/Documents/OneDrive/tools/shadowsocks-win-3.0/gui-config.json'

localPort = 36363

# line pattern
remarks_patt = re.compile('\${remarks\}')
server_patt = re.compile('\${server\}')
server_port_patt = re.compile('\${server_port\}')
password_patt = re.compile('\${password\}')
method_patt = re.compile('\${method\}')
obfs_patt = re.compile('\${obfs\}')
protocol_patt = re.compile('\${protocol\}')

localPort_patt = re.compile('\${localPort\}')

# node block pattern
node_block_patt = re.compile(r'\[\[(.*)\]\]', flags=re.M + re.DOTALL)


def node_block_sub_line(line, node_info, user_info):
    line = remarks_patt.sub(node_info[0], line)
    line = server_patt.sub(node_info[1], line)
    line = method_patt.sub(node_info[2], line)
    line = protocol_patt.sub(node_info[3], line)
    line = obfs_patt.sub(node_info[4], line)
    line = server_port_patt.sub(user_info['ss_port'], line)
    line = password_patt.sub(user_info['ss_passwd'], line)

    return line


def setup_ss_json(user_info, nodes_info, json_path_name=json_setup_abs):
    #
    # 开始执行
    #
    print len(nodes_info)

    # 读取 模板 文件
    f = open(json_tmpl_abs, 'r')
    content = f.read()
    f.close()

    # 获取 node block 模板
    node_block_tmpl = node_block_patt.findall(content)

    nodes_block = ''
    for node_info in nodes_info:
        for line in node_block_tmpl:
            nodes_block += node_block_sub_line(line, node_info, user_info)
            nodes_block += '\n'

    content = node_block_patt.sub(nodes_block, content)

    ## line 其他配置
    content = localPort_patt.sub(str(localPort), content)
    # print content

    # 以UTF-8的模式写入文件
    import codecs
    # f = codecs.open(json_setup_abs, 'w', 'utf-8')
    f = codecs.open(json_path_name, 'w', 'utf-8')
    f.write(content)
    f.close()


if __name__ == '__main__':
    setup_ss_json(user_info, nodes_info)
