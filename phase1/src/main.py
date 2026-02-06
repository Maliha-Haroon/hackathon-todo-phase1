# [Task]: T-020
# [From]: plan.md §Main Application, specify.md §Menu System

from todo_manager import TodoManager
from ui import TodoUI


def main():
    """
    Main entry point for the Todo Console App.
    Initializes the TodoManager and TodoUI, then runs the application loop.
    """
    print("🌟 Welcome to the Todo Console App! 🌟")
    
    # Initialize the TodoManager and TodoUI
    manager = TodoManager()
    ui = TodoUI(manager)
    
    # Application loop
    while True:
        # Show the main menu
        ui.show_menu()
        
        # Get the user's menu choice
        choice = ui.get_menu_choice()
        
        # Route the choice to the appropriate handler
        if choice == '1':
            ui.handle_add_task()
        elif choice == '2':
            ui.handle_view_tasks()
        elif choice == '3':
            ui.handle_update_task()
        elif choice == '4':
            ui.handle_delete_task()
        elif choice == '5':
            ui.handle_complete_task()
        elif choice == '6':
            print("\n👋 Thank you for using the Todo Console App. Goodbye! 👋")
            break
        
        # Pause before showing the menu again
        input("\n🔹 Press Enter to continue...")
    
    print("✨ Application exited. Have a great day! ✨")


if __name__ == "__main__":
    main()