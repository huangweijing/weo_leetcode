from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def __init__(self):
        self.employees = dict[int, Employee]()

    def my_sol(self, employee: int) -> int:
        ret = self.employees[employee].importance
        for s in self.employees[employee].subordinates:
            ret += self.my_sol(s)
        return ret

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employees = {employee.id: employee for employee in employees}
        return self.my_sol(id)


