import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr

# User configuration
sender_email = 'smtpforletslearnabout@gmail.com'
sender_name = 'David from LetsLearnAbout.net'
password = input('Please, type your password:\n')

# receiver_email = 'smtpforletslearnabout@gmail.com'
# receiver_name = 'My Alter-ego'
receiver_emails = ['smtpforletslearnabout@gmail.com',
                   'smtpforletslearnabout@gmail.com', 'smtpforletslearnabout@gmail.com']
receiver_names = ['My Alter-ego', 'Karen from the gym', 'Kevin from the subway']

# Email text
email_body = '''
	This is a test email sent by Python. Isn't that cool?
'''


def send_email(sender_email, sender_name, password, receiver_email, receiver_name):
    print(f'Sending an email to {receiver_name}...')

    # Configurating user's info
    msg = MIMEText(email_body, 'plain')
    msg['To'] = formataddr((receiver_name, receiver_email))
    msg['From'] = formataddr((sender_name, sender_email))
    msg['Subject'] = 'Hello, my friend ' + receiver_name

    try:
        # 587 with TLS, 465 SSL and 25
        server = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print('Email sent!')
    except Exception as e:
        print(f'Oh no! Something bad happened!\n {e}')
    finally:
        print('Closing the server...')
        server.quit()


if __name__ == "__main__":
    for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
        send_email(sender_email, sender_name, password,
                   receiver_email, receiver_name)
