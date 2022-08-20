# select
#     d2.name as 'department'
#     , e2.name as 'employee'
#     , e2.salary
# from employee e2
# inner join department d2
#     on e2.departmentId = d2.id
# where
# (d2.name, e2.salary)
# in (
# select d1.name, max(e1.salary)
# from employee e1
# inner join department d1
#     on e1.departmentId = d1.id
# group by d1.name
# )