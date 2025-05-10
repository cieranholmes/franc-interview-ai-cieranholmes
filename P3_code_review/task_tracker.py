#!/usr/bin/env python3
"""
Task Tracker Application

A simple console application for tracking tasks.
"""
import json
import os
from datetime import datetime
import time
import re

# Global variables
TASKS_FILE = "tasks.json"
tasks = {}
def load_tasks():
    """Load tasks from the JSON file."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            # Bug: Silent failure on corrupted JSON, doesn't initialize 'tasks'
            print("Warning: Tasks file is corrupted.")
            tasks = {}
            # Missing: Should initialize tasks = {} here
    else:
        # Create an empty JSON file if it doesn't exist
        save_tasks()

def save_tasks():
    """Save tasks to the JSON file."""
    # Bug: No error handling for file operations
    # Fix: IOError handling
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f)
    except IOError as e:
        print(f"Error: Unable to save tasks. {str(e)}")

def generate_task_id():
    """Generate a new unique task ID."""
    # Bug: This doesn't guarantee uniqueness if tasks are deleted
    # Fix: Uses a set to find the first available unique id - new approach eliminates need for checking base case as well

    used_ids = set(int(task_id) for task_id in tasks.keys())
    new_id = 1

    while new_id in used_ids:
        new_id += 1

    return new_id 

def validate_date(date):
    """Helper method that checjs if a date is in the correct format and in the future"""

    if not date:
        return

    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        print("Invalid date format. Please try again...")
        return

    year, month, day = map(int, date.split('-'))
    if datetime(year, month, day) <= datetime.today():
        print("Invalid future date. Please try again...")
        return

    return date


def add_task():
    """Add a new task."""
    print("\n=== Add New Task ===")
    
    while True:
        title = input("Enter task title: ")
        if not title:
            print("Empty title is not allowed. Please try again...")
        else:
            break
    # Bug: Missing validation for empty title
    # Fix: User will keep being prompted until valid title is inputted
    
    description = input("Enter task description: ")
    
    # Bug: No validation or error handling for date format
    # Fix: Use RegEx and datetime to check for valid date
    while True:
        due_date = validate_date(input("Enter due date (YYYY-MM-DD): "))
        if due_date:
            break
    
    # Missing: No validation that the date is in the future
    # Fix: validate_date() method checks for future date
    
    task_id = str(generate_task_id())
    tasks[task_id] = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "incomplete",
        "created_date": str(datetime.today())[0:10],
        # Bug: Missing created_date field required by specs
        # Fix: Use datetime.today() method and splicing to get the current date
    }
    
    save_tasks()
    print(f"Task {task_id} added successfully!")

def view_all_tasks():
    """View all tasks."""
    print(f"\n{'============================ All Tasks ============================':^64}")
    
    if not tasks:
        print("No tasks found.")
        return
    
    # Bug: This doesn't format output nicely with proper spacing
    # Fix: Uses alignment and width to have minimum column lengths for each task
    print(f"{'ID':<4} | {'Title':<20} | {'Due Date':<10} | {'Status':<10} | {'Created Date':<10}")
    print("-" * 66)
    for task_id, task in tasks.items():
        #print(f"{task_id} | {task['title']} | {task['due_date']} | {task['status']} | {task['created_date']}")
        print(f"{task_id:<4} | {task['title']:<20} | {task['due_date']:<10} | {task['status']:<10} | {task['created_date']:<10}")

def view_task():
    """View details of a specific task."""
    print("\n=== View Task ===")
    
    task_id = input("Enter task ID: ")
    
    # Bug: Missing validation for non-existent task IDs
    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return
    
    task = tasks[task_id]
    print(f"ID: {task_id}")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Status: {task['status']}")
    print(f"Created Date: {task['created_date']}")

def update_task():
    """Update an existing task."""
    print("\n=== Update Task ===")
    
    task_id = input("Enter task ID: ")
    
    # Bug: Missing validation for non-existent task IDs
    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return
    
    task = tasks[task_id]
    
    print("Leave field empty to keep current value.")
    print(f"Current Title: {task['title']}")
    new_title = input("New Title: ")
    
    print(f"Current Description: {task['description']}")
    new_description = input("New Description: ")
    
    print(f"Current Due Date: {task['due_date']}")
    new_due_date_input = input("New due date (YYYY-MM-DD): ")
    while True:
        new_due_date = validate_date(new_due_date_input)
        if new_due_date or not new_due_date_input: # checks for valid input or empty input
            break
        new_due_date_input = input("New due date (YYYY-MM-DD): ")

    
    # Bug: No validation on due date format
    # Fix: Use helper method validate_date to validate date format and future date
    
    # Update task with new values, keeping old values if input is empty
    if new_title:
        task['title'] = new_title
    if new_description:
        task['description'] = new_description
    if new_due_date:
        # Bug: No validation of date format
        # Fix: new_due_date is already validated at assignment
        task['due_date'] = new_due_date
    
    save_tasks()
    print(f"Task {task_id} updated successfully!")

# Bug: Missing implementation of mark_task_complete function (FR1.7)
# Fix: Implementation that checks if task is already marked as complete or if task id is non-existent
def mark_task_complete():
    """Mark a task as complete"""
    print("\n=== Mark Task as Complete===")

    task_id = input("Enter task ID: ") # follows same format as other methods for constintency

    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return

    task = tasks[task_id]
    if task['status'] == "complete":
        print(f'Task {task_id} is already marked as complete.')
    else:
        task['status'] = "complete"
        print(f"Task {task_id} was successfully marked as complete.")
        save_tasks()


def delete_task():
    """Delete a task."""
    print("\n=== Delete Task ===")
    
    task_id = input("Enter task ID: ")
    
    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return
    
    # Bug: Missing confirmation before deletion
    # Fix: User is continuously pronmpted until Y (yes) or n (no) is inputted
    while True:
        choice = input("Are you sure you want to delete this task? (Y/n): ").lower()

        match choice:
            case "y":
                del tasks[task_id]
                save_tasks()
                print(f"Task {task_id} deleted successfully!")
                break
            case "n":
                print("Cancelled operation: Task was not deleted.")
                break
            case _:
                print("Incorrect choice. Please choose Y or n.")

    
def display_menu():
    """Display the main menu."""
    print("\n=== Task Tracker ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Task")
    print("4. Update Task")
    # Bug: Missing option for marking task as complete
    # Fix: Add mark task complete option to menu and push proceeding options up one spot
    print("5. Mark Task as Complete")
    print("6. Delete Task")
    print("7. Exit")

def main():
    """Main application function."""
    load_tasks()
    
    while True:
        display_menu()
        
        # Bug: No validation on choice input
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            view_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            mark_task_complete()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 