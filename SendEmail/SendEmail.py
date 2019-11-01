import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import getpass

email_user = input("Email address to send from:\n")

email_domain = email_user.split("@")[1]

if email_domain in ["outlook.com", "hotmail.com"]:
    smtpserver = "smtp.live.com:587"  # Kludge for hotmail/outlook addresses
else:
    smtpserver = "smtp." + email_domain + ":587"  # Guess for SMTP server; works for gmail, yahoo etc.

to_addr = input("Address to send to:\n")

subject = input("What is your email subject?\n")

body_text = input("What message did you want to email? (currently this is only one line)\n\n")

body_html= """\
<html>
  <head></head>
  <body>
  <h1>I sent this email automatically, using Python!</h1>
  <p>
  """

body_html += body_text

body_html += """</p>
  </body>
</html>
"""

def send_mail(to_addr, subject="Test email",
              body_text="Test message",
              body_html="Test message",
              from_addr=email_user, email_user=email_user,
              email_passwd=email_passwd,
              smtpserver="smtp.live.com:587"):
    """A function to send email, in MIME multi-part (plain-text and HTML).

    For example: to send to myself:
    send_mail(to_addr, subject, body_text=body_text, body_html=body_html)
    """

    # Construct the message header
    message = MIMEMultipart('alternative')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = subject

    # Append the body text
    message.attach(MIMEText(body_text, 'plain'))
    message.attach(MIMEText(body_html, 'html'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(email_user, email_passwd)
    problems = server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()


email_passwd = getpass.getpass()

send_mail(to_addr, subject, body_text, body_html, email_user, email_user, email_passwd, smtpserver)
