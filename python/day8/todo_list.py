# create to do list using python code
# what we need to create to do list 
# 1. list -> 1
# 2. add function
# show function
# delete function
# save function
# edit function
# load function 

import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
task_count = 0
root = tk.Tk()   # this code define -> here root is the variable name which strore data and tk.tk mean initilagine the labirary which is abilaval in background of python

root.title("My First Python Todo List") # this code is used for change title of the page which you want to design
root.geometry("500x500") # this code define the height and width of the page how much he long 


#---------------------All code working program backend-------------------------#
def add_task():
    global task_count # here we use global fro change function like task count
    task = entry.get()
    if task != "":
        task_count += 1
        formatted_task = f"{task_count}.{task}\n"
        task_display.config(state="normal")
        task_display.insert('end', formatted_task)
        task_display.config(state="disabled")

        entry.delete(0, 'end')
        print(task)

def load_task():
    print("task loading ...................")
    global task_count
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
    if file_path:
        with open(file_path,"r") as file:
            content = file.read()
        task_display.delete("1.0","end")
        task_display.insert("1.0",content)
        task_display.config(state="disabled")

        lines = content.strip().split('\n')

        if lines[0]=="":
            task_count = 0
        else:
            task_count = len(lines)
        print(f"Data Comes From This File Path:'{file_path}'")

def save_task():
    print("Task Saving.................")
    # with open("task.txt", "w") as file:
    #     file.write(content)
    # print("file saved succefully")

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),("All files", "*.*")])

    if file_path:
        content = task_display.get("1.0", "end-1c")
        with open(file_path,"w") as file:
            file.write(content)
        print(f"file saved successfully in this location: {file_path}")
    else:
        print(f"file location not selected")
    
def  windows_exit():
    response = messagebox.askyesno("Exit Conformation", "Are You Seriouslly Want To Exit If Yes Please Check Are You Save This File Or Not")
    if response ==1:
        print("windows Are Now Closing.........")
        root.destroy()
    else:
        print("Windows Not Close Please Try Again")

def delete_task():
    global task_count
    if task_count >0:
        task_display.config(state="normal")
        task_display.delete("end-2l", "end-1l")
        task_count -=1
        task_display.config(state="disabled")
        print("last task will be deleted")
    else:
        messagebox.showwarning("warning", "list is empty")

#----------------design menubar for multiple option --------------------------#
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

#----------------menubar option ------------------------------------#
file_menu = tk.Menu(menu_bar, tearoff=0) #tear off mean the menu is not out of the windows
menu_bar.add_cascade(label="File", menu=file_menu) # menu button 

file_menu.add_command(label="Load Task", command=load_task) # load task button 
file_menu.add_command(label="Save Task", command=save_task) # save task button 
file_menu.add_command(label="exit", command=windows_exit) # exit button 


#----------- Now we need to design frame for our project whose code given bellow ---------------#
input_frame = tk.Frame(root, pady=10, )
input_frame.pack(side='top', fill='both', expand=True)

bottom_frame = tk.Frame(root, padx=10, pady=10)
bottom_frame.pack(side='bottom', fill='both', expand=True)



#------------------------------for display task -----------------------#
task_display =tk.Text(bottom_frame, height=10)
task_display.pack(fill='both', expand=True)

#--------- after from deisgn we need to design one entry box for make entry in the the list ----------------#
entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
entry.pack(side='left', padx=5)

#----------------- Now we need a add button after entry because for adding a tsk we need any button which perform work for add -------------------#

add_button = tk.Button(input_frame, width=10, text="Add Task", command = add_task)
add_button.pack(side='left',padx=2)

delete_button = tk.Button(input_frame, width=20, text="Delete Last Items", command=delete_task)
delete_button.pack(side='right', padx=2)





root.mainloop()

#----------------------------------------------------------todo_list.py--------------------------------end-------------------------------------------------------------------------#