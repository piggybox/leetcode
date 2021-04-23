-- easy
SELECT
    id,
    sum(
        CASE
            WHEN MONTH = 'Jan' THEN revenue
        END
    ) AS Jan_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Feb' THEN revenue
        END
    ) AS Feb_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Mar' THEN revenue
        END
    ) AS Mar_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Apr' THEN revenue
        END
    ) AS Apr_Revenue,
    sum(
        CASE
            WHEN MONTH = 'May' THEN revenue
        END
    ) AS May_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Jun' THEN revenue
        END
    ) AS Jun_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Jul' THEN revenue
        END
    ) AS Jul_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Aug' THEN revenue
        END
    ) AS Aug_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Sep' THEN revenue
        END
    ) AS Sep_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Oct' THEN revenue
        END
    ) AS Oct_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Nov' THEN revenue
        END
    ) AS Nov_Revenue,
    sum(
        CASE
            WHEN MONTH = 'Dec' THEN revenue
        END
    ) AS Dec_Revenue
FROM
    department
GROUP BY
    id