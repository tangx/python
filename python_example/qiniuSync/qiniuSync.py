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
@file: qiniuSync.py
@time: 2016/12/1 14:44
"""

import os
import qiniu
import user_cfg

if os.name in ('nt', 'dos', 'ce'):
    from utils import _uri_encode_win32 as _uri_encode
    # import utils._uri_encode_win32  as _uri_encode
else:
    from utils import _uri_encode_posix as _uri_encode
    # import utils._uri_encode_posix  as _uri_encode


def _local_etag(f):
    return qiniu.etag(f)


def _remote_etag(key):
    ret, info = bucket.stat(bucket_name, key)

    # print ret.get('hash')
    try:
        # assert 'hash' in ret
        return ret.get('hash')
    except:
        return None


def _samefile(f):
    if _local_etag(f) == _remote_etag(f):
        # print "File %s is exist" % f
        return True
    else:
        # print "File %s is not exist" % f
        return False


def _samefile2(l_etag, r_etag):
    if l_etag == r_etag:
        return True
    else:
        return False


def _putfile(f, key):
    local_file = f
    token = auth.upload_token(bucket_name, key)

    ret, info = qiniu.put_file(token, key, local_file)

    r_etag = ret.get('hash')

    print "  Uploading %s -> %s ... " % (local_file, key),
    if r_etag == _local_etag(local_file):
        print "SUCCESS"
    else:
        print "FAILED"


def walk_path(path):
    # auth = qiniu.Auth(access_key, secret_key)
    # bucket = qiniu.BucketManager(auth)

    os.chdir(path)

    path = os.curdir
    for p_path, sub_paths, sub_files in os.walk(path):

        for sub_file in sub_files:
            # print os.path.join(p_path, sub_file)
            f = os.path.join(p_path, sub_file)

            # get file key in bucket
            if len(bucket_prefix) == 0:
                key = _uri_encode(f)
            else:
                key = "%s%s" % (bucket_prefix, _uri_encode(f))

            # check file is or not in bucket
            remote_etag = _remote_etag(key)
            local_etag = _local_etag(f)
            if remote_etag is None:
                print "File %s doesn't exist" % f
                _putfile(f, key)
            else:
                # _local_etag(f) == _remote_etag(f)
                if not local_etag == remote_etag:
                    print "File %s exists, but etag %s != %s " % (f, local_etag, remote_etag)
                    _putfile(f, key)
                else:
                    print "File %s already exists" % f


if __name__ == '__main__':

    bucket_prefix = ''
    access_key = user_cfg.access_key
    secret_key = user_cfg.secret_key
    bucket_name = user_cfg.bucket_name
    local_path = user_cfg.local_path

    try:
        bucket_prefix = user_cfg.bucket_prefix
    except:
        pass

    auth = qiniu.Auth(access_key, secret_key)
    bucket = qiniu.BucketManager(auth)

    walk_path(local_path)
