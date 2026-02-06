# Todo Console App - Tasks Breakdown

## Implementation Checklist

### Phase 1: Project Setup
- [T-001] Create project structure and folders
- [T-002] Create `__init__.py` in src folder
- [T-003] Set up basic README.md

### Phase 2: TodoManager Implementation
- [T-004] Create TodoManager class skeleton
- [T-005] Implement `add_task()` method
- [T-006] Implement `get_all_tasks()` method
- [T-007] Implement `get_task()` method
- [T-008] Implement `update_task()` method
- [T-009] Implement `delete_task()` method
- [T-010] Implement `toggle_complete()` method

### Phase 3: UI Implementation
- [T-011] Create TodoUI class skeleton
- [T-012] Implement `show_menu()` method
- [T-013] Implement `get_menu_choice()` method
- [T-014] Implement `handle_add_task()` method
- [T-015] Implement `handle_view_tasks()` method
- [T-016] Implement `handle_update_task()` method
- [T-017] Implement `handle_delete_task()` method
- [T-018] Implement `handle_complete_task()` method
- [T-019] Implement `display_tasks()` method

### Phase 4: Main Application
- [T-020] Create main.py with application loop
- [T-021] Integrate TodoManager and TodoUI
- [T-022] Add graceful exit handling

### Phase 5: Testing & Polish
- [T-023] Test all CRUD operations
- [T-024] Test error handling
- [T-025] Polish user messages and formatting

---

## Task Details

### T-001: Create Project Structure
**From:** constitution.md §Project Structure
**Description:** Create the folder structure for the project
**Preconditions:** None
**Expected Output:** 
- `src/` folder exists
- `specs/` folder exists
**Artifacts:** Folder structure

---

### T-004: Create TodoManager Class Skeleton
**From:** plan.md §TodoManager Class
**Description:** Create the basic TodoManager class with __init__ method
**Preconditions:** T-001 completed
**Expected Output:**
```python
class TodoManager:
    def __init__(self):
        self._tasks: list[dict] = []
        self._next_id: int = 1
```
**Artifacts:** `src/todo_manager.py`

---

### T-005: Implement add_task() Method
**From:** specify.md §F1: Add Task
**Description:** Implement method to add a new task
**Preconditions:** T-004 completed
**Expected Output:**
```python
def add_task(self, title: str, description: str = "") -> dict:
    # Validate title
    # Create task dict with auto-incrementing ID
    # Add to _tasks list
    # Return created task
```
**Test:**
- Add task with title only
- Add task with title and description
- Verify ID auto-increments

**Artifacts:** Updated `src/todo_manager.py`

---

### T-006: Implement get_all_tasks() Method
**From:** specify.md §F2: View Tasks
**Description:** Return all tasks from memory
**Preconditions:** T-005 completed
**Expected Output:**
```python
def get_all_tasks(self) -> list[dict]:
    return self._tasks.copy()  # Return copy to prevent external modification
```
**Test:**
- Empty list returns []
- Multiple tasks return complete list

**Artifacts:** Updated `src/todo_manager.py`

---

### T-007: Implement get_task() Method
**From:** plan.md §TodoManager Class
**Description:** Find and return a single task by ID
**Preconditions:** T-005 completed
**Expected Output:**
```python
def get_task(self, task_id: int) -> dict | None:
    # Search _tasks for matching ID
    # Return task dict or None
```
**Test:**
- Valid ID returns task
- Invalid ID returns None

**Artifacts:** Updated `src/todo_manager.py`

---

### T-008: Implement update_task() Method
**From:** specify.md §F3: Update Task
**Description:** Update task title and/or description
**Preconditions:** T-007 completed
**Expected Output:**
```python
def update_task(self, task_id: int, title: str | None = None, 
               description: str | None = None) -> bool:
    # Find task
    # Update provided fields
    # Return success/failure
```
**Test:**
- Update title only
- Update description only
- Update both
- Invalid ID returns False

**Artifacts:** Updated `src/todo_manager.py`

---

### T-009: Implement delete_task() Method
**From:** specify.md §F4: Delete Task
**Description:** Remove a task from the list
**Preconditions:** T-007 completed
**Expected Output:**
```python
def delete_task(self, task_id: int) -> bool:
    # Find and remove task
    # Return success/failure
```
**Test:**
- Delete existing task
- Attempt to delete non-existent task

**Artifacts:** Updated `src/todo_manager.py`

---

### T-010: Implement toggle_complete() Method
**From:** specify.md §F5: Complete Task
**Description:** Toggle task completion status
**Preconditions:** T-007 completed
**Expected Output:**
```python
def toggle_complete(self, task_id: int) -> bool:
    # Find task
    # Toggle 'completed' field
    # Return new status
```
**Test:**
- Toggle from incomplete to complete
- Toggle from complete to incomplete

**Artifacts:** Updated `src/todo_manager.py`

---

### T-011: Create TodoUI Class Skeleton
**From:** plan.md §TodoUI Class
**Description:** Create the basic UI class structure
**Preconditions:** T-010 completed (TodoManager done)
**Expected Output:**
```python
class TodoUI:
    def __init__(self, manager: TodoManager):
        self.manager = manager
```
**Artifacts:** `src/ui.py`

---

### T-012: Implement show_menu() Method
**From:** specify.md §Menu System
**Description:** Display the main menu
**Expected Output:**
```python
def show_menu(self) -> None:
    print("\n=== Todo Manager ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
```
**Artifacts:** Updated `src/ui.py`

---

### T-020: Create main.py Application Loop
**From:** plan.md §Main Application
**Description:** Create the main entry point with application loop
**Preconditions:** All TodoManager and TodoUI tasks completed
**Expected Output:**
```python
from src.todo_manager import TodoManager
from src.ui import TodoUI

def main():
    manager = TodoManager()
    ui = TodoUI(manager)
    
    while True:
        ui.show_menu()
        choice = ui.get_menu_choice()
        
        if choice == '1':
            ui.handle_add_task()
        elif choice == '2':
            ui.handle_view_tasks()
        # ... etc
        elif choice == '6':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
```
**Artifacts:** `src/main.py`