# Write your MySQL query statement below
Select DISTINCT Author_id as id
from views
where author_id = viewer_id 
ORDER BY author_id;