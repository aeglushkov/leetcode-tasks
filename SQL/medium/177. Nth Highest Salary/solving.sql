CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT E2.Salary 
      FROM (
          SELECT E1.Salary, DENSE_RANK() OVER w AS 'Dense_rank'
          FROM Employee AS E1
          WINDOW w AS (ORDER BY E1.Salary DESC)
      ) AS E2
      WHERE E2.Dense_rank = N
  );
END


# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
#     BEGIN
#         DECLARE M INT;
#         SET M=N-1;
#         RETURN (
#             select Salary
#             from Employee
#             group by Salary
#             order by Salary desc
#             limit 1 offset M
#     );
# END