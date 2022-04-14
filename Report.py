import yagmail
import os

receiver = os.environ['RCV'] #要接收邮件的邮箱
body = os.environ['BODY'] #邮件正文
filename = "" #要发送的附件

yag = yagmail.SMTP(
user=os.environ['USR'],#要发送邮件的邮箱，可以自己发送给自己
password=os.environ['PWD'],#授权码
host = 'smtp.163.com')

yag.send(
    to=receiver,
    subject=os.environ['TITLE'],#邮件标题
    contents=body)
