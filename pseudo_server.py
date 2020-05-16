# We run a flask server to keep repl.it alive 
# is also being pinged from https://uptimerobot.com/ (20 minute interval)

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Server is running..."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()