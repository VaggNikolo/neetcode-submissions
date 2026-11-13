-- Write your query below
SELECT name FROM customers c
EXCEPT
SELECT c.name FROM customers c
INNER JOIN orders o
ON c.id=o.customer_id
