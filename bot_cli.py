from datetime import datetime

from bot.bot_interface import BotInterface

if __name__ == '__main__':
  bi = BotInterface()

  while True:
    text = input('>>> ')

    if text == 'quit()':
      break

    msg = {}
    msg['author']    = 'Andrew Norton'
    msg['text']      = text
    msg['timestamp'] = str(datetime.now())

    reply = bi.process_message(msg)
    if reply:
      print(reply['text'])

