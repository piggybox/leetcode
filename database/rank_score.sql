-- medium
SELECT
    a.score,
    b.count AS `rank`
FROM
    scores a
    LEFT JOIN (
        SELECT
            t1.score,
            count(DISTINCT t2.score) AS count
        FROM
            scores t1
            LEFT JOIN scores t2 ON t2.score >= t1.score
        GROUP BY
            t1.score
    ) b ON a.score = b.score
ORDER BY
    b.count