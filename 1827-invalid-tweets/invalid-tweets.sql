# Write your MySQL query statement below
Select Tweet_id
From tweets
where char_length(content) >15;