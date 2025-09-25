from insertRecordModule import myInsertRecord
from getAllRecordsModule import myGetAllRecords
from getOneRecordModule import myGetOneRecord, myGetOneRecordByName
from updateRecordModule import myUpdateRecord
from delete import myDeleteRecord
from filteringRecordsModule import myFilterRecords

def add_employee(ename, salary, location, dept):
    return myInsertRecord(ename, salary, location, dept)

def get_all_employees():
    return myGetAllRecords()

def get_employee(empid):
    return myGetOneRecord(empid)

def get_employee_by_name(ename):
    return myGetOneRecordByName(ename)

def update_employee(empid, ename, salary, location, dept):
    return myUpdateRecord(empid, ename, salary, location, dept)

def delete_employee(empid):
    return myDeleteRecord(empid)

def filter_employees_by_department(dept):
    return myFilterRecords(dept, 1)

def filter_employees_by_salary(salary):
    return myFilterRecords(salary, 2)

def filter_employees_by_location(location):
    return myFilterRecords(location, 3)
