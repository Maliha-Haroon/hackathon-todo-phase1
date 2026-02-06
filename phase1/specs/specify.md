# Todo Console App - Specification (WHAT)

## Project Overview
A command-line todo application for managing tasks in memory.

## User Journeys

### Journey 1: Add a Task
**As a user**
- I want to add a new todo task
- So that I can track things I need to do

**Acceptance Criteria:**
- User enters "add" command
- System prompts for task title (required)
- System prompts for task description (optional)
- System generates unique ID automatically
- System confirms task was added
- New task appears in task list

### Journey 2: View All Tasks
**As a user**
- I want to see all my tasks
- So that I know what needs to be done

**Acceptance Criteria:**
- User enters "list" command
- System displays all tasks with:
  - Task ID
  - Title
  - Description
  - Completion status (✓ or ✗)
- Empty list shows helpful message

### Journey 3: Update a Task
**As a user**
- I want to update a task's details
- So that I can correct mistakes or add information

**Acceptance Criteria:**
- User enters "update" command
- System prompts for task ID
- System validates ID exists
- System allows updating title and/or description
- System confirms update
- Changes visible in task list

### Journey 4: Delete a Task
**As a user**
- I want to delete a task
- So that I can remove tasks I no longer need

**Acceptance Criteria:**
- User enters "delete" command
- System prompts for task ID
- System validates ID exists
- System asks for confirmation
- System removes task
- System confirms deletion

### Journey 5: Mark Task Complete
**As a user**
- I want to mark tasks as complete
- So that I can track my progress

**Acceptance Criteria:**
- User enters "complete" command
- System prompts for task ID
- System validates ID exists
- System toggles completion status
- System shows updated status

## Features

### F1: Add Task
- **Input:** Title (1-200 chars), Description (0-1000 chars)
- **Output:** Confirmation with new task ID
- **Validation:** Title cannot be empty

### F2: View Tasks
- **Input:** None
- **Output:** Formatted list of all tasks
- **Display:** ID, Title (truncated if long), Status indicator

### F3: Update Task
- **Input:** Task ID, New title (optional), New description (optional)
- **Output:** Confirmation of update
- **Validation:** ID must exist, at least one field updated

### F4: Delete Task
- **Input:** Task ID
- **Output:** Confirmation of deletion
- **Validation:** ID must exist, user confirms action

### F5: Complete Task
- **Input:** Task ID
- **Output:** New completion status
- **Validation:** ID must exist
- **Behavior:** Toggles between complete/incomplete

## Menu System

### Main Menu Options:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

## Error Handling

- Invalid menu choice → Show valid options
- Invalid task ID → Show helpful error message
- Empty title → Prompt again
- Confirmation prompts → Accept y/n only

## Data Model

### Task Object:
```python
{
    'id': int,          # Auto-incrementing, starting at 1
    'title': str,       # Required, 1-200 characters
    'description': str, # Optional, max 1000 characters
    'completed': bool   # Default False
}
```

### Storage:
- List of task dictionaries
- In-memory only (data lost on exit)