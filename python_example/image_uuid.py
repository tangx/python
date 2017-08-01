#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: image_uuid.py
@time: 2017/8/1 14:47
"""

import os
import sys
import uuid
from base64 import b64encode

PYTHON_VER = sys.version_info.major

ENCODING = 'utf-8'

class ImageUUID(object):
    def __init__(self, imagefile):
        self.imagefile = imagefile

    @property
    def uuid(self):
        with open(self.imagefile, 'rb') as data_obj:
            data_content = data_obj.read()
            date_base64_bytes = b64encode(data_content)
            # print(date_base64_bytes)
            if PYTHON_VER == 2:
                return uuid.uuid3(uuid.NAMESPACE_X500, date_base64_bytes.encode(ENCODING))
            elif PYTHON_VER == 3:
                return uuid.uuid3(uuid.NAMESPACE_X500, date_base64_bytes.decode(ENCODING))


if __name__ == '__main__':
    image = ImageUUID('005DO33Hly1fhr7flzt6bj30qu0l4ds8.jpg')
    print(image.uuid)
