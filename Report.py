# coding=utf-8

import yagmail
import os

f = os.popen("python3 checkin.py", 'r')
res = f.readlines()
f.close()


receiver = os.environ['RCV']  # 要接收邮件的邮箱
body = res  # 邮件正文
filename = ""  # 要发送的附件

yag = yagmail.SMTP(
    user=os.environ['ACT'],  # 要发送邮件的邮箱，可以自己发送给自己
    password=os.environ['PWf'],  # 授权码
    host='smtp.163.com')

if "已经" in str(body):
    print("已填报，不发送")

else:
    yag.send(
        to=receiver,
        subject="打卡结果",  # 邮件标题
        contents=body)
    print("已发送邮件")

print("操作结束")
