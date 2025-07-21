import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access an environment variable
db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")

welcome_message = """--------------------------------------
    SAVR Financial Management Tool
--------------------------------------
Welcome SAVR
A Management Tool for Small-Scale Entrepreneurs!
This tool helps you track income, expenses, budgets, and savings goals."""

menu_message = """Please Select an option:
1. Add Income
2. Add Expense
3. Set Budget
4. Set Savings Goal
5. View Financial Summary
6. Exit
"""


def main():
    print(welcome_message)
    print("Connecting to the database...")
    try:
        mydb = mysql.connector.connect(host=db_host, user=db_user, password=db_password)
        print("Database connected successfully!")
    except mysql.connector.Error:
        print(
            "Failed to connect to the database, Please check your connection credentials"
        )


if __name__ == "__main__":
    main()
