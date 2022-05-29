from .. import mailsender
from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException


def sendMail(to,subject, template, **kwargs):
    """
    Send a mail to a list of recipients.
    :param subject: Subject of the mail
    :param recipients: List of recipients
    :param template: Template to use
    :param kwargs: Arguments to pass to the template
    :return: True if the mail was sent successfully, False otherwise
    """
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    try:
        
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        result = mailsender.send(msg)
        return True
    except SMTPException:
        current_app.logger.error("Error sending mail")
        return False