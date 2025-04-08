# Task Tracker Application - Requirements & Code Review Exercise

This folder contains a simple task tracking application that needs to be reviewed. The application has been implemented but doesn't fully meet all requirements and contains some bugs.

## Requirements Documentation

### Overview
The Task Tracker is a console application that allows users to manage and track tasks. It should provide functionality to add, view, update, and delete tasks, as well as mark tasks as complete.

### Functional Requirements

1. **Task Management**
   - FR1.1: Users shall be able to create new tasks with a title, description, and due date.
   - FR1.2: Task IDs shall be automatically generated and unique.
   - FR1.3: Tasks shall have a status (incomplete/complete).
   - FR1.4: Users shall be able to view all tasks.
   - FR1.5: Users shall be able to view details of a specific task by ID.
   - FR1.6: Users shall be able to update task details (title, description, due date).
   - FR1.7: Users shall be able to mark tasks as complete.
   - FR1.8: Users shall be able to delete tasks.

2. **Data Persistence**
   - FR2.1: All tasks shall be saved to a JSON file.
   - FR2.2: Tasks shall be loaded from the JSON file when the application starts.
   - FR2.3: Changes to tasks shall be persisted immediately.

3. **User Interface**
   - FR3.1: The application shall provide a simple console menu for all operations.
   - FR3.2: The application shall display appropriate error messages for invalid operations.
   - FR3.3: The application shall confirm successful operations.

### Non-Functional Requirements

1. **Usability**
   - NFR1.1: The application shall be easy to use with clear menu options.
   - NFR1.2: Input validation shall be implemented to prevent invalid data.

2. **Reliability**
   - NFR2.1: The application shall handle errors gracefully without crashing.
   - NFR2.2: The application shall validate user input to prevent data corruption.

3. **Performance**
   - NFR3.1: The application shall respond to user commands within 1 second.

## Code Review Instructions

The current implementation contains several issues:
1. Not all requirements have been implemented
2. There are bugs in the existing functionality
3. There may be coding style issues and best practice violations

Your tasks:
1. Review the code and identify issues/bugs
2. Determine which requirements are not met
3. Fix the issues and implement the missing requirements

## Running the Application

```bash
python task_tracker.py
```
