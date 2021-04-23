-- medium
SELECT
    *
FROM
    (
        SELECT
            t1.id,
            CASE
                WHEN t2.student IS NULL THEN t1.student
                ELSE t2.student
            END AS student
        FROM
            seat t1
            LEFT JOIN seat t2 ON t2.id - 1 = t1.id
        WHERE
            t1.id % 2 = 1
        UNION
        SELECT
            t1.id,
            CASE
                WHEN t2.student IS NULL THEN t1.student
                ELSE t2.student
            END AS student
        FROM
            seat t1
            LEFT JOIN seat t2 ON t2.id = t1.id - 1
        WHERE
            t1.id % 2 = 0
    ) t
ORDER BY
    id