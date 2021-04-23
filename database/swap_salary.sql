-- easy
-- conditional update
UPDATE
    salary
SET
    sex = CASE
        sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END