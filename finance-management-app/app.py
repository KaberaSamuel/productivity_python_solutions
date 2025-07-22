import mysql.connector
import os
from dotenv import load_dotenv
from queries import createTables
from queries import addIncome
from queries import addExpense
from queries import setBudget
from queries import setSavingsGoal
from queries import viewFinancialSummary

# Load environment variables from .env file
load_dotenv()

# Access an environment variable
dbname = os.getenv("DATABASE")
db_host = os.getenv("HOST")
# db_user = os.getenv("USER")
db_user = os.getenv("DB_USER")
db_password = os.getenv("PASSWORD")


# Global variables
mydb = None
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

# connecting to database
mydb = None
try:
    mydb = mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database=dbname
    )
    # Here we create the tables if they do not exist
    createTables(mydb)
except mysql.connector.Error:
    print("Failed to connect to the database, Please check your connection credentials")
    exit()


def main():
    if mydb:
        print(welcome_message)
        while True:
            print(menu_message)
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                addIncome(mydb)
            elif choice == "2":
                addExpense(mydb)
            elif choice == "3":
                setBudget(mydb)
            elif choice == "4":
                setSavingsGoal(mydb)
            elif choice == "5":
                viewFinancialSummary(mydb)
            elif choice == "6":
                print("Exiting SAVR. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
