import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from bot.bot_interface import BotInterface

app = Flask(__name__)
bi  = BotInterface()


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'Bloombot':
    msg = {}
    msg['author']    = data['name']
    msg['author_id'] = data['sender_id']
    msg['text']      = data['text']

    reply = bi.process_message(msg)
    if reply:
      send_message(reply['text'])

  return "ok", 200

@app.route('/canned', methods=['POST'])
def canned_webhook():
  data = request.get_json()
  print(data)
  reply = bi.canned_reply(data['topic'])
  send_message(reply['text'])

  return "ok", 200


def send_message(msg):
  if 'BLOOMBOT_DEBUG' in os.environ:
    print('[Bloombot]: ' + msg)
    return
    
  # if not in debug mode, use the right url 
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : '5b69eeb4c800c919c2aff81edc',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
