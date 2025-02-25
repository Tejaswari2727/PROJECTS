from connectionModule import myConnectToDatabase

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
