

class BotInterface:
  # Fields:
  #  - bot
  # 

  def __init__(self):
    self.bot = None

  # process_message
  #   msg : dictionary
  #    has keys "author", "text", and "author_id"
  #   returns new msg dictionary:
  #    (just text key for now)
  def process_message(self, msg):
    if any(map(lambda s: s in msg['text'], ['Hi', 'Hello', 'bot'])):
      reply = 'Hi {}!  It\'s nice to meet you.'.format(msg['author'])
      return { 'text' : reply }
    
    return None
