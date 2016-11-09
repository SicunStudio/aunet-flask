from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from aunet import mail,app

MAIL=app.config['MAIL']


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, recipients, html):
    recipients=list(recipients)
    msg = Message(subject, sender=MAIL, recipients=recipients)
    #msg.body = text_body
    msg.html=html
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()



