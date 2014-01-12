import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to,subject,body):

    #Log into Email Server
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login("gentle.effects@outlook.com", "Thomas84")

    fromaddr = "gentle.effects@outlook.com"
    toaddr = to
    bccaddr = "{0}, ".format("gentle.effects@outlook.com")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Bcc'] = bccaddr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.sendmail(fromaddr, bccaddr, msg.as_string())
