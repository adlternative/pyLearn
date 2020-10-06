#!/usr/bin/python3
import pymysql
from pprint import pprint
db = pymysql.connect("127.0.0.1", "root", "123456", "py")
cursor = db.cursor()

# reply_to = input('reply to: ')
# subject = input('SubJect: ')
# sender = input('Sender: ')
# text = input('Text: ')
# if reply_to:
#     query = """
# INSERT INTO messages(reply_to,sender,subject,text)
# VALUES({},'{}','{}','{}')
#   """.format(reply_to, sender, subject, text)
# else:
#     query = """
# INSERT INTO messages(sender,subject,text)
# VALUES('{}','{}','{}')
#   """.format(sender, subject, text)

#update  messages
#set reply_to = NULL where id= 3
 
def update():
    query = """
 update  messages
set reply_to = NULL where id= 3
   """
    return query


def select_all():
    query = """
 select * from messages
   """
    return query

cursor.execute(update())

# for i in cursor.fetchall():
#   print(i)
# names = [d[0] for d in cursor.description]
# rows = [dict(zip(names, row))for row in cursor.fetchall()]
# print(rows)
db.commit()
# data =cursor.fetchall()
# pprint(data)
db.close()