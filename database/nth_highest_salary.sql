-- medium
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN
SET
    n = n - 1;

RETURN (
    # Write your MySQL query statement below.
    SELECT
        DISTINCT salary
    FROM
        employee
    ORDER BY
        salary DESC
    LIMIT
        1 OFFSET n
);

END