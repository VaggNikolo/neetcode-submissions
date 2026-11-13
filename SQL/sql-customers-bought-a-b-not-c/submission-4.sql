-- Write your query below
WITH ord AS (
SELECT customer_id,ARRAY_AGG(product_name) AS prods FROM orders
GROUP BY customer_id
)

SELECT c.customer_id, c.customer_name FROM customers c
INNER JOIN ord o
ON o.customer_id = c.customer_id
where not ('C' = ANY(o.prods))
and ('A'=ANY(o.prods) AND 'B'=ANY(o.prods))
ORDER BY c.customer_name