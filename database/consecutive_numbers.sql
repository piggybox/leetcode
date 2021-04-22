-- medium
SELECT
    DISTINCT t1.num ConsecutiveNums
FROM
    LOGS t1
    JOIN LOGS t2
    JOIN LOGS t3
WHERE
    t1.num = t2.num
    AND t2.num = t3.num
    AND t2.id - t1.id = 1
    AND t3.id - t2.id = 1