from connectionModule import myConnectToDatabase

def myFilterRecords(value, option):

    if(option == 1):#Dept
        myFilter1(value)
    elif (option == 2): #Sal
        myFilter2(value)
    elif (option == 3): #Loc value
        myFilter3(value)

def myFilter1(dept):
    conn = myConnectToDatabase()
    cursor = conn.cursor()

    cursor.execute("select * from employees where dept = %s" , (str(dept), ))
                                #notice that we must separate with a comma and not with a %
                                #we have to pass the parameters as a tuple

    allRecords = cursor.fetchall()

    print("Number of filtered records: " , cursor.rowcount)

    if(cursor.rowcount > 0):
        print("\nThe employees belonging to department: ", dept, " are: ")
        for row in allRecords:
            print("%3d %-30s %7d %-20s %-20s" % (row[0], row[1], row[2], row[3], row[4]))
    else:
        print("No records found which satisfy the given criteria")

    conn.close()


def myFilter2(sal):
    conn = myConnectToDatabase()
    cursor = conn.cursor()

    cursor.execute("select * from employees where salary >= " + str(sal))

    allRecords = cursor.fetchall()

    print("Number of filtered records: " , cursor.rowcount)

    if(cursor.rowcount > 0):
        print("\nThe employees with salary >=", sal, " are: ")
        for row in allRecords:
            print("%3d %-30s %7d %-20s %-20s" % (row[0], row[1], row[2], row[3], row[4]))
    else:
        print("No records found which satisfy the given criteria")

    conn.close()

def myFilter3(loc):
    try:
        conn = myConnectToDatabase()
        cursor = conn.cursor()

        cursor.execute("select * from employees where location = %s " , (str(loc), ))

        allRecords = cursor.fetchall()

        print("Number of filtered records: " , cursor.rowcount)

        if(cursor.rowcount > 0):
            print("\nThe employees belonging to location:", loc, " are: ")
            for row in allRecords:
                print("%3d %-30s %7d %-20s %-20s" % (row[0], row[1], row[2], row[3], row[4]))
        else:
            print("No records found which satisfy the given criteria")

        conn.close()
    except Exception as e:
        print(e)


#for testing
# sal = float(input("Enter salary value: "))
# myFilterRecords(sal, 2)
