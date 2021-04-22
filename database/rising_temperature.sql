-- easy
SELECT
    t2.id
FROM
    Weather t1
    JOIN Weather t2 ON t2.temperature > t1.temperature
    AND datediff(t2.recorddate, t1.recorddate) = 1