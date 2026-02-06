# [Task]: Interactive GUI UI
# [From]: specify.md §User Experience, plan.md §UI Enhancement

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from todo_manager import TodoManager


class TodoGUI:
    """
    Graphical User Interface for the Todo Console App.
    Provides an interactive UI using tkinter.
    """
    
    def __init__(self, root):
        """
        Initialize the GUI with a root window.
        
        Args:
            root: The main tkinter window
        """
        self.root = root
        self.root.title("Todo Console App - GUI Version")
        self.root.geometry("700x500")
        
        # Initialize the TodoManager
        self.manager = TodoManager()
        
        # Set up the GUI elements
        self.setup_gui()
        
        # Refresh the task list
        self.refresh_task_list()
    
    def setup_gui(self):
        """
        Set up all GUI elements.
        """
        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)
        
        # Title label
        title_label = tk.Label(self.root, text="Todo Console App", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=10, sticky="n")
        
        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=10, sticky="ew")
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        
        # Buttons for different operations
        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.update_button = tk.Button(button_frame, text="Update Task", command=self.update_task, bg="#2196F3", fg="white")
        self.update_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.complete_button = tk.Button(button_frame, text="Toggle Complete", command=self.toggle_complete, bg="#FF9800", fg="white")
        self.complete_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#F44336", fg="white")
        self.delete_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        
        self.refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh_task_list, bg="#9E9E9E", fg="white")
        self.refresh_button.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        
        # Task list frame
        task_frame = tk.Frame(self.root)
        task_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        task_frame.columnconfigure(0, weight=1)
        task_frame.rowconfigure(0, weight=1)
        
        # Create the treeview for displaying tasks
        columns = ('ID', 'Title', 'Description', 'Status')
        self.task_tree = ttk.Treeview(task_frame, columns=columns, show='headings', height=15)
        
        # Define headings
        self.task_tree.heading('ID', text='ID')
        self.task_tree.heading('Title', text='Title')
        self.task_tree.heading('Description', text='Description')
        self.task_tree.heading('Status', text='Status')
        
        # Define column widths
        self.task_tree.column('ID', width=50)
        self.task_tree.column('Title', width=150)
        self.task_tree.column('Description', width=250)
        self.task_tree.column('Status', width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(task_frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        self.task_tree.configure(yscroll=scrollbar.set)
        
        # Pack the treeview and scrollbar
        self.task_tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Bind selection event
        self.task_tree.bind('<<TreeviewSelect>>', self.on_task_select)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.status_var.set("Ready")
    
    def refresh_task_list(self):
        """
        Refresh the task list display.
        """
        # Clear current items
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        
        # Get all tasks
        tasks = self.manager.get_all_tasks()
        
        # Insert tasks into the treeview
        for task in tasks:
            status_text = "Completed" if task['completed'] else "Pending"
            self.task_tree.insert('', tk.END, values=(task['id'], task['title'], task['description'], status_text))
        
        # Update status
        self.status_var.set(f"Showing {len(tasks)} tasks")
    
    def on_task_select(self, event):
        """
        Handle task selection event.
        """
        # Enable buttons that require a selected task
        selection = self.task_tree.selection()
        if selection:
            self.update_button.config(state='normal')
            self.delete_button.config(state='normal')
            self.complete_button.config(state='normal')
        else:
            self.update_button.config(state='disabled')
            self.delete_button.config(state='disabled')
            self.complete_button.config(state='disabled')
    
    def get_selected_task_id(self):
        """
        Get the ID of the currently selected task.
        
        Returns:
            int or None: The task ID if a task is selected, None otherwise
        """
        selection = self.task_tree.selection()
        if selection:
            item = self.task_tree.item(selection[0])
            task_id = item['values'][0]
            return int(task_id)
        return None
    
    def add_task(self):
        """
        Handle adding a new task.
        """
        # Create a dialog for task details
        dialog = TaskDialog(self.root, "Add New Task")
        
        if dialog.result:
            title, description = dialog.result
            try:
                task = self.manager.add_task(title, description)
                messagebox.showinfo("Success", f"Task added successfully! ID: {task['id']}")
                self.refresh_task_list()
            except ValueError as e:
                messagebox.showerror("Error", f"Error adding task: {e}")
    
    def update_task(self):
        """
        Handle updating a task.
        """
        task_id = self.get_selected_task_id()
        if not task_id:
            messagebox.showwarning("Warning", "Please select a task to update.")
            return
        
        # Get the current task details
        task = self.manager.get_task(task_id)
        if not task:
            messagebox.showerror("Error", f"Task with ID {task_id} not found.")
            return
        
        # Create a dialog with current values
        dialog = TaskDialog(self.root, "Update Task", task['title'], task['description'])
        
        if dialog.result:
            new_title, new_description = dialog.result
            try:
                success = self.manager.update_task(task_id, new_title, new_description)
                if success:
                    messagebox.showinfo("Success", f"Task {task_id} updated successfully!")
                    self.refresh_task_list()
                else:
                    messagebox.showerror("Error", f"Failed to update task {task_id}.")
            except ValueError as e:
                messagebox.showerror("Error", f"Error updating task: {e}")
    
    def delete_task(self):
        """
        Handle deleting a task.
        """
        task_id = self.get_selected_task_id()
        if not task_id:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
        
        # Confirm deletion
        confirmed = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete task {task_id}?")
        if confirmed:
            success = self.manager.delete_task(task_id)
            if success:
                messagebox.showinfo("Success", f"Task {task_id} deleted successfully!")
                self.refresh_task_list()
            else:
                messagebox.showerror("Error", f"Failed to delete task {task_id}.")
    
    def toggle_complete(self):
        """
        Handle toggling task completion status.
        """
        task_id = self.get_selected_task_id()
        if not task_id:
            messagebox.showwarning("Warning", "Please select a task to toggle completion status.")
            return
        
        # Get the current task details to show status
        task = self.manager.get_task(task_id)
        if not task:
            messagebox.showerror("Error", f"Task with ID {task_id} not found.")
            return
        
        success = self.manager.toggle_complete(task_id)
        if success:
            new_status = "completed" if task['completed'] else "incomplete"
            messagebox.showinfo("Success", f"Task {task_id} marked as {new_status}!")
            self.refresh_task_list()
        else:
            messagebox.showerror("Error", f"Failed to toggle completion status for task {task_id}.")


class TaskDialog:
    """
    A dialog for entering task details.
    """
    
    def __init__(self, parent, title, initial_title="", initial_description=""):
        """
        Initialize the dialog.
        
        Args:
            parent: The parent window
            title: The dialog title
            initial_title: Initial value for the title field
            initial_description: Initial value for the description field
        """
        self.parent = parent
        self.result = None
        
        # Create the dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x200")
        self.dialog.resizable(False, False)
        
        # Center the dialog over the parent
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Position the dialog in the center of the screen
        self.dialog.geometry("+%d+%d" % (
            parent.winfo_rootx() + 50,
            parent.winfo_rooty() + 50
        ))
        
        # Create the GUI elements
        self.create_widgets(initial_title, initial_description)
        
        # Focus on the title field
        self.title_entry.focus_set()
        
        # Bind Enter key to OK
        self.dialog.bind('<Return>', lambda event: self.ok())
        
        # Wait for the dialog to close
        self.dialog.wait_window(self.dialog)
    
    def create_widgets(self, initial_title, initial_description):
        """
        Create the widgets for the dialog.
        """
        # Main frame
        main_frame = tk.Frame(self.dialog, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label and entry
        tk.Label(main_frame, text="Title (required):").grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.title_entry = tk.Entry(main_frame, width=50)
        self.title_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        self.title_entry.insert(0, initial_title)
        
        # Description label and entry
        tk.Label(main_frame, text="Description (optional):").grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.description_entry = tk.Entry(main_frame, width=50)
        self.description_entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        self.description_entry.insert(0, initial_description)
        
        # Button frame
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        # OK and Cancel buttons
        self.ok_button = tk.Button(button_frame, text="OK", command=self.ok, width=10)
        self.ok_button.pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(button_frame, text="Cancel", command=self.cancel, width=10).pack(side=tk.LEFT)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
    
    def ok(self, event=None):
        """
        Handle OK button click.
        """
        title = self.title_entry.get().strip()
        
        if not title:
            messagebox.showerror("Error", "Title cannot be empty.")
            return
        
        if len(title) > 200:
            messagebox.showerror("Error", "Title cannot exceed 200 characters.")
            return
        
        description = self.description_entry.get()
        if len(description) > 1000:
            messagebox.showerror("Error", "Description cannot exceed 1000 characters.")
            return
        
        self.result = (title, description)
        self.dialog.destroy()
    
    def cancel(self, event=None):
        """
        Handle Cancel button click.
        """
        self.result = None
        self.dialog.destroy()


def run_gui():
    """
    Run the GUI application.
    """
    root = tk.Tk()
    app = TodoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()