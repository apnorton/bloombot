
class BotController:
  # Static Members
  office_hours = {
      'Andrew'     : 'Thu 6-8',
      'Atallah'    : 'Wed 6-8, Wed 8-10',
      'Ben'        : 'Mon 6-8',
      'Divya'      : 'Mon 8-10',
      'Glenna'     : 'Thu 6-8, Thu 8-10',
      'Jake'       : 'Sun 4-6',
      'Jay'        : 'Wed 8-10',
      'Jessica'    : 'Mon 8-10',
      'John'       : 'Wed 8-10',
      'Joo Wan'    : 'Mon 8-10',
      'Leila'      : 'Mon 6-8, Wed 6-8',
      'Leon'       : 'Mon 6-8',
      'Marina'     : 'Thu 8-10',
      'Michelle'   : 'Sun 4-6, Wed 6-8',
      'Rachel'     : 'Thu 6-8',
      'Ryan'       : 'Mon 8-10, Thu 8-10',
      'Salah'      : 'Sun 6-8',
      'Sam'        : 'Thu 6-8',
      'Tahiya'     : 'Thu 8-10',
      'Xhama'      : 'Sun 6-8, Mon 6-8',
      'Bloomfield' : 'at an unknown time',
      'Floryan'    : 'at an unknown time',
    }

  OH_WORDS       = ['office hours', 'oh']
  GREETING_WORDS = ['hello', 'hi', 'what\'s up'] 
  HELP_WORDS     = ['help', 'you do?']

  # Field List:
  #  (none)

  def __init__(self):
    pass
  
  def text_preprocessing(self, text):
    return text.lower()

  def process_message(self, recd_msg):
    msg_to_send = {} # reply
    
    # Preprocessing
    text = recd_msg['text'].lower()

    # Helper function
    used_any = lambda word_list: any(map(lambda x : x in text, word_list))

    # Use some hard-coded rules to decide what this message says
    if 'when' in text and used_any(BotController.OH_WORDS):
      msg_to_send['text'] = 'You\'re asking about someone\'s office hours!'
    elif used_any(BotController.GREETING_WORDS):
      msg_to_send['text'] = 'Greetings to you, as well, {}!'.format(recd_msg['author'])
    elif used_any(BotController.HELP_WORDS):
      msg_to_send['text'] = ('Hi! I\'m Bloombot, the 2150 TA chatbot.  I don\'t do much right now,' +
                             ' but I will help remind you when timesheets are due, answer questions' + 
                             ' about whose office hours are when, and possibly do other things. \n' +
                             'I\'m open-source; check Andrew\'s github to suggest or add features.')
    else:
      msg_to_send['text'] = 'I can\'t tell what you\'re talking about.'

    return msg_to_send
