Select V.customer_id, COUNT(*) as count_no_trans
From Visits v
left join Transactions t
on v.visit_id = t.visit_id
where t.transaction_id is NULL
Group BY v.customer_id;