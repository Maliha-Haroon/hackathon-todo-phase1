# [Task]: T-023
# [From]: tasks.md §T-023, specify.md §Features

"""
Test script to verify all CRUD operations for the Todo Console App.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_manager import TodoManager


def test_crud_operations():
    """
    Test all CRUD operations for the TodoManager.
    """
    print("Testing CRUD Operations for Todo Console App...")
    print("="*50)
    
    # Initialize TodoManager
    manager = TodoManager()
    
    # Test 1: Add tasks (CREATE)
    print("\n1. Testing ADD operations:")
    task1 = manager.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added task: ID={task1['id']}, Title='{task1['title']}'")
    
    task2 = manager.add_task("Walk the dog")
    print(f"   Added task: ID={task2['id']}, Title='{task2['title']}'")
    
    task3 = manager.add_task("Finish project", "Complete the todo app implementation")
    print(f"   Added task: ID={task3['id']}, Title='{task3['title']}'")
    
    # Test 2: View all tasks (READ)
    print("\n2. Testing VIEW ALL operations:")
    all_tasks = manager.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        status = "[X]" if task['completed'] else "[ ]"
        print(f"   ID={task['id']}, Title='{task['title']}', Status={status}")
    
    # Test 3: Get specific task (READ)
    print("\n3. Testing GET SPECIFIC TASK operations:")
    retrieved_task = manager.get_task(task1['id'])
    if retrieved_task:
        print(f"   Retrieved task: ID={retrieved_task['id']}, Title='{retrieved_task['title']}'")
    else:
        print("   Failed to retrieve task")
    
    # Test 4: Update task (UPDATE)
    print("\n4. Testing UPDATE operations:")
    update_success = manager.update_task(task2['id'], "Walk the cat", "Take Fluffy for a walk")
    if update_success:
        updated_task = manager.get_task(task2['id'])
        print(f"   Updated task: ID={updated_task['id']}, Title='{updated_task['title']}'")
    else:
        print("   Failed to update task")
    
    # Test 5: Toggle completion status (UPDATE)
    print("\n5. Testing TOGGLE COMPLETION operations:")
    toggle_success = manager.toggle_complete(task1['id'])
    if toggle_success:
        toggled_task = manager.get_task(task1['id'])
        status = "[X]" if toggled_task['completed'] else "[ ]"
        print(f"   Toggled task: ID={toggled_task['id']}, Status={status}")
    else:
        print("   Failed to toggle task completion")
    
    # Test 6: Delete task (DELETE)
    print("\n6. Testing DELETE operations:")
    delete_success = manager.delete_task(task3['id'])
    if delete_success:
        print(f"   Deleted task with ID={task3['id']}")
    else:
        print("   Failed to delete task")
    
    # Verify deletion
    remaining_tasks = manager.get_all_tasks()
    print(f"   Remaining tasks after deletion: {len(remaining_tasks)}")
    
    # Test 7: Edge cases
    print("\n7. Testing EDGE CASES:")
    
    # Try to get a non-existent task
    nonexistent_task = manager.get_task(999)
    if nonexistent_task is None:
        print("   + Correctly returned None for non-existent task")
    else:
        print("   - Failed to return None for non-existent task")
    
    # Try to update a non-existent task
    update_nonexistent = manager.update_task(999, "Non-existent task")
    if not update_nonexistent:
        print("   + Correctly returned False when updating non-existent task")
    else:
        print("   - Failed to return False when updating non-existent task")
    
    # Try to delete a non-existent task
    delete_nonexistent = manager.delete_task(999)
    if not delete_nonexistent:
        print("   + Correctly returned False when deleting non-existent task")
    else:
        print("   - Failed to return False when deleting non-existent task")
    
    # Try to toggle completion of a non-existent task
    toggle_nonexistent = manager.toggle_complete(999)
    if not toggle_nonexistent:
        print("   + Correctly returned False when toggling non-existent task")
    else:
        print("   - Failed to return False when toggling non-existent task")
    
    print("\n" + "="*50)
    print("CRUD operations testing completed!")


if __name__ == "__main__":
    test_crud_operations()