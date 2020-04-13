import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
from pdf import *
import ssl
import smtplib
import os
from pdf import *

def email_generator(movie):
    subject = "Requested Movie report"
    body = "Movie report"
    sender_email = "diegoflorezestrada@gmail.com"
    receiver_email = input("Enter your email address to send you the report: ")
    password = getpass.getpass("Type your password and press enter:")
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject


    # Create the plain-text and HTML version of your message
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        Below you will find your requested info about the movie.<br>
        Also if you want more info, you can visit:<br>
        <a href="https://www.imdb.com">IMDB</a> 
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)


    # Add body and file to email
    message.attach(MIMEText(body, "plain"))
    pdf = FPDF()
    pdf = pdf_generator(pdf)
    filename = "../OUTPUT/report.pdf"
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    return print("Email sent to {}".format(receiver_email))