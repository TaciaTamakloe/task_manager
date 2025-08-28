import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands 

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(title="Update",message="Cannot be updated with empty task", parent=app)
    else:
        commands.update_task(id, {"title": title})
        show_all_tasks_frame(app)


def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)

def submit_tasks(title, app):
    if not title:
        messagebox.showerror(title="Add task",message= "cannot add empty task",parent=app)
    else:
        commands.save_task({"title":title})
        show_all_tasks_frame(app)

def show_edit_task_frame(task,app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0,sticky="nsew", padx=10, pady=10)
    label = tk.Label(master=frame, text=f"Edit task:{task["title"]}")
    label.grid()
    # Add an entry widget and show the task title
    entry = tk.Entry(master=frame)
    entry.insert(0,task["title"])
    entry.grid(column=1)
    #Add a button with text update for the saving the changes
    update_btn = tk.Button(master=frame,
                           text="update",
                           command=lambda: handle_update(task["_id"], entry.get(),app))
    update_btn.grid(column=1, row=2)
    # Add a button with the text back/cancel to remove the frame
    cancel_btn = tk.Button(master=frame,text="Back",command=lambda:frame.destroy())
    cancel_btn.grid(column=1, row=3)
    
     

def show_add_task_frame(app):
        
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0,sticky="nsew", padx=10, pady=10)
    
    label = tk.Label(master=frame, text="what do you want to do?")
    label.grid()
    entry= tk.Entry(master=frame)
    entry.grid()
    btn= tk.Button(
        master=frame,
        text = "submit",
         command=lambda:submit_tasks(entry.get(), app))
    btn.grid()
    frame.tkraise()
    

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0,sticky="nsew", padx=10, pady=10)
    
    
    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master = frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)
        
        btn = tk.Button(master=frame, text="Delete",command=lambda:handle_delete(task["_id"],app ))
        btn.grid(row=tasks.index(task), column=1)
        
    btn = tk.Button(master=frame, text="Add Task",command=lambda: show_add_task_frame(app))
    btn.grid(row=len(tasks) + 1, column=1)
        
    frame.tkraise()
    def show_all_tasks_frame(app):
     frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)

        edit_btn = tk.Button(
            master=frame,
            text= "Edit", command=partial(show_edit_task_frame,task,app)
        )
        edit_btn.grid(row=tasks.index(task), column=1)

        delete_btn = tk.Button(master=frame, 
                        text="Delete",
                        command=partial(handle_delete, task["_id"], app))
        delete_btn.grid(row=tasks.index(task), column=2)

    add_btn = tk.Button( master=frame,text="Add Task",command=lambda: show_add_task_frame(app))
    add_btn.grid(row=len(tasks) + 1, column=1)
    frame.tkraise()