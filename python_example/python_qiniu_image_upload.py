#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  ??
@author: TangHsin
@license: Apache Licence
@mailto: octowhale@github
@site: 
@software: PyCharm Community Edition
@python ver: Python 2.7.12
@FILE: python_qiniu_image_upload.py
@time: 2016/11/10 21:01
"""

import os
import sys
import imghdr
import hashlib
import sqlite3

# pip install qiniu
import qiniu

'''
上传图片到七牛容器
并返回对应的URL

'''


class QiniuUpload:
    access_key = ''
    secret_key = ''
    bucket_name = ''
    bucket_url = ''
    image_prefix = ""

    image = ''
    image_md5sum = ""
    image_type = ""
    image_name = ''

    db_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    db_name = os.path.join(db_path, 'image.db')

    def get_image_name(self):
        self.image_name = os.path.basename(self.image)
        # print self.image_name

    def get_exist(self):
        '''检查文件是否存在'''
        if not os.path.exists(self.image):
            print "Error: 文件 ( %s ) 不存在。 " % self.image
            sys.exit(10)

    def get_md5sum(self):
        '''获取文件md5码，作为上传文件名，以及数据库主键'''

        f = open(self.image, 'rb').read()
        md5sum = hashlib.md5(f).hexdigest()
        self.image_md5sum = md5sum
        return md5sum

    def get_type(self):
        '''获取图片类型'''

        type_value = imghdr.what(self.image)
        if type_value is not None:
            self.image_type = type_value
            # return type_value
        else:
            print 'Error: 文件 ( %s )不是图片' % self.image
            sys.exit(9)

    def to_connect_qiniu_image_database(self):
        '''
            连接数据库
            如果没有则创建数据库及表
        '''

        # 如果数据库文件不存在，则创建
        # if not os.path.exists(self.db_name):
        # print self.db_name
        cx = sqlite3.connect(self.db_name)
        cursor = cx.cursor()
        try:
            sql = "create table qiniu_image_url ( image_md5sum varchar(32) primary key, image_type varchar(4), image_prefix varchar(50))"
            cursor.execute(sql)
            cx.commit()
            cx.close()
        except:
            pass

        cx = sqlite3.connect(self.db_name)
        cursor = cx.cursor()
        # return cursor
        return [cursor, cx]

    def to_select_image_database(self, cursor):
        '''
        查看文件是否已经存在于数据库中，如果存在则直接返回七牛URL
        :param cursor: 数据库连接指针
        :return: 七牛URL
        '''
        sql = "select * from qiniu_image_url where image_md5sum='%s'" % self.image_md5sum
        # cx = sqlite3.connect(self.db_name)
        # cursor = cx.cursor()
        try:
            # print sql
            cursor.execute(sql)
            r = cursor.fetchall()
            if len(r) == 1:
                # abs_url = "http://%s/%s%s.%s" % (self.bucket_url, r[0][-1], r[0][0], r[0][1])
                # print 'Success: file "%s" is already exist' % self.image
                # print abs_url
                # return abs_url
                self.to_print_urls(r[0])
                return r[0]
        except:
            pass

    def to_print_urls(self, the_tuple):
        '''
        按照格式打印输出
        :param the_tuple:  数据库中的图片信息 [image_md5sum,image_type,image_prefix_url]
        :return: None
        '''

        abs_url = "http://%s/%s%s.%s" % (self.bucket_url, the_tuple[-1], the_tuple[0], the_tuple[1])
        
        print abs_url  # qiniu abs_url
        print "![%s](%s)" % (self.image_name, abs_url)  # markdown
        print '<img src="%s">%s</img>' % (abs_url, self.image_name)  # html

    def to_update_image_database(self, cursor, cx):
        '''
        插入成功后更新数据库，并返回七牛URL
        :param cursor: 数据库指针
        :param cx:      数据库实例
        :return:    通过to_select_image_database()返回七牛URL
        '''
        sql = "insert into qiniu_image_url values ('%s','%s','%s')" % (
            self.image_md5sum, self.image_type, self.image_prefix)
        # print sql
        try:
            cursor.execute(sql)
            cx.commit()  # 提交到数据库
            # cx.close()
            self.to_select_image_database(cursor)
        except:
            pass

    def to_upload_image_to_qiniu(self):
        '''
        上传文件到七牛仓库
        :return: 成功或失败
        '''
        try:
            # print self.image_prefix
            # print 'md5' + self.image_md5sum
            # print self.image_type
            # print '开始上传'
            q = qiniu.Auth(self.access_key, self.secret_key)
            key = "%s%s.%s" % (self.image_prefix, self.image_md5sum, self.image_type)

            # print key
            token = q.upload_token(self.bucket_name, key)

            qiniu.put_file(token, key, self.image)
            # self.to_update_image_database(self.cursor)
            return True
        except:
            return False

    def get_url(self):
        '''
        @breif : main 方法
        :return:
        '''
        self.get_image_name()
        # 检查文件是否存在
        self.get_exist()

        # 获取图片 type
        self.get_type()

        # 获取 图片 md5
        self.get_md5sum()

        # 连接数据库
        cursor, cx = self.to_connect_qiniu_image_database()

        # 检查图片是否已经上传到七牛
        if self.to_select_image_database(cursor) is not None:

            cx.close()
            sys.exit()
            pass

        # 之前没有上传
        elif self.to_upload_image_to_qiniu():
            self.to_update_image_database(cursor, cx)
            # self.to_select_image_database(cursor)

            # cursor.close()
            cx.commit()
            cx.close()


if __name__ == "__main__":
    image = r'C:\Users\owners\Desktop\PNG\loading_logo.png'

    import user_auth

    qr_upload = QiniuUpload()
    qr_upload.access_key = user_auth.accKey
    qr_upload.secret_key = user_auth.secKey
    qr_upload.bucket_name = user_auth.bucketName
    qr_upload.bucket_url = user_auth.bucketUrl
    qr_upload.image_prefix = ''
    qr_upload.image = image

    qr_upload.get_url()
