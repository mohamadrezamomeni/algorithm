SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
From Employee
INNER JOIN Department ON Department.id = Employee.departmentId
WHERE Employee.salary = (SELECT max(e.salary) From Employee AS e WHERE Employee.departmentId=e.departmentId)
