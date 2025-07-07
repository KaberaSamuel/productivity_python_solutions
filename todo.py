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
    python todo.py add "todo item"  # Add a new todo
    python todo.py ls               # Show remaining todos
    python todo.py del NUMBER       # Delete a todo
    python todo.py done NUMBER      # Complete a todo
    python todo.py help             # Show usage
    python todo.py report           # Statistics
    python todo.py show             # Show completed todos
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

    elif command == "ls":
        list_todos()

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

    elif command == "show":
        show_done_todos()

    else:
        print(f"Error: Unknown command '{command}'")
        show_help()


if __name__ == "__main__":
    main()
