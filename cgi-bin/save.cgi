#!/usr/bin/python3
import sys
import cgi
from os.path import join, abspath
from hashlib import sha1
print("Content-type:text/html\n")
# print(sha1(b'foobar').hexdigest())
# sys.exit()


BASE_DIR = abspath('data')
form = cgi.FieldStorage()
text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')
if not (filename and text and password):
    print('invaild parameters')
    sys.exit()
if sha1(password.encode()).hexdigest() != '8843d7f92416211de9ebb963ff4ce28125932878':
    print('invalid password')
    sys.exit()
f=open(join(BASE_DIR,filename),'w')
f.write(text)
f.close()
print('the file has been saved')
