import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My First App")
root.geometry("500x600")
def login():
    username = e1.get()
    messagebox.showinfo("login successful","welcome"+username)
    print(username)





    password = e2.get()
    print(password)
    print("Login Successful")

l1 = tk.Label(root, text="username")
l1.grid(row=0, column=0)

l2 = tk.Label(root, text="password")
l2.grid(row=1, column=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)

e2 = tk.Entry(root, show="-")
e2.grid(row=1, column=1)

b1 = tk.Button(root,text="Login", command=login)
b1.place(x=10, y=50)




# pack()
# grid(row,column)
# place(x,y)


root.mainloop()


# wizart
