# [Task]: T-010
# [From]: specify.md §F5: Complete Task, plan.md §TodoManager Class

from typing import Dict, List, Optional


class TodoManager:
    """
    Manages todo tasks in memory.
    
    Responsibilities:
    - Store tasks in memory
    - Generate unique IDs for tasks
    - Provide methods to manipulate tasks
    """
    
    def __init__(self):
        """Initialize the TodoManager with an empty task list and starting ID."""
        self._tasks: List[Dict] = []
        self._next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Dict:
        """
        Add a new task to the task list.
        
        Args:
            title (str): The title of the task (required, 1-200 characters)
            description (str): The description of the task (optional, max 1000 characters)
            
        Returns:
            dict: The created task dictionary
            
        Raises:
            ValueError: If title is empty or exceeds character limits
        """
        # Validate title
        if not title or len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        
        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        
        if len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")
        
        # Create task dictionary with auto-incrementing ID
        task = {
            'id': self._next_id,
            'title': title.strip(),
            'description': description,
            'completed': False
        }
        
        # Add to tasks list
        self._tasks.append(task)
        
        # Increment the next ID
        self._next_id += 1
        
        # Return the created task
        return task
    
    def get_all_tasks(self) -> List[Dict]:
        """
        Return all tasks from memory.
        
        Returns:
            list[dict]: A copy of the tasks list to prevent external modification
        """
        # Return a copy of the tasks list to prevent external modification
        return self._tasks.copy()
    
    def get_task(self, task_id: int) -> Optional[Dict]:
        """
        Find and return a single task by ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            dict | None: The task dictionary if found, None otherwise
        """
        # Search _tasks for matching ID
        for task in self._tasks:
            if task['id'] == task_id:
                return task
        # Return None if task not found
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, 
                   description: Optional[str] = None) -> bool:
        """
        Update task title and/or description.
        
        Args:
            task_id (int): The ID of the task to update
            title (str | None): New title for the task (optional)
            description (str | None): New description for the task (optional)
            
        Returns:
            bool: True if update was successful, False if task not found
        """
        # Find the task to update
        task = self.get_task(task_id)
        
        # Return False if task doesn't exist
        if task is None:
            return False
        
        # Update title if provided
        if title is not None:
            if not title or len(title.strip()) == 0:
                raise ValueError("Title cannot be empty")
            if len(title) > 200:
                raise ValueError("Title cannot exceed 200 characters")
            task['title'] = title.strip()
        
        # Update description if provided
        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description cannot exceed 1000 characters")
            task['description'] = description
        
        # Return True to indicate successful update
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the list.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if deletion was successful, False if task not found
        """
        # Find the index of the task with the given ID
        for i, task in enumerate(self._tasks):
            if task['id'] == task_id:
                # Remove the task from the list
                del self._tasks[i]
                return True
        # Return False if task not found
        return False
    
    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle task completion status.
        
        Args:
            task_id (int): The ID of the task to toggle
            
        Returns:
            bool: True if toggle was successful, False if task not found
        """
        # Find the task to toggle
        task = self.get_task(task_id)
        
        # Return False if task doesn't exist
        if task is None:
            return False
        
        # Toggle the 'completed' field
        task['completed'] = not task['completed']
        
        # Return True to indicate successful toggle
        return True

