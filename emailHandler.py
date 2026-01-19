import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import EMAIL, EMAIL_APP_PASSWORD, RECIEVER_EMAIL, SEND_EMAIL_NOTIFICATION





def send_email(ErrorText:str):
    if SEND_EMAIL_NOTIFICATION == True:
        subject = "GFS Backup Failed!"
        message = "Check setup to see what went wrong. Got error: \n " + ErrorText
        text = f"Subject: {subject}\n\n{message}"

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(EMAIL, EMAIL_APP_PASSWORD)
        server.sendmail(EMAIL, RECIEVER_EMAIL, text)
        print("Sent Email!")