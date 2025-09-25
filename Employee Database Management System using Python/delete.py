from connectionModule import myConnectToDatabase

def myDeleteRecord(eid):
    conn = myConnectToDatabase()
    cursor = conn.cursor()

    # Use parameterized query to prevent issues
    cursor.execute("DELETE FROM employees WHERE empid = %s", (eid,))
    conn.commit()

    rows = cursor.rowcount  # number of rows deleted
    conn.close()

    return rows   # ✅ return rowcount instead of string




'''from connectionModule import myConnectToDatabase

def myDeleteRecord(eid):
    conn = myConnectToDatabase()

    cursor = conn.cursor()

    cursor.execute("delete from employees where empid = " + str(eid))

    conn.commit()

    if(cursor.rowcount > 0):
        print("Record deleted successfully!")
    else:
        print("No Record has been deleted!")

    conn.close()

#for testing
# n = int(input("Enter employee id: "))
# myDeleteRecord(n)
'''