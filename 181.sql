SELECT Employee.name AS Employee
FROM Employee
INNER JOIN Employee AS Employee2 On Employee.managerId=Employee2.id
WHERE Employee2.salary < Employee.salary