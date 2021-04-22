SELECT
    t1.firstname,
    t1.lastname,
    t2.city,
    t2.state
FROM
    person t1
    LEFT JOIN address t2 ON t2.personid = t1.personid