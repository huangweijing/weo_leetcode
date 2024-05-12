# Write your MySQL query statement below
# select
# project_id
# sum(employee.experience_years) / count(1) as average_years
# from project
# inner join employee
#   on employee.employee_id = project.employee_id
# group by project.project_id