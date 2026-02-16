import os
import string 
import tkinter as tk
from tkinter.messagebox import showinfo 


window = tk.Tk()
window.title('Desktop Search')

tk.Label(window , text="Enter to be search ").grid(row=0)
searchtext = tk.Entry(window,width=150)
searchtext.grid(row=0,column=150)
tk.Label(window,text='search results ---->' ).grid(row=1)
tk.Button(window,text="Search",).grid(row=0,column=2)

tk.Button(window,text="Merge .txt file form search results",fg="blue").grid(row=2,column=1)
tk.Button(window,text="QUIT" , fg="red",command=window.destroy).grid(row=3,column=2)

tk.mainloop()

