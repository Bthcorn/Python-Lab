import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Task Management App")

# Create a Treeview widget to display tasks
tree = ttk.Treeview(app, columns=("Task", "Due Date"), show="headings")
tree.heading("#1", text="Task")
tree.heading("#2", text="Due Date")
tree.pack()

# Input fields for task details
task_entry = tk.Entry(app, width=30)
due_date_entry = tk.Entry(app, width=15)
task_entry.pack()
due_date_entry.pack()

# Buttons to add and delete tasks
add_button = tk.Button(app, text="Add Task")
delete_button = tk.Button(app, text="Delete Task")
add_button.pack()
delete_button.pack()

app.mainloop()



