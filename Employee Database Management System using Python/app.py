import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from webBridge import (
    add_employee, get_all_employees,
    update_employee, delete_employee,
    get_employee, get_employee_by_name,
    filter_employees_by_department,
    filter_employees_by_salary,
    filter_employees_by_location
)

HOST = "localhost"
PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/employees":
            data = get_all_employees()
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
            print("✅ Sent all employees")

        elif self.path.startswith("/employees/id/"):
            empid = int(self.path.split("/")[-1])
            data = get_employee(empid)
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
            print(f"✅ Sent employee by ID {empid}")

        elif self.path.startswith("/employees/name/"):
            ename = self.path.split("/")[-1]
            data = get_employee_by_name(ename)
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
            print(f"✅ Sent employee by Name {ename}")

        elif self.path.startswith("/employees/department/"):
            dept = self.path.split("/")[-1]
            data = filter_employees_by_department(dept)
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
            print(f"✅ Sent employees in department {dept}")

        elif self.path.startswith("/employees/location/"):
            loc = self.path.split("/")[-1]
            data = filter_employees_by_location(loc)
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
            print(f"✅ Sent employees in location {loc}")

        elif self.path.startswith("/employees/salary/"):
            salary = int(self.path.split("/")[-1])
            data = filter_employees_by_salary(salary)
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
            print(f"✅ Sent employees with salary >= {salary}")

    def do_POST(self):
        if self.path == "/employees":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length).decode()
            params = parse_qs(body)

            ename = params.get("ename", [""])[0]
            salary = int(params.get("salary", [0])[0])
            location = params.get("location", [""])[0]
            dept = params.get("dept", [""])[0]

            add_employee(ename, salary, location, dept)
            self._set_headers()
            self.wfile.write(json.dumps({"status": "Employee added"}).encode())
            print(f"➕ Added employee: {ename}, {salary}, {location}, {dept}")

    def do_PUT(self):
        if self.path.startswith("/employees/"):
            empid = int(self.path.split("/")[-1])
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length).decode()
            params = parse_qs(body)

            ename = params.get("ename", [""])[0]
            salary = int(params.get("salary", [0])[0])
            location = params.get("location", [""])[0]
            dept = params.get("dept", [""])[0]

            update_employee(empid, ename, salary, location, dept)
            self._set_headers()
            self.wfile.write(json.dumps({"status": "Employee updated"}).encode())
            print(f"✏️ Updated employee {empid} → {ename}, {salary}, {location}, {dept}")

    def do_DELETE(self):
        if self.path.startswith("/employees/"):
            empid = int(self.path.split("/")[-1])
            delete_employee(empid)
            self._set_headers()
            self.wfile.write(json.dumps({"status": "Employee deleted"}).encode())
            print(f"🗑️ Deleted employee {empid}")

def run():
    server = HTTPServer((HOST, PORT), MyHandler)
    print(f"🚀 Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
