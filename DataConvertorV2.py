import tkinter as tk

win = tk.Tk()
y = 0

def sayHi():
	global y
	y += 1
	print(y)

win.geometry("480x360")
b = tk.Button(
	win,
	text='click here',
	command=sayHi()
)
b.pack()
win.mainloop()
