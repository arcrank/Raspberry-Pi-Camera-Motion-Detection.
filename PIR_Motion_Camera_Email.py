import RPi.GPIO as GPIO
import time
import datetime
import picamera
import os
import telebot

camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer

'''
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
'''

CHAT_ID = 1234567 # target chat_id AKA your user id, ideally
BOT_TOKEN = 'your bot token here'

bot = telebot.TeleBot(BOT_TOKEN)

COMMASPACE = ', '

def send_message(image):
    try:
        with open(image, 'rb') as f:
            bot.send_photo(CHAT_ID, f)
        print("Message sent!")
    except:
        print("Unable to send the message. Error: ", sys.exc_info()[0])
        raise



try:
    time.sleep(2) # to stabilize sensor
    
            
    while True:
        ##Timeloop
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if GPIO.input(23):
            ##If loop
            GPIO.output(24, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            print("Motion Detected at {}".format(st))
            ##Adds timestamp to image
            camera.capture('image_Time_{}.jpg'.format(st))
            image = ('image_Time_{}.jpg'.format(st))
            send_message(image)
            time.sleep(2)
            GPIO.output(24, False)
            time.sleep(5) #to avoid multiple detection

        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()



