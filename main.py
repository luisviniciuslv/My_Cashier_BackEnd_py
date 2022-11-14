import os

from flask import Flask

from constants import config

class MyCashier(Flask):
  def __init__(self):
    super(MyCashier, self).__init__("MyCashier")
    for i in os.listdir('./src/controllers'):
        if str(i).endswith('.py'):
          i = str(i).replace('.py', '')
          self.register_blueprint(__import__('src.controllers.' + i, fromlist=[i]).__dict__[i])
          print("loaded ", i)

client = MyCashier()
client.run(port=config["PORT"])
