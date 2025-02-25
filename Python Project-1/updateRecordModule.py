from connectionModule import myConnectToDatabase
#import pymysql

def myUpdateRecord(eid, newSalary): #done
    conn = myConnectToDatabase()

    cursor = conn.cursor()

    cursor.execute("update employees set salary = %s where empid = %s", (newSalary, eid))
                                    #make sure that the order is given correctly
    conn.commit()

    if(cursor.rowcount > 0):
        print("Record updated successfully!")
    else:
        print("No Record has been updated!")

    conn.close()
    
    

