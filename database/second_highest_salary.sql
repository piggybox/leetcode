-- easy
-- table as field to deal with null
SELECT
    (
        SELECT
            DISTINCT salary -- exclude same rank
        FROM
            employee
        ORDER BY
            salary DESC
        LIMIT
            1 OFFSET 1
    ) AS SecondHighestSalary