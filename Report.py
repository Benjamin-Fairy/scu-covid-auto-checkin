import yagmail
import os

receiver = "facionia@outlook.com" #要接收邮件的邮箱
body = "test" #邮件正文
filename = "" #要发送的附件

yag = yagmail.SMTP(
user="testfromfairyland@163.com",#要发送邮件的邮箱，可以自己发送给自己
password= str(os.environ["PWD"]),#授权码
print(os.environ["PWD"])
host = 'smtp.163.com')

yag.send(
    to=receiver,
    subject="打卡结果",#邮件标题
    contents=body)

