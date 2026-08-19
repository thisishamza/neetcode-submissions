-- Write your query below
Select u.name , COALESCE(SUM(r.distance), 0) AS travelled_distance
from users u 
left join rides r on u.id = r.user_id
group by u.name
order by travelled_distance desc;