from connectionModule import myConnectToDatabase

def myGetOneRecord(eid):
    conn = myConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE empid = %s", (eid,))
    oneRecord = cursor.fetchone()
    conn.close()
    return oneRecord  # None if not found

def myGetOneRecordByName(ename):
    conn = myConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE ename = %s", (ename,))
    oneRecord = cursor.fetchone()
    conn.close()
    return oneRecord
