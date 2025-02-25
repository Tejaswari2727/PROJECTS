from connectionModule import myConnectToDatabase
#import pymysql

def myGetOneRecord(eid): #done
    conn = myConnectToDatabase()

    cursor = conn.cursor()

    cursor.execute("select * from employees where empid = " + str(eid))

    oneRecord = cursor.fetchone()

    if(oneRecord is not None):
        print("The record is:")
        print("%3d %-30s %7d %-20s %-20s" % (oneRecord[0], oneRecord[1], oneRecord[2], oneRecord[3], oneRecord[4]))
    else:
        print("No record found!")

    conn.close()

#for testing
# n = int(input("Enter employee id: "))
# myGetOneRecord(n)
