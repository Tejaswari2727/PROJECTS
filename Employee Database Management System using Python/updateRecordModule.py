from connectionModule import myConnectToDatabase

def myUpdateRecord(eid, ename, salary, location, dept):
    conn = myConnectToDatabase()
    cursor = conn.cursor()

    print(f"🟡 [DEBUG] Trying to update empid={eid} → {ename}, {salary}, {location}, {dept}")

    cursor.execute("""
        UPDATE employees
        SET ename = %s, salary = %s, location = %s, dept = %s
        WHERE empid = %s
    """, (ename, salary, location, dept, eid))

    conn.commit()

    if cursor.rowcount > 0:
        result = "Record updated successfully!"
        print(f"✅ [DEBUG] {result}")
    else:
        result = "No record updated!"
        print(f"❌ [DEBUG] {result}")

    conn.close()
    return result
