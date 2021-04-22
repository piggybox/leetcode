-- easy
DELETE t1 -- important to add t1 here for mysql to run
FROM
    person t1
    JOIN person t2
WHERE
    t1.email = t2.email
    AND t2.id < t1.id