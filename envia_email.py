import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import body_html

class SendEmail:
    def __init__(self, email, nome, classe):
        self.subject_sgc = 'Recrutamento Guild Fury'
        self.sender = 'staff.fury@guildfury.com.br'
        self.recipients = email
        self.nome = nome
        self.classe = classe
        self.pwd = 'D49e4SXUbaaG'


    def send_email(self):
        body = body_html.html(self.nome, self.classe)

        msg = MIMEMultipart()
        msg['subject'] = self.subject_sgc
        msg['From'] = self.sender
        msg['To'] = ', '.join([self.recipients])

        text_part = MIMEText(body, 'html')
        msg.attach(text_part)
        
        attachment_path = os.path.join('pdf/', f'respostas_form_{self.nome}.pdf')

        with open(attachment_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), Name=attachment_path.split('/')[-1])
        attachment['Content-Disposition'] = f'attachment; filename="{attachment_path.split("/")[-1]}"'
        msg.attach(attachment)

        with smtplib.SMTP_SSL('smtp.zoho.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.pwd)
            smtp_server.sendmail(self.sender, self.recipients, msg.as_string())
            
        os.remove
