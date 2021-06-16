


from tkinter import *
from tkinter import messagebox as mb
import json
import os

root= Tk()
root.geometry("800x500")
root.title("Quiz")
cwd = os.getcwd()
print(os.listdir(cwd))
with open('quiz.json') as f:
    obj = json.load(f)
q=(obj['ques'])
options= (obj['options'])
a=(obj['ans'])

print(q)
print(options)
print(a)

root.mainloop()
