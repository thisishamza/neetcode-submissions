-- Write your query below
Select employee_id,
 case 
 when name not like 'M%' and employee_id % 2 != 0 then salary 
 else 0 
 end as bonus
from employees
order by employee_id asc;