import smtplib, ssl


"""
  Simple email sender

  No configuration, no MIMEText, plain text email
"""


# User configuration
sender_email = 'smtpforletslearnabout@gmail.com'
receiver_email = 'smtpforletslearnabout@gmail.com'
password = input('Please, type your password:\n')

# Email text
email_text_sent = '''
  This is a test email sent by Python. Isn't that cool?
'''


def send_email():
	print("Sending the email...")
    try:
        # 587 with TLS, 465 SSL and 25
        server = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_text_sent)

        print('Email sent!')
    except Exepction as e:
        print(f'Oh no! Something bad happened!\n {e}')
    finally:
        print('Closing the server...')
        server.quit()


if __name__ == "__main__":
    send_email()
