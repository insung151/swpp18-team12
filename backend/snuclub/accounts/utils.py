from django.core.mail import EmailMessage
from .tokens import account_activation_token, password_forgot_token
from django.template.loader import render_to_string


def send_verification_mail(username, email, domain):
    mail_subject = 'Activate your snuclub account.'
    message = render_to_string('acc_active_email.html', {
        'username': username,
        'domain': domain,
        'token': account_activation_token.make_token(username),
    })
    to_email = email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


def send_password_reset_mail(username, email, domain):
    mail_subject = 'Change your password'
    message = render_to_string('forgot_password_email.html', {
        'username': username,
        'domain': domain,
        'token': password_forgot_token.make_token(username),
    })
    to_email = email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()