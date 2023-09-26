# Write your MySQL query statement below
# select max(t1.num) as num from (
# select num
# from MyNumbers
# group by num
# having count(1) = 1
# ) t1