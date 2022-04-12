from tkinter import *
from tkinter.ttk import *
import pandas as pd

df = pd.read_csv("D:\Github Python D1\PythonD1\data-firearm.csv")

statelist = []
ostatelist = []
for i in df["state"]:
 if i not in statelist:
  statelist.append(i)
h = len(statelist)
print(statelist,h)

window = Tk()
window.title("test UI")
window.geometry("500x400")

text = Label(window, text="owen",)
text.grid(column=5,row=0)

textbox = Entry(window, width=50)
textbox.grid(column=10, row=0)

combo = Combobox(window,width=20)
combo["values"] = statelist
combo.grid(column=0, row=0)

def click():
 x = textbox.get()
 text.configure(text="Nanii")

button = Button(window, text="คนกดหล่อมากก", command=click)
button.grid(column=7,row=0)

window.mainloop()
