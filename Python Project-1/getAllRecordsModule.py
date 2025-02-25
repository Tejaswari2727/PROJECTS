from connectionModule import myConnectToDatabase
#import pymysql

def myGetAllRecords(): #done
    conn = myConnectToDatabase()

    cursor = conn.cursor()

    cursor.execute("select * from employees")

    allRecords = cursor.fetchall()

    print("Number of records: " , cursor.rowcount)

    if(cursor.rowcount > 0):
        print("\nThe records are:")
        for row in allRecords:
            print("%3d %-30s %7d %-20s %-20s" % (row[0], row[1], row[2], row[3], row[4]))
    else:
        print("No records found")

    conn.close()

#for testing
#myGetAllRecords()
