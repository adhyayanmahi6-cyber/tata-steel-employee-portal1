DROP TABLE IF EXISTS employees;
CREATE TABLE employees(id INTEGER PRIMARY KEY AUTOINCREMENT,employee_name TEXT,employee_id TEXT UNIQUE,department_name TEXT,password TEXT);
INSERT INTO employees(employee_name,employee_id,department_name,password) VALUES
('Rahul Kumar','TS1001','Production','rahul123'),
('Amit Singh','TS1002','Mechanical','amit123'),
('Priya Sharma','TS1003','HR','priya123');
