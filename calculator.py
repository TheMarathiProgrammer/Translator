import tkinter as tk 
from tkinter import *
root = tk.Tk()
root.title('Calculator')
root.geometry('500x500')


entry_1 = tk.Entry(root,width=60)
entry_1.pack(pady=20)
math = ''

def button_click(number):
	current = entry_1.get()
	entry_1.delete(0,END)
	entry_1.insert(0,str(current)+str(number))
	
def button_add():
	global math,first_number
	first_number=entry_1.get()
	if '.' in first_number:
		first_number = float(first_number)
	else:
		first_number=int(first_number)
	entry_1.delete(0,END)
	math = 'Addition'

def button_subtract():
	global math,first_number
	first_number=entry_1.get()
	if '.' in first_number:
		first_number = float(first_number)
	else:
		first_number=int(first_number)
	entry_1.delete(0,END)
	math = 'Subtraction'

def button_multiply():
	global math,first_number
	first_number=entry_1.get()
	if '.' in first_number:
		first_number = float(first_number)
	else:
		first_number=int(first_number)
	entry_1.delete(0,END)
	math = 'Multiplication'

def button_division():
	global math,first_number
	first_number=entry_1.get()
	if '.' in first_number:
		first_number = float(first_number)
	else:
		first_number=int(first_number)
	entry_1.delete(0,END)
	math = 'Divided'

def button_equals():
	global math,first_number
	second_number = entry_1.get()
	if '.' in second_number:
		second_number = float(second_number)
	else:
		second_number = int(second_number)
	if math == 'Addition':
		add = first_number+second_number
		entry_1.delete(0,END)
		entry_1.insert(0,add)

	if math == 'Subtraction':
		sub = first_number-second_number
		entry_1.delete(0,END)
		entry_1.insert(0,sub)

	if math == 'Multiplication':
		mul = first_number*second_number
		entry_1.delete(0,END)
		entry_1.insert(0,mul)

	if math == 'Divided':
		div = first_number/second_number
		entry_1.delete(0,END)
		entry_1.insert(0,div)

def clear():
	entry_1.delete(0,END)
frame = tk.Frame(root)
frame.pack()
btn_clear = tk.Button(frame,text='clear',padx=20,pady=10,bg='white',font=('bold'),activebackground='grey',command=clear)
btn_clear.pack(side=LEFT)
frame1 = tk.Frame(root)
frame1.pack()
btn_7 = tk.Button(frame1,text='7',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("7"))
btn_7.pack(side= LEFT,padx=10,pady=10)
btn_8 = tk.Button(frame1,text='8',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("8"))
btn_8.pack(side= LEFT,padx=10,pady=10)
btn_9 = tk.Button(frame1,text='9',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("9"))
btn_9.pack(side= LEFT,padx=10,pady=10)
btn_multiply = tk.Button(frame1,text='X',padx=40,pady=20,bg='#00c2cb',font=('bold'),activebackground='grey',command=button_multiply)
btn_multiply.pack(side=LEFT,padx=10,pady=10)

frame2 = tk.Frame(root) 
frame2.pack()
btn_4 = tk.Button(frame2,text='4',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("4"))
btn_4.pack(side= LEFT,padx=10,pady=10)
btn_5 = tk.Button(frame2,text='5',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("5"))
btn_5.pack(side= LEFT,padx=10,pady=10)
btn_6 = tk.Button(frame2,text='6',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("6"))
btn_6.pack(side= LEFT,padx=10,pady=10)
btn_minus = tk.Button(frame2,text='-',padx=40,pady=20,bg='#00c2cb',font=('bold'),activebackground='grey',command=button_subtract)
btn_minus.pack(side=LEFT,padx=10,pady=10)



frame3 = tk.Frame(root)
frame3.pack()
btn_1 = tk.Button(frame3,text='1',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("1"))
btn_1.pack(side= LEFT,padx=10,pady=10)
btn_2 = tk.Button(frame3,text='2',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("2"))
btn_2.pack(side= LEFT,padx=10,pady=10)
btn_3 = tk.Button(frame3,text='3',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("3"))
btn_3.pack(side= LEFT,padx=10,pady=10)
btn_plus = tk.Button(frame3,text='+',padx=40,pady=20,bg='#00c2cb',font=('bold'),activebackground='grey',command=button_add)
btn_plus.pack(side=LEFT,padx=10,pady=10)

frame4 = tk.Frame(root)
frame4.pack()
btn_dot = tk.Button(frame4,text='.',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("."))
btn_dot.pack(side=LEFT,padx=10,pady=10)
btn_0 = tk.Button(frame4,text='0',padx=40,pady=20,bg='white',font=('bold'),activebackground='grey',command=lambda: button_click("0"))
btn_0.pack(side=LEFT,padx=10,pady=10)
btn_equals = tk.Button(frame4,text='=',padx=40,pady=20,bg='#ff5757',font=('bold'),activebackground='grey',command=button_equals)
btn_equals.pack(side=LEFT,padx=10,pady=10)
btn_divide = tk.Button(frame4,text='/',padx=40,pady=20,bg='#00c2cb',font=('bold'),activebackground='grey',command=button_division)
btn_divide.pack(side=LEFT,padx=10,pady=10)

root.mainloop()
