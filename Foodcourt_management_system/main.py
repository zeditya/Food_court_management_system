import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from mydb import start_db

cart=[]

def add():
    try:
        sel=box.get(box.curselection())
        n=sel.split("-")[0].strip()
        p=float(sel.split("-")[1].replace("Rs","").strip())
        cart.append({"Item":n,"Price":p})
        messagebox.showinfo("Done",n+" added")
    except:
        messagebox.showerror("Error","Select item")

def bill():
    if len(cart)==0:
        messagebox.showwarning("Wait","Cart empty")
        return
    df=pd.DataFrame(cart)
    val=df["Price"].values
    tot=np.sum(val)
    tx=tot*0.05
    fin=tot+tx
    txt="BILL\n"
    txt+=df.to_string(index=False)
    txt+="\nTotal:"+str(tot)
    txt+="\nTax:"+str(tx)
    txt+="\nFinal:"+str(fin)
    messagebox.showinfo("Bill",txt)

win=tk.Tk()
win.title("Food court management system")
win.geometry("300x400")

l1=tk.Label(win,text="Menu")
l1.pack()

box=tk.Listbox(win)
box.pack()

db=start_db()
data=db["food_items"].find()

for x in data:
    box.insert("end",x["name"]+"-"+str(x["price"])+"Rs")
b1=tk.Button(win,text="Add",command=add)
b1.pack()
b2=tk.Button(win,text="Bill",command=bill)
b2.pack()

win.mainloop()