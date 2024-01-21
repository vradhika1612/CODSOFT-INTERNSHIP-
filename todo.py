import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")

        self.tasks = []
        self.load_tasks()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.refresh_tasks()

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.pack()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file).get("tasks", [])
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump({"tasks": self.tasks}, file)

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[X]" if task["completed"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['description']}")

    def add_task(self):
        description = simpledialog.askstring("Input", "Enter task description:")
        if description:
            self.tasks.append({"description": description, "completed": False})
            self.save_tasks()
            self.refresh_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            task = self.tasks[selected_index]
            task["completed"] = not task["completed"]
            self.save_tasks()
            self.refresh_tasks()
        else:
            messagebox.showinfo("Error", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
