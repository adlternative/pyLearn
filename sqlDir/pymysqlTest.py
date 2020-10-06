#!/usr/bin/python3
import pymysql
from pprint import pprint
db = pymysql.connect("127.0.0.1", "root", "123456", "py")
cursor = db.cursor()
reply_to = input('reply to: ')
subject = input('SubJect: ')
sender = input('Sender: ')
text = input('Text: ')
if reply_to:
    query = """
INSERT INTO messages(reply_to,sender,subject,text)
VALUES({},'{}','{}','{}')
  """.format(reply_to, sender, subject, text)
else:
    query = """
INSERT INTO messages(sender,subject,text)
VALUES('{}','{}','{}')
  """.format(sender, subject, text)
cursor.execute(query)
db.commit()
# data =cursor.fetchall()
# pprint(data)
db.close()

