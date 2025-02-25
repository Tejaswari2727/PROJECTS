from delete import *
from updateRecordModule import *
from filteringRecordsModule import *
from getAllRecordsModule import  *
from getOneRecordModule import *
from insertRecordModule import *

from connectionModule import myConnectToDatabase

def myCheckTableExists():
    # Create a cursor object to execute SQL queries
    conn = myConnectToDatabase()
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute("SHOW TABLES LIKE 'employees'")
    table_exists = cursor.fetchone()    

    if not table_exists:
        print("First, insert at least one employee record")
        return False

    conn.close()

    return True

while True:
    print("\nEMPLOYEES MANAGEMENT SYSTEM - PROJECT\n")
    print("1. Add an Employee record")
    print("2. Get a record by employee id")
    print("3. Get all employees records")
    print("4. Delete an employee record")
    print("5. Update salary of an employee")
    print("6. Filter employees records")
    print("7. Exit\n")

    choice = int(input("Enter your choice:"))


    if( choice > 7):
        print("Invalid choice, please try again...")
        
    elif (choice == 1):
        ename = input("Enter employee's name: ")
        salary = int(input("Enter salary: "))
        location = input("Enter location: ")
        dept = input("Enter department name: ")
        myInsertRecord(ename, salary, location, dept)

    elif (choice == 2):
        status = myCheckTableExists()
        if status != False:
            n = int(input("Enter employee id: "))
            myGetOneRecord(n)

    elif (choice == 3):
        status = myCheckTableExists()
        if status != False:
            myGetAllRecords()

    elif (choice == 4):
        status = myCheckTableExists()
        if status != False:
            n = int(input("Enter employee id: "))
            myDeleteRecord(n)

    elif (choice == 5):
        status = myCheckTableExists()
        if status != False:
            n = int(input("Enter employee id: "))
            sal = int(input("Enter new salary: "))
            myUpdateRecord(n, sal)

    elif (choice == 6):
        status = myCheckTableExists()
        if status != False:   
            ch = input("Choose 1 for Department wise, 2 for Salary wise and 3 for Location wise:")

            if( ch == '1'):
                dept = input("Enter Department name: ")
                myFilterRecords(dept, 1)
            elif( ch == '2'):
                sal = int(input("Enter Salary value: "))
                myFilterRecords(sal, 2)
            elif (ch == '3'):
                loc = input("Enter Location name: ")
                myFilterRecords(loc, 3)
            else:
                print("Invalid filter option choosen")

    elif (choice == 7):
        break
