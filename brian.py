#!/usr/bin/env python 

from bottle import *

@route('/')
@view('home')
def home():
  brian="rocks"
  return locals()

@get('/static/:thing')
def static_thing(thing):
  static_file(thing,root='static')

if __name__ == '__main__':
  import bottle
  app = bottle.app()
  bottle.debug(True)
  bottle.run(app=app,host='localhost', port=8080,reloader=True)
