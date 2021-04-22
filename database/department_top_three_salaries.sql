-- hard
SELECT
    d.name AS Department,
    t1.Name AS Employee,
    t1.Salary AS Salary
FROM
    Employee t1
    JOIN Employee t2
    JOIN Department d
WHERE
    t1.DepartmentId = t2.DepartmentId
    AND t1.Salary <= t2.Salary
    AND d.id = t2.DepartmentId
GROUP BY
    t1.id
HAVING
    COUNT(DISTINCT(t2.Salary)) <= 3
ORDER BY
    d.name,
    salary DESC