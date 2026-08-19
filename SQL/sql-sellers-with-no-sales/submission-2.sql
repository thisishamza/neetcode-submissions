-- Write your query below
SELECT seller_name FROM seller
where seller_id not in (
SELECT o.seller_id 
FROM orders o 
WHERE o.sale_date BETWEEN '2020-01-01' AND '2020-12-31')
ORDER BY seller_name ASC;
