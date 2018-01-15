#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: sms.py


################

import nexmo
import time
from threading import Thread

key = 'd1258708'
secret = 'ea2d3fe59f49fb64'

client = nexmo.Client(key=key, secret=secret)

sms_list = []

def send_sms(number, message):
    message = (number, message)
    sms_list.append(message)

def send(number, message):
  client.send_message({
    'from': 16018666656,
    'to': number,
    'text': message,
    'type': 'unicode'
  })


def check_sms():
    while True:
        if len(sms_list) == 0:
            pass
        else:
            number = sms_list[0][0]
            text = sms_list[0][1]
            if number != None:
                send(number, text)
                print('%s 发送成功 %s' % (number, text))
                time.sleep(2)
            sms_list.remove(sms_list[0])

Thread(target=check_sms, args=()).start()
#phone = 16267318573
#text = 'A text message sent using the Nexmo SMS API'
#send_sms(phone, text)
