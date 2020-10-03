#!/usr/bin/python3
# -*-codeing:utf-8-*-
# import cgitb;cgitb.enable()
import cgi
form = cgi.FieldStorage()
name = form.getvalue('name','world')
age = form.getvalue('age','18')
print("""Content-type: text/html

<html>
	<head>
		<title>ADL Is u father</title>
	</head>
	<body>
		<h1>hello,{} years old {}!</h1>
		<form action=cgi02.cgi>
		Change age  <input type='text' name='age' />
		<input type='submit' />
		Change name <input type='text' name='name' />
		<input type='submit' />
		</form>
	</body>
</html>
""".format(age,name))
# print()
# i= input("in")
# age = form.getvalue('age','18')
# print((name),age)
# print("helo")
