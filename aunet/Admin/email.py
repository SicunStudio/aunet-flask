# -*-coding:utf-8 -*-
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from aunet import mail,app

MAIL=app.config['MAIL']


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
#subject:主题,recipients:收件人列表list type，text_body：内容；sender:发件人，默认为配置中的发件人
def send_email(subject, recipients, text_body):
    msg = Message(subject, sender=MAIL, recipients=recipients)
    msg.html = text_body
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()




