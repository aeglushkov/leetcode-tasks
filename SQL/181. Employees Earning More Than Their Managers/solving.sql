SELECT E1.Name AS Employee FROM Employee AS E1, Employee AS E2
WHERE E1.ManagerId = E2.Id AND E1.Salary > E2.Salary;

# # Using JOIN
# SELECT
#      a.NAME AS Employee
# FROM Employee AS a JOIN Employee AS b
#      ON a.ManagerId = b.Id
#      AND a.Salary > b.Salary
# ;
