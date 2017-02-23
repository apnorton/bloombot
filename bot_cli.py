import os
import sys
import json
import socket
from datetime import datetime

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

##
# Assuming we've started up the bot on localhost using gunicorn,
# this program provides a CLI for testing the bot locally before
# deployment to heroku
##

def send_to_bot(msg):
  url  = 'http://127.0.0.1:8000'
  data = {
          "attachments": [],
          "avatar_url": "http://i.groupme.com/123456789",
          "created_at": 1302623328,
          "group_id": "1234567890",
          "id": "1234567890",
          "sender_id": "12345",
          "sender_type": "user",
          "source_guid": "GUID",
          "system": False,
          "user_id": "1234567890",
          "name": msg['author'],
          "text": msg['text'],
         }
  params = json.dumps(data).encode('utf-8')

  request = Request(url, data=params)
  request.add_header('Content-Type', 'application/json')

  reply = urlopen(request).read().decode()

def request_canned_message(title):
  url  = 'http://127.0.0.1:8000/canned'
  data = {
          "topic": title,
         }
  params = json.dumps(data).encode('utf-8')

  request = Request(url, data=params)
  request.add_header('Content-Type', 'application/json')

  reply = urlopen(request).read().decode()

if __name__ == '__main__':
  while True:
    text = input('>>> ')

    if text.startswith(':'):
      commands = text.split()
      # special commands:
      if commands[0] == ':quit':
        break
      elif commands[0] == ':canned':
        request_canned_message(commands[1])
        
    msg = {}
    msg['author']    = 'Andrew Norton'
    msg['text']      = text
    msg['timestamp'] = str(datetime.now())

    send_to_bot(msg)

 
