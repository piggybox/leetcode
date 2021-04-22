-- medium
-- advanced version
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
    COUNT(DISTINCT(t2.Salary)) <= 1
ORDER BY
    d.name,
    salary DESC 
    
    
-- regular version
SELECT
    t2.name AS department,
    t1.name AS employee,
    t1.salary
FROM
    employee t1
    JOIN department t2 ON t2.id = t1.departmentid
    JOIN (
        SELECT
            max(salary) AS salary,
            departmentid
        FROM
            employee
        GROUP BY
            departmentid
    ) t3 ON t3.salary = t1.salary
    AND t3.departmentid = t1.departmentid