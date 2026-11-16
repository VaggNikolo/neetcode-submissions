-- Write your query below
WITH sells AS (
    SELECT a.seller_id
    FROM seller a
    INNER JOIN orders b
    ON a.seller_id = b.seller_id
    WHERE date_part('year',sale_date) = 2020
)

SELECT c.seller_name
FROM seller c
WHERE c.seller_id NOT IN (SELECT d.seller_id FROM sells d)
ORDER BY c.seller_name asc;
