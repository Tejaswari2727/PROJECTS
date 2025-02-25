import pymysql

def myConnectToDatabase():
    conn = pymysql.connect(host="localhost", user = "teju 1", password="aditya1", db="project1")
    return conn


    
