import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import body_html

class SendEmail:
    def __init__(self, email, nome):
        self.subject_sgc = 'Recrutamento Guild Fury'
        self.sender = 'bot126997@gmail.com'
        self.recipients = email
        self.nome = nome
        self.pwd = 'jlul ndyv vtcd omhg'


    def send_email(self):
        body = body_html.html(self.nome)

        msg = MIMEMultipart()
        msg['subject'] = self.subject_sgc
        msg['From'] = self.sender
        msg['To'] = ', '.join([self.recipients,'devlucaseduardosilva@gmail.com'])

        text_part = MIMEText(body, 'html')
        msg.attach(text_part)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.pwd)
            smtp_server.sendmail(self.sender, self.recipients, msg.as_string())
