import pyautogui
import time
import getpass
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

sender_email = input("Enter email to send from: ")
password = getpass.getpass("Enter password: ")
smtp_server = input("Enter smtp server: ")
smtp_port = int(input("Enter smtp port: "))
send_to = input("Enter email to send screenshot to: ")
sleep_time = int(input("Enter interval (seconds): "))

while True:
    try:
        filename = str(time.time()).split(".")[0] + ".png"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

        subject = "Hourly screenshot"
        body = str(datetime.now())

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = send_to
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with open(filename, "rb") as attachment:
            part = MIMEBase("image", "png")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, send_to, text)

        print("EMAIL SENT SLEEPING FOR AN HOUR NOW")
        time.sleep(3600)

    except KeyboardInterrupt:
        exit()    
    
    except Exception as e:
        print(e)