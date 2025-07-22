# finance-management-app/queries.py
# Creating necessary tables
def createTables(mydb):
    cursor = mydb.cursor()
    #income table
    cursor.execute ("""CREATE TABLE IF NOT EXISTS income (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    amount INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
     )                 

    #expenses table
    cursor.execute ("""CREATE TABLE IF NOT EXISTS expenses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    amount INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )


    # budgets table
    cursor.execute ("""CREATE TABLE IF NOT EXISTS budgets (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100),
    amount INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")

    # savings goals table
    cursor.execute ("""CREATE TABLE IF NOT EXISTS savings_goals (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goal_name VARCHAR(100),
    target_amount INT,
    target_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")  

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
