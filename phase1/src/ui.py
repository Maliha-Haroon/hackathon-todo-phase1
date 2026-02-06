# [Task]: T-018
# [From]: specify.md §Journey 5: Mark Task Complete, plan.md §TodoUI Class

from typing import Tuple
from todo_manager import TodoManager


class TodoUI:
    """
    Handles user interaction and display for the Todo application.
    
    Responsibilities:
    - Display menus and prompts
    - Handle user input
    - Format and display task information
    """
    
    def __init__(self, manager: TodoManager):
        """
        Initialize the TodoUI with a TodoManager instance.
        
        Args:
            manager (TodoManager): The TodoManager instance to interact with
        """
        self.manager = manager
    
    def show_menu(self) -> None:
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*50)
        print("           TODO CONSOLE APP")
        print("="*50)
        print("What would you like to do?")
        print("1. ➕ Add Task")
        print("2. 📋 View All Tasks")
        print("3. ✏️  Update Task")
        print("4. 🗑️  Delete Task")
        print("5. ✅ Mark Task Complete/Incomplete")
        print("6. 🚪 Exit")
        print("-"*50)
    
    def get_menu_choice(self) -> str:
        """
        Get and validate the user's menu choice.
        
        Returns:
            str: The validated menu choice
        """
        while True:
            try:
                choice = input("Enter your choice (1-6): ").strip()
                
                # Validate the choice
                if choice in ['1', '2', '3', '4', '5', '6']:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                return '6'  # Return '6' to exit
            except EOFError:
                print("\n\nOperation cancelled.")
                return '6'  # Return '6' to exit
    
    def prompt_task_details(self) -> Tuple[str, str]:
        """
        Prompt the user for task title and description.
        
        Returns:
            tuple[str, str]: A tuple containing the title and description
        """
        while True:
            try:
                title = input("Enter task title (required): ").strip()
                
                if not title:
                    print("Title cannot be empty. Please try again.")
                    continue
                
                if len(title) > 200:
                    print("Title is too long. Please enter a title with 200 characters or less.")
                    continue
                
                break
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                return "", ""
            except EOFError:
                print("\n\nOperation cancelled.")
                return "", ""
        
        try:
            description = input("Enter task description (optional): ")
            
            if len(description) > 1000:
                print("Description is too long. Truncating to 1000 characters.")
                description = description[:1000]
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            description = ""
        except EOFError:
            print("\n\nOperation cancelled.")
            description = ""
        
        return title, description
    
    def handle_add_task(self) -> None:
        """
        Handle the process of adding a new task.
        """
        print("\n➕ Adding New Task...")
        
        # Get task details from user
        title, description = self.prompt_task_details()
        
        # Check if operation was cancelled
        if not title:
            print("❌ Add task operation cancelled.")
            return
        
        try:
            # Add the task using the manager
            task = self.manager.add_task(title, description)
            
            # Confirm the task was added
            print(f"✅ Task added successfully! Your task ID is: {task['id']}")
        except ValueError as e:
            print(f"❌ Error adding task: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
    
    def display_tasks(self, tasks: list) -> None:
        """
        Display a formatted list of tasks.
        
        Args:
            tasks (list): List of task dictionaries to display
        """
        if not tasks:
            print("\n📭 No tasks found. Your list is empty!")
            return
        
        print("\n📋 Task List:")
        print("=" * 80)
        print(f"{'ID':<4} {'Status':<10} {'Title':<30} {'Description'}")
        print("-" * 80)
        
        for task in tasks:
            status = "✅ Done" if task['completed'] else "⏳ Pending"
            title = task['title'][:27] + "..." if len(task['title']) > 30 else task['title']
            description = task['description'][:35] + "..." if len(task['description']) > 35 else task['description']
            print(f"{task['id']:<4} {status:<10} {title:<30} {description}")
        print("=" * 80)
    
    def handle_view_tasks(self) -> None:
        """
        Handle the process of viewing all tasks.
        """
        print("\n📋 Retrieving all tasks...")
        
        # Get all tasks from the manager
        tasks = self.manager.get_all_tasks()
        
        # Display the tasks
        self.display_tasks(tasks)
    
    def handle_update_task(self) -> None:
        """
        Handle the process of updating a task.
        """
        print("\n✏️  Updating Task...")
        
        # Get task ID from user
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            
            if not task_id_input:
                print("❌ Update operation cancelled.")
                return
            
            task_id = int(task_id_input)
        except ValueError:
            print("❌ Invalid task ID. Please enter a number.")
            return
        except KeyboardInterrupt:
            print("\n\n❌ Update operation cancelled by user.")
            return
        except EOFError:
            print("\n\n❌ Update operation cancelled.")
            return
        
        # Check if task exists
        task = self.manager.get_task(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found.")
            return
        
        print(f"📝 Current task: {task['title']}")
        
        # Ask what to update
        try:
            print("💡 Leave blank to keep current value.")
            new_title = input(f"📝 New title (current: '{task['title']}'): ").strip()
            
            if new_title == "":
                new_title = None  # Keep current title
            elif len(new_title) > 200:
                print("❌ Title is too long. Update cancelled.")
                return
            
            new_description = input(f"📝 New description (current: '{task['description']}'): ")
            
            if new_description == "":
                new_description = None  # Keep current description
            elif len(new_description) > 1000:
                print("❌ Description is too long. Update cancelled.")
                return
            
            # Update the task
            success = self.manager.update_task(task_id, new_title, new_description)
            
            if success:
                print(f"✅ Task {task_id} updated successfully!")
            else:
                print(f"❌ Failed to update task {task_id}.")
        except KeyboardInterrupt:
            print("\n\n❌ Update operation cancelled by user.")
        except EOFError:
            print("\n\n❌ Update operation cancelled.")
    
    def handle_delete_task(self) -> None:
        """
        Handle the process of deleting a task.
        """
        print("\n🗑️  Deleting Task...")
        
        # Get task ID from user
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            
            if not task_id_input:
                print("❌ Delete operation cancelled.")
                return
            
            task_id = int(task_id_input)
        except ValueError:
            print("❌ Invalid task ID. Please enter a number.")
            return
        except KeyboardInterrupt:
            print("\n\n❌ Delete operation cancelled by user.")
            return
        except EOFError:
            print("\n\n❌ Delete operation cancelled.")
            return
        
        # Check if task exists
        task = self.manager.get_task(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found.")
            return
        
        print(f"📝 Task to delete: {task['title']}")
        
        # Confirm deletion
        try:
            confirm = input("❓ Are you sure you want to delete this task? (y/N): ").strip().lower()
            
            if confirm not in ['y', 'yes']:
                print("❌ Delete operation cancelled.")
                return
            
            # Delete the task
            success = self.manager.delete_task(task_id)
            
            if success:
                print(f"✅ Task {task_id} deleted successfully!")
            else:
                print(f"❌ Failed to delete task {task_id}.")
        except KeyboardInterrupt:
            print("\n\n❌ Delete operation cancelled by user.")
        except EOFError:
            print("\n\n❌ Delete operation cancelled.")
    
    def handle_complete_task(self) -> None:
        """
        Handle the process of marking a task as complete/incomplete.
        """
        print("\n✅ Toggling Task Completion Status...")
        
        # Get task ID from user
        try:
            task_id_input = input("Enter task ID to toggle completion status: ").strip()
            
            if not task_id_input:
                print("❌ Mark complete operation cancelled.")
                return
            
            task_id = int(task_id_input)
        except ValueError:
            print("❌ Invalid task ID. Please enter a number.")
            return
        except KeyboardInterrupt:
            print("\n\n❌ Mark complete operation cancelled by user.")
            return
        except EOFError:
            print("\n\n❌ Mark complete operation cancelled.")
            return
        
        # Check if task exists
        task = self.manager.get_task(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found.")
            return
        
        # Toggle completion status
        success = self.manager.toggle_complete(task_id)
        
        if success:
            status = "✅ completed" if task['completed'] else "⏳ incomplete"
            print(f"✅ Task {task_id} marked as {status}!")
        else:
            print(f"❌ Failed to toggle completion status for task {task_id}.")