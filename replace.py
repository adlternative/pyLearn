import sys

try:
  with open(input('输入文件名:'),"r+") as file:
    text = file.read()
    text=text.replace('.', '。').replace(',', '，')
    # text=text.replace(',', '，')
    # print(text)
    file.seek(0)
    file.write(text)
    print('修改成功')
    file.close()
except Exception as e:
  print(e)
  sys.exit()
