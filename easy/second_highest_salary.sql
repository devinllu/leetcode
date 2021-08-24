SELECT MAX(e1.Salary) as SecondHighestSalary
FROM Employee e1 INNER JOIN Employee e2 ON e1.Salary < e2.Salary