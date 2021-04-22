-- easy
SELECT
    t2.name AS employee
FROM
    employee t1
    LEFT JOIN employee t2 ON t2.manager_id = t1.id
WHERE
    t2.salary > t1.salary