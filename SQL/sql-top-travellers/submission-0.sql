-- Write your query below
Select u.name ,
 case
    when sum(r.distance) is Null then 0 
    else sum(r.distance)
    end as travelled_distance
from users u 
left join rides r on u.id = r.user_id
group by u.name
order by travelled_distance desc;