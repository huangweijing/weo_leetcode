# # Write your MySQL query statement below
# select s.name
# from SalesPerson s
# where s.sales_id not in (
# select sales_id
# from Orders o
#   inner join Company c
#   on c.com_id = o.com_id
# where
#   c.name = "RED"
#     )
