import email, smtplib, ssl
import os
import cv2
import threading
import io
import imghdr
import RPi.GPIO as GPIO
import picamera
import subprocess
import camerae
from email.message import EmailMessage
from time import sleep
from time import strftime
from os import system
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send():

    file1 = "/home/pi/supinger/images/product/angle1.gif"
    file2 = "/home/pi/supinger/images/product/angle2.gif"

    subject = "New suspect"
    body = "This suspect has been detected by Supinger™"
    sender = "pigger.pinger@gmail.com"
    password = "jtntretaejqaisab"

    # headers
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = sender
    message["Subject"] = subject
    message["Bcc"] = sender

    message.attach(MIMEText(body, "plain"))

    #Open recorded gif from picamera

    with open(file1, "rb") as attachment:

        #octet streaming bloq
        part = MIMEBase("application" , "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # add header as key/value pair and convert to str
    part.add_header("Content-Disposition", f"attachment; filename = {file1}",)

    message.attach(part)
    text = message.as_string()

    #Open recorded gif from picamera

    with open(file2, "rb") as attachment:

        #octet streaming bloq
        part = MIMEBase("application" , "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # add header as key/value pair and convert to str
    part.add_header("Content-Disposition", f"attachment; filename = {file2}",)

    # add attachment to message and convert message to sting
    message.attach(part)
    text = message.as_string()

    #Log in and send
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, sender, text)

def run_sensor_webcam():

    print("Starting PIR Module")

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.IN)

    sleep(0.5)
    print('Ready')

    while True:
        if GPIO.input(17) or GPIO.input(18):
            
            print("Sensor B has detected some motion...")
            camerae.capture()
            send()

if __name__ == "__main__":

    global FLAG_RECORD, sleep

    FLAG_RECORD = False
    sensor_webcam = threading.Thread(target=run_sensor_webcam, args=())

    sensor_webcam.start()
    sensor_webcam.join()






    

                           


        
            




    
