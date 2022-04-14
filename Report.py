import yagmail

receiver = "facionia@outlook.com" #要接收邮件的邮箱
body = "Hello there from Yagmail" #邮件正文
filename = "" #要发送的附件

yag = yagmail.SMTP(
user='testfromfairyland@163.com',#要发送邮件的邮箱，可以自己发送给自己
password=,#授权码
host = 'smtp.163.com')

yag.send(
    to=receiver,
    subject="Yagmail test with attachment",#邮件标题
    contents=body)
