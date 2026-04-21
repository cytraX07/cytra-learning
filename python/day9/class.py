import tkinter as tk


# step 1: create windows

root = tk.Tk()
root.title("My Menu App")
root.geometry("500x500")

menu_bar = tk.Menu(root)
root.config(menu = menu_bar)

top_frame = tk.Frame(root,padding=10)
top_frame.pack(fill='x')

bottom_frame = tk.Frame(root,padding=10)
bottom_frame.pack(fill='both', expand=True)

task_entry = tk.Entry(top_frame, width=30)
task_entry.pack(side='left', padx=5)

add_button = tk.Button(top_frame,text="Add Task", command=lambda:add_task())
add_button.pack(side='left')


task_display= tk.Text(bottom_frame, height=15, wrap='word')
scrollbar = tk.Scrollbar(bottom_frame, orient='vertical', command=task_display.yview)
task_display.configure(yscrollcommand=scrollbar.set)

def save_file():
    print("saved")
    
    
def load_file():
    print("load successfull")

def exit_app():
    print("Exiting.....")
    root.quit()

def close():
    print("close")
    

file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu2 = tk.Menu(menu_bar,tearoff=0)

file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Load", command=load_file)
file_menu.add_command(label="exit", command=exit_app)

file_menu2.add_command(label="close", command=close)


menu_bar.add_cascade(label="file", menu=file_menu)
menu_bar.add_cascade(label="exit", menu=file_menu2)


# windows show command
root.mainloop()

