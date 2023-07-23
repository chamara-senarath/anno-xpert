from tkinter import *
import ttkbootstrap as tb

app = tb.Window(themename="cosmo")
app.geometry('500x350')

my_label =  tb.Label(text="Hello World", font=("Helvetica", 16), bootstyle="primary")
my_label.pack(side=RIGHT,pady=50, padx=50)

my_button = tb.Button(text="Click me!", bootstyle="success")
my_button.pack(pady=20)

app.mainloop()