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

# 2016-12-05
  + add cdn refresh log  in put_files function.
    + like cdn_refresh_2016-12-02_19-37.log
    + module at cdn_refresh_log_obj
  + add get_files fuction.
"""

import os
import sys
import oss2
import hashlib
import datetime

from user_cfg import *


def _local_etag(data):
    md5_hash = hashlib.md5(data).hexdigest()

    # print "line 28: %s" % md5_hash
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
        return None
    except oss2.exceptions as err:
        print err
        print "Failed!"
    print "Failed!"


def _get_file(key):
    print "Downloading ... ",
    try:
        file_obj = bucket.get_object(key)

        # remove the prefix in key
        if "remove_prefix" is True:
            key = '/'.join(key.split('/')[1:])

        # f = open(key, 'wb')
        # f.write(file_obj.read())
        # f.close()

        with open(key, 'wb') as f:
            f.write(file_obj.read())

        print "Success!"
    except oss2.exceptions as err:
        print err
        print "Failed!"


def _uri_encode(f, pfix):
    f_list = f.split(os.path.sep)
    uri = '/'.join(f_list[1:])
    return "%s%s" % (pfix, uri)


def usage():
    print "Usage: aliyun_oss_sync.py [get|put] -c config.json "
    sys.exit(1)


def put_files(path):
    # log file for cdn refresh
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    cdn_refresh_log = 'cdn_refresh_%s.log' % dt
    cdn_refresh_log_obj = open(cdn_refresh_log, 'w+')

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

                    cdn_refresh_url = "http://%s/%s" % (cdn_domain, key)
                    cdn_refresh_log_obj.write(cdn_refresh_url)

    cdn_refresh_log_obj.close()


def get_files(path):

    os.chdir(path)
    list_obj = bucket.list_objects(bucket_prefix)
    obj_list = list_obj.object_list

    for obj in obj_list:

        # print dir(obj) # "'etag', 'is_prefix', 'key', 'last_modified', 'size', 'storage_class', 'type'"
        key = obj.key

        if os.path.exists(key) is True:

            remote_etag = obj.etag
            with open(key, 'rb') as data:
                local_etag = _local_etag(data.read())

                if local_etag == remote_etag:
                    print "File %s exists -> skip" % key
                    continue
                else:
                    print "File %s exists, but etag %s != %s -> " % (key, local_etag, remote_etag),
                    _get_file(key)
        else:

            # file_name = os.path.basename(key)
            dir_name = os.path.dirname(key)

            if os.path.exists(dir_name) is False:
                os.makedirs(dir_name)

            print "File %s doesn't exist -> " % key,
            _get_file(key)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        usage()

    action = sys.argv[1]

    # run function
    try:
        auth = oss2.Auth(access_key, secret_key)
        bucket = oss2.Bucket(auth, endpoint, bucket_name)

        if action == 'get':
            get_files(local_path)
        elif action == 'put':
            put_files(local_path)
        else:
            usage()

    except Exception as err:
        print err
        usage()
