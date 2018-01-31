import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_success_Email(content,client_email):

    # string to store the body of the mail

    s = smtplib.SMTP('smtp.gmail.com', 587)


    # start TLS for security
    s.starttls()
    fromaddr = "popgenoncloud@gmail.com"

    fromPassword = "kaka12345"
    # Authentication
    s.login(fromaddr, fromPassword)




    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = client_email
    msg['Subject'] = "Your Popgen result "

    body = "https://s3.amazonaws.com/pogen-upload/"+str(content)
    body = body+'\n This file be deleted after 48 hours from the time you have recieved this email.'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, fromPassword)
    text = msg.as_string()
    server.sendmail(fromaddr, client_email, text)
    server.quit()



def send_Error_Email(path,client_email):
    fromaddr = "popgenoncloud@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = client_email

    # storing the subject
    msg['Subject'] = "There was an error in your Popgen File"

    # string to store the body of the mail
    body = "There was an error please see the attached log file or check your Yaml file again"
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    attachment = open(path, "rb")

    filename = str(path).split("/")
    filename = filename[len(filename) - 1]

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded formg
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "kaka12345")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, client_email, text)

    # terminating the session
    s.quit()