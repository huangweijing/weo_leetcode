# select
#     d1.name as 'department'
#     , e1.name as 'employee'
#     , e1.salary
# from employee e1
# inner join department d1
#     on e1.departmentId = d1.id
# inner join
# (
# select
# t2.department
# , min(t2.salary) as min_salary
# from (
#     select
#     t1.department
#     , t1.salary
#     , rank() over (partition by t1.department order by t1.salary desc) as 'rank'
#     from (
#         select
#             distinct
#             d2.name as 'department'
#             , e2.salary
#         from employee e2
#         inner join department d2
#             on e2.departmentId = d2.id
#     ) t1
# ) t2
# where t2.rank <= 3
# group by t2.department
# ) t3
#   on t3.department = d1.name
#   and e1.salary >= t3.min_salary