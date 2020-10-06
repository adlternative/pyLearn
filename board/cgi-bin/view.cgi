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
id = form.getvalue('id')

print('''
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset=utf-8 />
    <title>View Message...</title>
  </head>
  <body>
  <h1>View Message</h1>
''')

try:
    id = int(id)
except:
    print("invaid message ID")
    sys.exit()

# s='select * from messages where id = %s'.format('asd')

curs.execute('select * from messages where id = %s',(id,))
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row))for row in curs.fetchall()]

if not rows:
    print('unknown message')
    sys.exit()
row = rows[0]
print("""
<p>
<b>subject:</b> {subject}<br />
<b>Sender:</b>{sender}<br/>
<pre>{text}</pre>
</p>
<hr />
<a href='main.cgi'>Back to the main page</a>
| <a href="edit.cgi?reply_to={id}">Reply</a>
</body>
</html>
  """.format_map(row))
