#!/usr/bin/env python3
import sys
import os
from datetime import datetime

TODO_FILE = "todo.txt"
DONE_FILE = "done.txt"


def show_help():
    # Display usage instructions
    help_text = """
Usage:
    python todo.py add "todo item"      # Add a new todo
    python todo.py show pending         # Show pending todos
    python todo.py show done            # Show completed todos
    python todo.py del NUMBER           # Delete a todo
    python todo.py done NUMBER          # Complete a todo
    python todo.py help                 # Show usage
    python todo.py report               # Statistics
    """
    print(help_text)


def read_todos():
    # Read all todos from file and return as list
    if not os.path.exists(TODO_FILE):
        return []

    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []


def write_todos(todos):
    # Write todos list to file
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for todo in todos:
            file.write(todo + "\n")


def read_done_todos():
    # Read all completed todos from done file and return as list
    if not os.path.exists(DONE_FILE):
        return []

    try:
        with open(DONE_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []


def add_todo(todo_text):
    # Add a new todo item
    if not todo_text:
        print("Error: Missing todo string. Nothing added!")
        return

    with open(TODO_FILE, "a", encoding="utf-8") as file:
        file.write(todo_text + "\n")

    print(f'Added todo: "{todo_text}"')


def list_todos():
    # Display all pending todos (newest first)
    todos = read_todos()

    if not todos:
        print("There are no pending todos!")
        return

    # Display in reverse order (newest first)
    for i, todo in enumerate(reversed(todos), 1):
        print(f"[{len(todos) - i + 1}] {todo}")


def show_done_todos():
    # Display all completed todos
    done_todos = read_done_todos()

    if not done_todos:
        print("No completed todos found!")
        return

    print("Completed todos:")
    for i, done_todo in enumerate(done_todos, 1):
        print(f"[{i}] {done_todo}")


def delete_todo(todo_number):
    # Delete a specific todo by number
    try:
        todo_num = int(todo_number)
    except ValueError:
        print(f"Error: Invalid todo number '{todo_number}'")
        return

    todos = read_todos()

    if todo_num < 1 or todo_num > len(todos):
        print(f"Error: todo #{todo_num} does not exist. Nothing deleted.")
        return

    # Remove the todo (convert to 0-based index)
    removed_todo = todos.pop(todo_num - 1)
    write_todos(todos)

    print(f"Deleted todo #{todo_num}")


def complete_todo(todo_number):
    # Mark a todo as completed
    try:
        todo_num = int(todo_number)
    except ValueError:
        print(f"Error: Invalid todo number '{todo_number}'")
        return

    todos = read_todos()

    if todo_num < 1 or todo_num > len(todos):
        print(f"Error: todo #{todo_num} does not exist.")
        return

    # Get the todo to complete (convert to 0-based index)
    completed_todo = todos[todo_num - 1]

    # Add to done file with completion date
    today = datetime.today().strftime("%Y-%m-%d")
    done_entry = f"x {today} {completed_todo}"

    with open(DONE_FILE, "a", encoding="utf-8") as file:
        file.write(done_entry + "\n")

    # Remove from todo list
    todos.pop(todo_num - 1)
    write_todos(todos)

    print(f"Marked todo #{todo_num} as done.")


def show_report():
    # Display statistics of pending and completed todos
    todos = read_todos()
    pending_count = len(todos)

    # Count completed todos
    completed_count = len(read_done_todos())

    today = datetime.today().strftime("%Y-%m-%d")
    print(f"{today} Pending : {pending_count} Completed : {completed_count}")


def main():
    # Main function to handle command line arguments
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "help":
        show_help()

    elif command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing todo string. Nothing added!")
        else:
            # Join all arguments after 'add' to handle todos with spaces
            todo_text = " ".join(sys.argv[2:])
            add_todo(todo_text)

    elif command == "show":
        if len(sys.argv) < 3:
            print("Error: Missing argument. Use 'show pending' or 'show done'")
        elif sys.argv[2].lower() == "pending":
            list_todos()
        elif sys.argv[2].lower() == "done":
            show_done_todos()
        else:
            print(
                f"Error: Unknown show command '{sys.argv[2]}'. Use 'pending' or 'done'"
            )

    elif command == "del":
        if len(sys.argv) < 3:
            print("Error: Missing NUMBER for deleting todo.")
        else:
            delete_todo(sys.argv[2])

    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Missing NUMBER for marking todo as done.")
        else:
            complete_todo(sys.argv[2])

    elif command == "report":
        show_report()

    else:
        print(f"Error: Unknown command '{command}'")
        show_help()


if __name__ == "__main__":
    main()
