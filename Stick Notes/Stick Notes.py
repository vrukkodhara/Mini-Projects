#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3
from tkinter import *

# Function to create the tasks table if it doesn't exist
def create_table():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, completed INTEGER)")
    connection.commit()
    connection.close()

# Function to insert a task into the database
def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
        
        # Insert task into the database
        connection = sqlite3.connect("todo.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, 0))
        connection.commit()
        connection.close()

# Function to delete a task from the database
def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
        
        # Delete task from the database
        connection = sqlite3.connect("todo.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (selected_task[0]+1,))  # SQLite uses 1-based indexing for AUTOINCREMENT
        connection.commit()
        connection.close()

# Function to mark a task as complete and update the database
def complete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.itemconfig(selected_task, {'fg': 'gray'})
        
        # Mark task as complete in the database
        connection = sqlite3.connect("todo.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE tasks SET completed=? WHERE id=?", (1, selected_task[0]+1))  # SQLite uses 1-based indexing for AUTOINCREMENT
        connection.commit()
        connection.close()

# Function to retrieve tasks from the database and populate the listbox
def load_tasks():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    
    for task in tasks:
        if task[2] == 1:  # Check if the task is completed
            listbox.insert(END, task[1])
            listbox.itemconfig(END-1, {'fg': 'gray'})
        else:
            listbox.insert(END, task[1])

# Create the tasks table
create_table()

# GUI code
root = Tk()
root.title('To-Do List')

frame = Frame(root, bg='#3498db')
frame.pack(pady=10)

entry = Entry(frame, width=40, font=('Helvetica', 12), bg='#ecf0f1')
entry.grid(row=0, column=0, padx=5)

add_button = Button(frame, text='Add Task', command=add_task, font=('Helvetica', 10), bg='#2ecc71', fg='white')
add_button.grid(row=0, column=1, padx=5)

listbox = Listbox(root, selectbackground='#a6a6a6', selectmode=SINGLE, height=10, width=50, font=('Helvetica', 12), bg='#ecf0f1')
listbox.pack(pady=10)

delete_button = Button(root, text='Delete Task', command=delete_task, font=('Helvetica', 10), bg='#e74c3c', fg='white')
delete_button.pack(pady=5)

complete_button = Button(root, text='Complete Task', command=complete_task, font=('Helvetica', 10), bg='#3498db', fg='white')
complete_button.pack(pady=5)

# Load tasks from the database when the application starts
load_tasks()

root.mainloop()


# In[ ]:




