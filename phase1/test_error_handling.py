# [Task]: T-024
# [From]: tasks.md §T-024, specify.md §Error Handling

"""
Test script to verify error handling for the Todo Console App.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_manager import TodoManager


def test_error_handling():
    """
    Test error handling for the TodoManager.
    """
    print("Testing Error Handling for Todo Console App...")
    print("="*50)
    
    # Initialize TodoManager
    manager = TodoManager()
    
    # Test 1: Add task with empty title (should raise ValueError)
    print("\n1. Testing ADD with invalid inputs:")
    try:
        manager.add_task("")
        print("   - FAILED: Should have raised ValueError for empty title")
    except ValueError as e:
        print(f"   + PASSED: Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"   - FAILED: Raised unexpected exception: {e}")
    
    # Test 2: Add task with title exceeding 200 characters
    long_title = "A" * 201
    try:
        manager.add_task(long_title)
        print("   - FAILED: Should have raised ValueError for title too long")
    except ValueError as e:
        print(f"   + PASSED: Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"   - FAILED: Raised unexpected exception: {e}")
    
    # Test 3: Add task with description exceeding 1000 characters
    long_desc = "A" * 1001
    try:
        manager.add_task("Valid title", long_desc)
        print("   - FAILED: Should have raised ValueError for description too long")
    except ValueError as e:
        print(f"   + PASSED: Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"   - FAILED: Raised unexpected exception: {e}")
    
    # Test 4: Update with empty title (should raise ValueError)
    task = manager.add_task("Initial title")
    print(f"\n   Added task with ID: {task['id']}")
    
    try:
        manager.update_task(task['id'], "")
        print("   - FAILED: Should have raised ValueError for empty title in update")
    except ValueError as e:
        print(f"   + PASSED: Correctly raised ValueError during update: {e}")
    except Exception as e:
        print(f"   - FAILED: Raised unexpected exception during update: {e}")
    
    # Test 5: Update with title exceeding 200 characters
    try:
        manager.update_task(task['id'], "A" * 201)
        print("   - FAILED: Should have raised ValueError for title too long in update")
    except ValueError as e:
        print(f"   + PASSED: Correctly raised ValueError during update: {e}")
    except Exception as e:
        print(f"   - FAILED: Raised unexpected exception during update: {e}")
    
    # Test 6: Update with description exceeding 1000 characters
    try:
        manager.update_task(task['id'], description="A" * 1001)
        print("   - FAILED: Should have raised ValueError for description too long in update")
    except ValueError as e:
        print(f"   + PASSED: Correctly raised ValueError during update: {e}")
    except Exception as e:
        print(f"   - FAILED: Raised unexpected exception during update: {e}")
    
    # Test 7: Update non-existent task (should return False)
    print("\n2. Testing operations on non-existent tasks:")
    result = manager.update_task(999, "New title")
    if result is False:
        print("   + PASSED: update_task returned False for non-existent task")
    else:
        print(f"   - FAILED: update_task returned {result} instead of False")
    
    # Test 8: Delete non-existent task (should return False)
    result = manager.delete_task(999)
    if result is False:
        print("   + PASSED: delete_task returned False for non-existent task")
    else:
        print(f"   - FAILED: delete_task returned {result} instead of False")
    
    # Test 9: Toggle completion of non-existent task (should return False)
    result = manager.toggle_complete(999)
    if result is False:
        print("   + PASSED: toggle_complete returned False for non-existent task")
    else:
        print(f"   - FAILED: toggle_complete returned {result} instead of False")
    
    # Test 10: Get non-existent task (should return None)
    result = manager.get_task(999)
    if result is None:
        print("   + PASSED: get_task returned None for non-existent task")
    else:
        print(f"   - FAILED: get_task returned {result} instead of None")
    
    print("\n" + "="*50)
    print("Error handling testing completed!")


if __name__ == "__main__":
    test_error_handling()