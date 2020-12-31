import tkinter as tk
from tkinter import ttk

from tkinter import * #everting

root = tk.Tk()

L1 = Label(root, text="song/content: ")
L1.grid(row=1, column=1)

C0 = ttk.Combobox(root, values=["song","content"])
C0.current(0) #select
C0.grid(row=1, column=2)



L2 = Label(root, text="category: ")
L2.grid(row=2, column=1)



C1 = ttk.Combobox(root, values=["agayt","bhagwan","lagan","pyaar","dosti","guru","prerna","tyag"])
C1.current(0) #select
C1.grid(row=2, column=2)

L3 = Label(root, text="enter id: ")
L3.grid(row=3, column=1)

E1 = Entry(root)
E1.grid(row=3, column=2)


L4 = Label(root, text="content: ")
L4.grid(row=4, column=1)

E2 = Entry(root)
E2.grid(row=4, column=2)

L4 = Label(root, text="message: ")
L4.grid(row=5, column=1)

result = StringVar()
result.set("all good")
L5 = Label(root, textvar=result) #for dynamic text we use textvar
L5.grid(row=5, column=2)


def calculate():
	a = C0.get()
	b = C1.get()
	c = int(E1.get())
	d = E2.get()
	print("content/song: ",a)
	print('category: ',b)
	print('your id is: ',c)
	print('your content is: ',d)
	

bt = Button(root, text="Submit", command=calculate)
bt.grid(row=6, column=2)

root.mainloop()
