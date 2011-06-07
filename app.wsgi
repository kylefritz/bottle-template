import os

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

#include pwd
import sys
wsgi_dir=os.path.dirname(__file__)
sys.path = [wsgi_dir] + sys.path

# ... add or import your bottle app code here ...
from brian import *
import bottle
app = bottle.app() 

# Do NOT use bottle.run() with mod_wsgi
application = app
