-- easy
DELETE t1
FROM
    person t1
    JOIN person t2
WHERE
    t1.email = t2.email
    AND t2.id < t1.id