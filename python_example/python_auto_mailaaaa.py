#!/usr/bin/python
#coding:utf-8
# author: QQ 群友
#
import urllib, urllib2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import time
import os
os.chdir('/data/application/tomcat-transnwe/bin/logs/')


mail_host = 'smtp.163.com'  
mail_user = '*********@163.com'   #邮箱账号
mail_pass = '*******'             #邮箱密码
mail_postfix = '163.com'
#以上内容根据你的实际情况进行修改

def send_mail(to_list,subject,content,log_path,log_name):
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"

    msg = MIMEMultipart()                       #用于发送多个类型
    msg['Subject'] = subject                    #邮件主题
    msg['From'] = '***********@163.com'
    msg['to'] = to_list                         #发送给谁，抄送
    
    
    # 下面是文字部分，也就是纯文本
    log_test = MIMEText(content)                #邮件文本
    msg.attach(log_test)  
    
    # 首先是log类型的附件
    logpart = MIMEApplication(open(log_path, 'rb').read())
    logpart.add_header('Content-Disposition', 'attachment', filename=log_name)
    msg.attach(logpart)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == "__main__":
    
    times = datetime.date.today() - datetime.timedelta(days=1)
    time_str = times.strftime('%Y-%m-%d')
    
    log_path = '/data/application/tomcat-transnwe/bin/logs/' + time_str + '_errlr_log.tgz' 
    log_name = time_str + '_errlr_log.tgz'
    shells =  ' wetransn_' + time_str + '*error.log'
    num = os.popen('ls wetransn_' + time_str + '*error.log | wc -l').read()
    title = time_str + '_woordee_error'
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    
    if int(num) > 0:
        err = os.system('tar zcvf ' + log_name + shells)

        filename = r'/data/application/tomcat-transnwe/bin/logs/%s' %(log_name)
        if not os.path.isfile(filename) :
            print '附件路径：' + log_path + '不存在'

        print '附件路径：' + log_path
        if err > 0 : exit()
            
        send_mail('riven.dong@transn.com', title , date , log_path , log_name)
        
        os.system('rm -rf ' + filename)     
#	收件人地址、主题、详细内容、附件路径、附件name        
    else: 
        print '没有日志记录'
        exit()
