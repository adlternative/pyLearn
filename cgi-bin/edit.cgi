#!/usr/bin/env python3
import sys
import cgi
from os.path import join, abspath
from html.parser import HTMLParser
print("Content-type: text/html\n")

BASE_DIR = abspath("data")
form = cgi.FieldStorage()

filename = HTMLParser().unescape(form.getvalue('filename'))
if not filename:
  print('please enter a file name')
  sys.exit()
try:
  text =open(join(BASE_DIR,filename)).read()
except FileNotFoundError :
  print('the file is not exist')
  sys.exit()
#lang="zh-CN"
print('''
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset=utf-8 />
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

