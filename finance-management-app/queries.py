# queries.py


# Creating necessary tables
def createTables(mydb):
    cursor = mydb.cursor()
    # income table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS income (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    amount INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    # expenses table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    amount INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    # budgets table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS budgets (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100),
    amount INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    # savings goals table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS savings_goals (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goal_name VARCHAR(100),
    target_amount INT,
    target_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )

    mydb.commit()
    cursor.close()


def insertIntoTables(mydb, content_array):
    cursor = mydb.cursor()
    table_name, record_name, amount = content_array
    query = f"""INSERT INTO {table_name} (name, amount)
    VALUES ('{record_name}', {amount});"""
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()


# add income function
def addIncome(mydb):
    name = input("Enter income source: ")
    amount = input("Enter amount: ")
    try:
        amount = int(amount)
        # check if amount is a positive number
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        # Insert income into the database
        cursor = mydb.cursor()
        query = """INSERT INTO income (name, amount) VALUES (%s, %s)"""
        cursor.execute(query, (name, amount))
        mydb.commit()
        print("Income recorded successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
    except Exception as e:
        print(f"Error recording income: {e}")


# add expense function
def addExpense(mydb):
    name = input("Enter expense source: ")
    amount = input("Enter amount: ")
    try:
        amount = int(amount)
        # check if amount is a positive number
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        # Insert expense into the database
        cursor = mydb.cursor()
        query = """INSERT INTO expenses (name, amount) VALUES (%s, %s)"""
        cursor.execute(query, (name, amount))
        mydb.commit()
        print("Expense recorded successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
    except Exception as e:
        print(f"Error recording expense: {e}")


# set budget amount function
def setBudget(mydb):
    category = input("Enter budget category (e.g. food,transport): ")
    amount = input("Enter budget amount: ")
    try:
        amount = int(amount)
        # check if amount is a positive number
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        # Insert budget into the database
        cursor = mydb.cursor()
        query = """INSERT INTO budgets (category, amount) VALUES (%s, %s)"""
        cursor.execute(query, (category, amount))
        mydb.commit()
        print("Budget set successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
    except Exception as e:
        print(f"Error setting budget: {e}")


# set savings goal function
def setSavingsGoal(mydb):
    goal_name = input("Enter savings goal name: ")
    target_amount = input("Enter target amount: ")
    target_date = input("Enter target date (YYYY-MM-DD): ")
    try:
        target_amount = int(target_amount)
        # check if target amount is a positive number
        if target_amount <= 0:
            print("Target amount must be a positive number.")
            return
        # Insert savings goal into the database
        cursor = mydb.cursor()
        query = """INSERT INTO savings_goals (goal_name, target_amount, target_date) 
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (goal_name, target_amount, target_date))
        mydb.commit()
        print("Savings goal set successfully.")
    except ValueError:
        print("Invalid amount or date. Please enter valid values.")
    except Exception as e:
        print(f"Error setting savings goal: {e}")


# view financial summary function
def viewFinancialSummary(mydb):
    cursor = mydb.cursor()
    try:
        # Get total income
        cursor.execute("SELECT SUM(amount) FROM income")
        total_income = cursor.fetchone()[0] or 0

        # Get total expenses
        cursor.execute("SELECT SUM(amount) FROM expenses")
        total_expenses = cursor.fetchone()[0] or 0

        # Get total budget
        cursor.execute("SELECT category, amount FROM budgets")
        budgets = cursor.fetchall()

        # Get saving goals
        cursor.execute(
            "SELECT goal_name, target_amount, target_date FROM savings_goals"
        )
        savings = cursor.fetchall()

        # get net balance
        net_balance = total_income - total_expenses

        print("\n------ Financial Summary ------")
        print(f"Total Income: {total_income} RWF")
        print(f"Total Expenses: {total_expenses} RWF")
        print(f"Net Balance: {net_balance} RWF")

        print("\n Budgets:")
        if budgets:
            for category, amount in budgets:
                print(f" Category: {category}: {amount} RWF")
        else:
            print(" No budgets set.")

        print("\n Savings Goals:")
        if savings:
            for goal_name, target_amount, target_date in savings:
                print(
                    f" Goal: {goal_name}, Target Amount: {target_amount} RWF, Target Date: {target_date}"
                )
        else:
            print(" No savings goals set.")
    except Exception as e:
        print(f"Error retrieving financial summary: {e}")
    finally:
        cursor.close()


def getAllItems(mydb, table):
    cursor = None
    try:
        query = f"""SELECT * FROM {table};"""
        cursor = mydb.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print(f"Items from table '{table}':")
            for row in data:
                print(row)
        else:
            print(f"No items found in table '{table}'.")

    except Exception as e:
        print(f"Error retrieving items: {e}")

    finally:
        if cursor:
            cursor.close()
        if mydb:
            mydb.close()
