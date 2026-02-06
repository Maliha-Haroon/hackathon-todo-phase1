# Todo Console App - Technical Plan (HOW)

## Architecture

### Component Breakdown

#### 1. Main Application (`main.py`)
- Entry point
- Displays main menu
- Routes commands to appropriate handlers
- Manages application loop

#### 2. Todo Manager (`todo_manager.py`)
- **Class:** `TodoManager`
- **Responsibility:** Business logic and data management
- **Methods:**
  - `add_task(title: str, description: str) -> dict`
  - `get_all_tasks() -> list[dict]`
  - `get_task(task_id: int) -> dict | None`
  - `update_task(task_id: int, title: str | None, description: str | None) -> bool`
  - `delete_task(task_id: int) -> bool`
  - `toggle_complete(task_id: int) -> bool`

#### 3. User Interface (`ui.py`)
- **Class:** `TodoUI`
- **Responsibility:** User interaction and display
- **Methods:**
  - `show_menu() -> None`
  - `get_menu_choice() -> str`
  - `prompt_task_details() -> tuple[str, str]`
  - `display_tasks(tasks: list[dict]) -> None`
  - `confirm_action(message: str) -> bool`

## Data Flow

### Add Task Flow: