import os
import sys
import json

from urllib.parse import urlencode
from urllib.reqest import Request, urlopen

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log(data)

  send_message('Hello, world!')

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  data = {
          'bot_id' : '5b69eeb4c800c919c2aff81edc',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  log(json)
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
