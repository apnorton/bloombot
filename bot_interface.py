

class BotInterface:
  # Fields:
  #  - bot
  # 

  def __init__(self):
    self.bot = None

  # process_message
  #   msg : dictionary
  #    has keys "author", "text", and "timestamp"
  #   returns new msg dictionary:
  #    (just text key for now)
  def process_message(self, msg):
    reply = 'Hi {}. I got your message: "{}" at {}'.format(msg['author'], msg['text'], msg['timestamp']) 
    return { 'text' : reply }
