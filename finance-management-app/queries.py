def createTables(mydb):
    income_table_sql = """CREATE TABLE income (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    amount INT);"""

    expense_table_sql = """CREATE TABLE expenses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    amount INT);"""
    cursor = mydb.cursor()

    # creating income table
    cursor.execute(income_table_sql)

    # creating expenses table
    cursor.execute(expense_table_sql)

    mydb.commit()
    cursor.close()
    mydb.close()


def insertIntoTables(mydb, content_array):
    cursor = mydb.cursor()
    table_name, record_name, amount = content_array
    query = f"""INSERT INTO {table_name} (name, amount)
    VALUES ('{record_name}', {amount});"""
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()


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
