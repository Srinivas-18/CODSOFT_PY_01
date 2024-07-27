import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_number = 0

        # Create GUI components
        self.task_list_label = tk.Label(root, text="To-Do List:")
        self.task_list_label.pack()

        self.task_list = tk.Listbox(root, width=40, height=10)
        self.task_list.pack()

        self.task_entry_label = tk.Label(root, text="Enter a new task:")
        self.task_entry_label.pack()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(self.task_number, task)
            self.task_number += 1
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
            self.task_number -= 1
        except IndexError:
            messagebox.showerror("Error", "Please select a task to delete.")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.task_entry.get()
            if task != "":
                self.tasks[task_index] = task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a new task.")
        except IndexError:
            messagebox.showerror("Error", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    todo_list = ToDoList(root)
    root.mainloop()