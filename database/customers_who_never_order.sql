-- easy
SELECT
    t1.name AS customers
FROM
    customers t1
    LEFT JOIN orders t2 ON t2.customerid = t1.id
WHERE
    t2.id IS NULL