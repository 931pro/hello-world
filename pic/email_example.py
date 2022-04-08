# coding:utf-8
# sys.setdefaultencoding('utf8')
import smtplib
import time

from email6.mime.text import MIMEText
from email6.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send():
    # 发送者的登陆用户名和密码
    user = '3357211768@qq.com'
    password = 'liujie&931'
    #接收者的邮箱
    receiver = ['2812154885@qq.com']  #    receiver 可以是一个list
    #秘钥
    auth_pwd='yxcfgdqazjazdaed'
    # 构造邮件内容
    msg = MIMEMultipart('related')
    msg['Subject']='python邮件测试'#邮件主题
    msg['From']=user   #发件人
    msg['To']=";".join(receiver)
    #正文内容
    text=MIMEText('<html><body><p>这是今天的推送，请查收！</p><img src="cid:imageid"></img></body></html>','html','utf-8')
    msg.attach(text)
    #插入图片
    filename='./output/{}.png'.format(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file = open(filename, "rb")
    img_data = file.read()
    file.close()
    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    msg.attach(img)

    # 发送者邮箱的SMTP服务器地址
    smtpserver = 'smtp.qq.com'
    try:
        smtp = smtplib.SMTP()  # 实例化SMTP对象
        smtp.connect(smtpserver, 25)  # （缺省）默认端口是25 也可以根据服务器进行设定
        smtp.login(user,auth_pwd)  # 登陆smtp服务器
        smtp.sendmail(user, receiver, msg.as_string())  # 发送邮件 ，这里有三个参数
        result='发送成功！当前时间为{}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print(result)
        smtp.quit()
        '''
        login()方法用来登录SMTP服务器0000000000000000000000000，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文
        是一个str，as_string()把MIMEText对象变成str。
        '''
    except:
        result = '发送失败！当前时间为{}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print(result)
        smtp.quit()

