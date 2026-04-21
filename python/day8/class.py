import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.title("")
root.geometry("500x500")

nameEntry = tk.Entry(root)
text = tk.Text(root, height=20, width=40)
nameEntry.pack()
text.pack()

# text.delete("1.0", tk.END)

def add_task():
    task = nameEntry.get()
    text.insert(tk.END, task + "\n")
def save_task():
    task = text.get("1.0", tk.END).strip()
    if task:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(task)
            messagebox.showinfo("success", "Task Are Added Succefully")
            print("task saved")
    else:
        messagebox.showwarning("warning:","There is no task in the field")
        print("task not saved")


btn = tk.Button(root,text="add_task",command=add_task)
btn.pack()

btn2 = tk.Button(root, text="save task", command=save_task)
btn2.pack()



root.mainloop()



# file opration
