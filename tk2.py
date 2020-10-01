

from tkinter import *
from tkinter.scrolledtext import ScrolledText


top =Tk()

btn =Button()
btn.pack()
btn['text']='helo you'
def funcc(string):
	print(string)

def click():
	print('you are amazing')
	second =Toplevel()
	Label(second,text='i am first win').pack()

# def click():print('you are amazing')
btn['command']=click
# btn.config(text="click me",command=click)
Button(text='click me too!',command=click).pack()
Label(text='i am first win').pack()
second =Toplevel()
Label(second,text="i am second win").pack()
for i in range(10):
	Button(text=i).pack()
top.bind('<Button-1>',funcc)

mainloop()
