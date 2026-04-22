import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("calculator")
root.geometry("200x200")

def add():
    number1 = e1.get()
    number2 = e2.get()
    addition = int(number1)+int(number2)
    messagebox.showinfo("adding succesfull", addition)
    
def sub():
    number1 = e1.get()
    number2 = e2.get()
    messagebox.showinfo("subtracting succesfull", int(number1)-int(number2))
    print(number1, number2)

def multi():
    number1 = e1.get()
    number2 = e2.get()
    messagebox.showinfo("multiple succesfull", int(number1)*int(number2))
    print(number1, number2)

def div():
    number1 = e1.get()
    number2 = e2.get()
    messagebox.showinfo("division succesfull", int(number1)/int(number2))
    print(number1, number2)
l1 = tk.Label(root, text="number->1")
l1.grid(row=0, column=0)

l2 = tk.Label(root, text="number->2")
l2.grid(row=1, column=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)

e2 = tk.Entry(root)
e2.grid(row=1, column=1)

b1 = tk.Button(root, text="+", command=add)
b1.place(x=10, y=70)

b1 = tk.Button(root, text="-", command=sub)
b1.place(x=60, y=70)

b1 = tk.Button(root, text="*", command=multi)
b1.place(x=110, y=70)

b1 = tk.Button(root, text="/", command=div)
b1.place(x=150, y=70)

root.mainloop()


# 1. Data Type Awareness
# User jo bhi Entry mein likhta hai, wo hamesha String hota hai. Math karne ke liye usey int() ya float() mein convert karna hi padega.

# 2. Geometry Managers ka Rule
# Tkinter mein teen tarike hote hain cheezon ko screen par sajane ke:

# .pack(): Ek ke niche ek (Simple layout).

# .grid(): Rows aur Columns (Table jaisa, sabse best).

# .place(): Exact X aur Y coordinates (Bahut mehnat wala).

# Rule: Ek hi window mein grid aur pack ko kabhi mix mat karna, varna window "freez" ho jayegi.

# 3. Button Command Logic
# Aapne command=add likha, ye sahi hai. Lekin dhyan rakhna ki yahan add() (brackets ke saath) mat likhna, varna function button dabane se pehle hi chal jayega. Hum sirf function ka naam pass karte hain.

# Ek chhota sa challenge du aapko isi task se juda hua?
# Agar aap chaho, toh try karo ki jab user "+" button dabaye, toh input boxes apne aap khali (clear) ho jayein calculation ke baad. Isse aapko .delete() method ki practice ho jayegi.

# Try karoge ya fir agla topic start karein?