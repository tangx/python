#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: octowahle@github
@software: PyCharm Community Edition
@file: python_arukas_api.py
@time: 2016/11/14 12:18
"""

"""
pip install qrcode
pip install Image
"""

# import os, sys
import base64
import qrcode
# 生成二维码还需要 Image 库
# import Image # 但此处不需要导入


def get_base64_encode(s):
    '''
        对字符串执行base64编码和解码
    '''

    # 编码
    # 不需要手动去除最后面的（占位符）等号，否则解码会出错
    # s_base64 = base64.b64encode(s).rstrip('=')  # 这是错的

    s_base64 = base64.b64encode(s)

    # 解码
    # s= base64.b64decode(s_encode)

    return s_base64


def gen_qrcode(s, image_name="pictname.png"):
    '''
        将字符串生成二维码
    '''

    # 创建对象,所有参数都有默认值。
    # qr=qrcode.QRCode()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )

    # 为对象添加数据
    qr.add_data(s)

    # 生成适应大小的图片
    qr.make(fit=True)  # 可以省略

    # 创建图片对象并保存
    img = qr.make_image()
    img.save(image_name)


if __name__ == "__main__":
    s = "i have a dream"
    s_encode = get_base64_encode(s)
    gen_qrcode(s)
