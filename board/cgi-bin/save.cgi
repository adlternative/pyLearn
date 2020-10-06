#!/usr/bin/python3

import cgitb
import pymysql
import sys
import cgi
import logging
from html.parser import HTMLParser
import logging

print("Content-type:text/html\n")

cgitb.enable()
db = pymysql.connect("127.0.0.1", "root", "123456", "py")
curs = db.cursor()
form = cgi.FieldStorage()
logging.basicConfig(level=logging.INFO, filename='mylog.log')
sender = HTMLParser().unescape(form.getvalue('sender'))
subject = HTMLParser().unescape(form.getvalue('subject'))
text = HTMLParser().unescape(form.getvalue('text'))
reply_to = form.getvalue('reply_to')

logging.info(sender)
logging.info(subject)
logging.info(text)
logging.info(reply_to)


if not (sender and subject and text):
    print('please supply sender,subject,and text')
if reply_to is not None:
    reply_to=HTMLParser().unescape(reply_to)
    query = ("""
    insert into
    messages(reply_to,sender,subject,text)values(%s,%s,%s,%s)
    """, (reply_to, sender, subject, text))

    logging.info(query)
else:
    query = ("""
    insert into
    messages(sender,subject,text)
    values(%s,%s,%s)
    """, (sender, subject, text))
try:
  curs.execute(*query)
except:
  db.rollback()
else :
  db.commit()
print("""
<html>
  <head>
    <title>Message Saved</title>
  </head>
  <body>
    <h1>Message Saved</h1>
    <hr />
    <a href='main.cgi'>Back to the main.page</a>
  </body>
</html>
 """)
db.close()