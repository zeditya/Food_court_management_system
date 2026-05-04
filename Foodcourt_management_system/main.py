import tkinter as tk
from tkinter import messagebox,simpledialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

def update():
    try:
        sel=box.get(box.curselection())
        n=sel.split("-")[0].strip()
        new_p=simpledialog.askinteger("Price","New price:")
        if new_p:
            db=start_db()
            db["food_items"].update_one({"name":n},{"$set":{"price":new_p}})
            messagebox.showinfo("Done","Updated! Restart app")
    except:
        messagebox.showerror("Error","Select item")

def graph():
    if len(cart)==0:
        messagebox.showwarning("Wait","Cart empty")
        return
    df=pd.DataFrame(cart)
    cnt=df["Item"].value_counts()
    plt.bar(cnt.index,cnt.values)
    plt.title("Items in Cart")
    plt.show()

win=tk.Tk()
win.title("Food management system")
win.geometry("300x500")

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

b3=tk.Button(win,text="Update",command=update)
b3.pack()

b4=tk.Button(win,text="Graph",command=graph)
b4.pack()

win.mainloop()