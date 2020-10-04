#!/usr/bin/env python3

import sys
import cgi
from os.path import join, abspath
print("Content-type: text/html\n")

BASE_DIR = abspath("data")
form = cgi.FieldStorage()

filename = form.getvalue('filename')
if not filename:
  print('please enter a file name')
  sys.exit()

text =open(join(BASE_DIR,filename)).read()
print('''
<html>
  <head>
    <title>Editing...</title>
  </head>
  <body>
  <form action ='save.cgi' method='POST'>
    <b>File:</b>{}<br />
    <input type='hidden' value='{}' name='filename' />
    <b>Password:</b><br/>
    <input name='password' type='password' /><br />
    <b>Text:</b><br />
    <textarea name='text' cols='40' rows='20'>{}</textarea><br/>
    <input type='submit' value='Save' />
  </form>
  </body>
</html>
 '''.format(filename,filename,text))
