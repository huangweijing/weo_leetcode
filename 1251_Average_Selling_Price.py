# # Write your MySQL query statement below
# select
# Prices.product_id
# , IFNULL(round(sum(unitssold.units * prices.price) / sum(unitssold.units), 2), 0) as average_price
# from Prices
# left outer join UnitsSold
#   on prices.start_date <= UnitsSold.purchase_date
#      and UnitsSold.purchase_date <= prices.end_date
#      and UnitsSold.product_id = prices.product_id
# group by Prices.product_id
# order by Prices.product_id