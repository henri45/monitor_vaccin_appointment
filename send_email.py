import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
email_info = config_object["EMAIL"]

MY_ADDRESS = email_info["my_address"]
PASSWORD = email_info["password"]
EMAIL_DESTINATION = email_info["email_destination"]


def send_email():
    host = "smtp.live.com"
    # set up the SMTP server
    s = smtplib.SMTP(host=host, port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = "Nouveau RDV pour se faire vacciner !"

    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = EMAIL_DESTINATION
    msg['Subject'] = "NOUVEAU RDV POUR VACCIN !"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
