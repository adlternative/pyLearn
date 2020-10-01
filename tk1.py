
# import tkinter as tk
# from tkinter import *
# top =Tk()
# mainloop()
# btn =Button()
# # btn.pack()
# # btn['text']='CLick me!'
# def clicked():
# 	print('i was clicked')
# # btn['command']=clicked
# btn.config(text='click me',command=clicked)
# Button(text='click me too!',command=clicked).pack()
# Label(text='i am first win').pack()
# second =Toplevel()
# Label(second,text="i am second win").pack()
# for i in range(10):
# 	Button(text=i).pack()

# help(Pack.config)
# import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
# from tkinter.constants
def load():
	with open(filename.get())as file:
		contents.delete('1.0',END)
		contents.insert(INSERT,file.read())

def save():
	with open(filename.get(),'w')as file:
			file.write(contents.get('1.0',END))		

top =Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=BOTTOM,expand=True,fill=BOTH)
filename =Entry()
filename.pack(side=LEFT,expand=True,fill=X)
Button(text='Open',command=load).pack(side=LEFT)
Button(text='Save',command=save).pack(side=RIGHT)

mainloop()
