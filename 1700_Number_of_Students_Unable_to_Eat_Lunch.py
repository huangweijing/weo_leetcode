from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        cnt = 0
        while len(students) > 0:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                cnt = 0
            else:
                students.append(students.popleft())
                cnt += 1
            if cnt >= len(students):
                break
        return cnt


data = [
    [1,1,0,0]
    , [0,1,0,1]
]
r = Solution().countStudents(* data)
print(r)
