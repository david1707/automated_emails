import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line

# User configuration
sender_email = 'smtpforletslearnabout@gmail.com'
sender_name = 'David from LetsLearnAbout.net'
password = input('Please, type your password:\n')

receiver_emails = ['smtpforletslearnabout@gmail.com',
                   'smtpforletslearnabout@gmail.com', 'smtpforletslearnabout@gmail.com']
receiver_names = ['My Alter-ego',
                  'Karen from the gym', 'Kevin from the subway']

# Email body
email_html = open('email.html')
email_body = email_html.read()

filename = 'cat.gif'

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
    print("Sending the email...")
    # Configurating user's info
    msg = MIMEMultipart()
    msg['To'] = formataddr((receiver_name, receiver_email))
    msg['From'] = formataddr((sender_name, sender_email))
    msg['Subject'] = 'Hello, my friend ' + receiver_name
    msg.attach(MIMEText(email_body, 'html'))

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    msg.attach(part)

    try:
        # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Encrypts the email
        context = ssl.create_default_context()
        server.starttls(context=context)
        # We log in into our Google account
        server.login(sender_email, password)
        # Sending email from sender, to receiver with the email body
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent!')
    except Exception as e:
        print(f'Oh no! Something bad happened!\n {e}')
        break
    finally:
        print('Closing the server...')
        server.quit()
