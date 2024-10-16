import json
import os
import smtplib
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

url = '127.0.0.1:5700'

def getToken():
    if os.path.isfile('/ql/config/auth.json'):
        with open('/ql/config/auth.json', 'r') as f:
            config = json.load(f)
            return 'Bearer ' + config['token']


def 保存文件(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


def 备份订阅信息():
    newUrl = f"http://{url}/open/subscriptions"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers).json()
    if rj['code'] == 200:
        保存文件('subscription.json', rj)


def 备份环境变量():
    newUrl = f"http://{url}/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers).json()
    if rj['code'] == 200:
        保存文件('envs.json', rj)


def 备份依赖():
    newUrl = f"http://{url}/open/dependencies"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers, params={'type': 'python3'}).json()
    if rj['code'] == 200:
        保存文件('dependencies-python3.json', rj)

    rj = sec.get(newUrl, headers=headers, params={'type': 'nodejs'}).json()
    if rj['code'] == 200:
        保存文件('dependencies-nodejs.json', rj)


def 邮箱发送文件():
    # 邮件服务器的信息
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # 发件人、收件人和主题
    from_email = smtp_username
    to_email = smtp_username
    subject = f"青龙备份-{time.strftime('%Y-%m-%d', time.localtime())}"

    # 创建一个带附件的邮件
    message = MIMEMultipart()

    message["From"] = Header(from_email)
    message["To"] = Header(to_email)
    message["Subject"] = Header(subject, 'utf-8')

    # 邮件正文
    with open('subscription.json', "rb") as attachment_file:
        attachment = MIMEApplication(attachment_file.read(), Name="subscription.json")
        attachment.add_header("Content-Disposition", "subscription.json", filename="subscription.json")
        message.attach(attachment)

    with open('dependencies-nodejs.json', "rb") as attachment_file:
        attachment = MIMEApplication(attachment_file.read(), Name="dependencies-nodejs.json")
        attachment.add_header("Content-Disposition", "dependencies-nodejs.json", filename="dependencies-nodejs.json")
        message.attach(attachment)

    with open('dependencies-python3.json', "rb") as attachment_file:
        attachment = MIMEApplication(attachment_file.read(), Name="dependencies-python3.json")
        attachment.add_header("Content-Disposition", "dependencies-python3.json", filename="dependencies-python3.json")
        message.attach(attachment)

    with open('envs.json', "rb") as attachment_file:
        attachment = MIMEApplication(attachment_file.read(), Name="envs.json")
        attachment.add_header("Content-Disposition", "envs.json", filename="envs.json")
        message.attach(attachment)


    # 连接到SMTP服务器并发送邮件
    try:
        smtpObj = smtplib.SMTP(smtp_server)
        # smtpObj.set_debuglevel(1)
        smtpObj.login(smtp_username, smtp_password)
        smtpObj.sendmail(from_email, [to_email], message.as_string())
        print("SEND EMAIL SUCCESS")
    except smtplib.SMTPException:
        print("SEND EMAIL FAIL")


if __name__ == '__main__':
    # print(getToken())
    备份订阅信息()
    备份环境变量()
    备份依赖()
    邮箱发送文件()