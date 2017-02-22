import os
import sys
import json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log(data)
  
def log(msg):
  print str(msg)
  sys.stdout.flush()
