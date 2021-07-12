CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT E2.Salary FROM (SELECT Salary, ROW_NUMBER() OVER w AS 'Row_number' FROM
                             (SELECT Salary FROM Employee
                              GROUP BY Salary) AS E1
                             WINDOW w AS (ORDER BY E1.Salary DESC)) AS E2
      WHERE E2.Row_number = N
  );
END
