from connectionModule import myConnectToDatabase

def myFilterRecords(value, option):
    if option == 1:   # Department
        return myFilter1(value)
    elif option == 2: # Salary
        return myFilter2(value)
    elif option == 3: # Location
        return myFilter3(value)
    else:
        return []

def myFilter1(dept):
    conn = myConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE dept = %s", (dept,))
    allRecords = cursor.fetchall()
    conn.close()
    return allRecords

def myFilter2(sal):
    conn = myConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE salary >= %s", (sal,))
    allRecords = cursor.fetchall()
    conn.close()
    return allRecords

def myFilter3(loc):
    conn = myConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE location = %s", (loc,))
    allRecords = cursor.fetchall()
    conn.close()
    return allRecords
