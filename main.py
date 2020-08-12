import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
# for sending mail
email = input('email:')
password = input('password:')
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = 'Sumit'
msg['To'] = 'sumitkrpradhan.mec18@itbhu.ac.in'
msg['subject'] = 'A text from python server'
message = 'Hello User, It is a server generated message from python'
msg.attach(MIMEText(message, 'plain')) # attaching header

# sending message
filename = 'img.jpg'
attachment = open(filename, 'rb') # reading in binary

# creating payload
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)

# attaching payload
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(email, 'sumitkrpradhan.mec18@itbhu.ac.in', text)

