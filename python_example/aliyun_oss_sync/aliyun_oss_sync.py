#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@python_version: python_x86 3.5.2
@site: octowahle@github
@software: PyCharm Community Edition
@file: aliyun_oss_sync.py
@time: 2016/12/2 10:29
"""

import os
import sys
import oss2
import hashlib

from user_cfg import *


def _local_etag(data):
    md5_hash = hashlib.md5(data).hexdigest()

    return md5_hash.upper()


def _remote_etag(key):
    try:
        result = bucket.get_object_meta(key)
        etag = result.etag

        return etag
    except:
        return None


def _put_file(key, data):
    print "Uploading ... ",

    try:
        bucket.put_object(key, data)
        print "Success!"
    except oss2.exceptions as err:
        print err
        print "Failed!"


def _uri_encode(f, pfix):
    f_list = f.split(os.path.sep)
    uri = '/'.join(f_list[1:])
    return "%s%s" % (pfix, uri)


def usage():
    print "Usage: aliyun_oss_sync.py -c config.json "


def walk_path(path):
    os.chdir(path)
    path = os.curdir

    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            f = os.path.join(dir_path, file_name)

            key = _uri_encode(f, bucket_prefix)

            with open(f, 'rb') as f_obj:
                data = f_obj.read()
                remote_etag = _remote_etag(key)
                local_etag = _local_etag(data)

                if remote_etag is None:
                    print "File: %s doesn't exist. -> " % f,
                    _put_file(key, data)
                    continue

                if remote_etag == local_etag:
                    print "File: %s already exists -> skip" % f
                    continue
                else:
                    print "File: %s exists, but etag '%s' != '%s'. -> " % (f, local_etag, remote_etag),
                    _put_file(key, data)


if __name__ == '__main__':

    # run function
    try:
        auth = oss2.Auth(access_key, secret_key)
        bucket = oss2.Bucket(auth, endpoint, bucket_name)
        walk_path(local_path)

    except Exception as err:
        print err
        usage()
        sys.exit(1)
