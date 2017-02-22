BloomBot
========

A simple chatbot for 2150 TAs.  Deployed to Heroku for webhook into the 2150TA Groupme.

Local Testing
-------------

Since I was tired of continually deploying broken stuff to Heroku, I wrote a small bot client in CLI; the process for local running is:

```
$ source debug_setup.sh
$ gunicorn app:app --log-file bot.log & # Run botserver in background
$ python3 bot_cli.py # Run CLI for sending messages to bot
```

It's a little hacky (the botserver determines if it's in debug mode and prints responses instead of sending them back over HTTP), but it works and is good enough for simple tests.

Misc
----

**Avatar**: Why such an odd avatar image?  I chose it as a combination of a *mild* resemblence to [Tay][tay]'s avatar and a Deep Dream image.  I used [this generator][deep-dream] to create the generated image.

[tay]: https://en.wikipedia.org/wiki/Tay_(bot) 
[deep-dream]: https://deepdreamgenerator.com/
