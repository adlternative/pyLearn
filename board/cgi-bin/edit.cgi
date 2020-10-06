#!/usr/bin/python3

import cgitb
import pymysql
import sys
import cgi
print("Content-type:text/html\n")

cgitb.enable()
db = pymysql.connect("127.0.0.1", "root", "123456", "py")
curs = db.cursor()
form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')

print('''
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset=utf-8 />
    <title>Compose Message...</title>
  </head>
  <body>
  <h1>Compose Message</h1>
    <form action='save.cgi' method='POST'>
''')
subject = ''
if reply_to is not None:
    print('<input type="hidden" name="reply_to" value="{}" />'.format(reply_to))
    curs.execute('SELECT subject From messages where id = %s', (reply_to,))
    # names = [d[0] for d in curs.description]
    # rows = [dict(zip(names, row))for row in curs.fetchall()]
    subject = curs.fetchone()[0]
    if not subject.startswith('Reply: '):
      subject = 'Reply: '+subject
print("""
<b>Subject:</b><br />
<input type='text' size='40' name='subject' value='{}' /><br />
<b>Sender:</b><br />
<input type='text' size='40' name='sender' /><br />
<b>Message:</b><br />
<textarea name='text' cols='40' rows='20'></textarea><br />
<input type ='submit' value='Save' />
</form>
<hr />
<a href='main.cgi'>Back to the main page</a>
</body>
</html>
  """.format(subject))
