#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()

text = form.getvalue('text', open('a.txt',encoding='utf-8').read())
f = open('a.txt', 'w')
f.write(text)
f.close()
print('''Content-type: text/html

<html>
<head>
<title>
a simple editor
</title>
</head>
<body>
<form action='simple_edit.cgi' method='POST'>
<textarea rows='100' cols='200' name='text'>{}</textarea><br />
<input type='submit'>
</form>
</body>
</html>
 '''.format(text))

#.encode("gb2312")

