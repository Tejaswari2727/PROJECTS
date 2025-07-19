from connectionModule import myConnectToDatabase

def myInsertRecord(ename, salary, location, dept): #done
    # Open database connection
    conn = myConnectToDatabase()
    
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute("SHOW TABLES LIKE 'employees'")
    table_exists = cursor.fetchone()

    if not table_exists:
    # Create the table if it doesn't exist
        cursor.execute("""CREATE TABLE employees
                    (empid INT AUTO_INCREMENT PRIMARY KEY, ename VARCHAR(30), salary INT,
                    location VARCHAR(30), dept VARCHAR(30))""")
        print("employees table created successfully")

    cursor.execute("insert into employees(ename, salary, location, dept) values(%s, %s, %s, %s) ",
                                                   (ename, salary, location, dept))
    #You must always use %s for all fields.
    #here %s is NOT formatter, but is a placeholder
    conn.commit()

    print("Record inserted successfully")

    conn.close()

#for testing
# ename = input("Enter employee's name: ")
# salary = float(input("Enter salary: "))
# location = input("Enter location: ")
# dept = input("Enter department name: ")

# myInsertRecord(ename, salary, location, dept)
