SELECT D.Name AS 'Department', E.Name AS 'Employee', E.Salary
FROM 
(SELECT DISTINCT MAX(Salary) AS 'Max_salary', DepartmentId 
 FROM Employee
 GROUP BY DepartmentId) AS MS,
 Employee AS E,
 Department AS D
WHERE E.Salary = MS.Max_salary and E.DepartmentId = MS.DepartmentId and E.DepartmentId = D.Id
