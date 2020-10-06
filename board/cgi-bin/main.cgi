#!/usr/bin/python3

import cgitb
import pymysql
print("Content-type:text/html\n")

cgitb.enable()
db = pymysql.connect("127.0.0.1", "root", "123456", "py")
curs = db.cursor()

print('''
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset=utf-8 />
    <title>the foobar bulletin board...</title>
  </head>
  <body>
  <h1>The FooBar Bulletin Board</h1>
''')

curs.execute('select * from messages')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row))for row in curs.fetchall()]
toplevel = []
children = {}
for row in rows:
    parent_id = row['reply_to']

    if parent_id is None:
        toplevel.append(row)
    else:
        children.setdefault(parent_id, []).append(row)
#大致上会形成 childlren = {3:[{id:2,},]}
#大致上会形成 toplevel = [{id:3,},]

def format(row):
    #主题+其地址
    # try:kids=children[row['id']]
    # except KeyError:pass
    # else
    # print(row['subject'])
    # print(row['sender'],":")
    # print(row['text'])
    #先序遍历
    print('<p><a href="view.cgi?id={id}">{subject}</a></p>'.format_map(row))
    try:
        kids = children[row['id']]
    except KeyError:
        pass
    else:
        print('<blockquote>')
        for kid in kids:
            format(kid)
        print('</blockquote>')

    print('<p>')


for row in toplevel:
    format(row)
print("""
      </p>
    <hr />
    <p>
      <a href="edit.cgi">post message</a>
    </p>
  </body>
</html>
 """)
