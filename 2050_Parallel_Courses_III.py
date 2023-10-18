from typing import List
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        next_course = [list[int]() for _ in range(n)]
        prev_course = [list[int]() for _ in range(n)]
        for i, relation in enumerate(relations):
            next_course[relation[0] - 1].append(relation[1] - 1)
            prev_course[relation[1] - 1].append(relation[0] - 1)
        # print(prev_course, next_course)
        start_courses = set[int]()
        for c, prev in enumerate(prev_course):
            if len(prev) == 0:
                start_courses.add(c)
        # visited = set[int](start_courses)
        prev_course_finished = [0] * n
        time_taken = [0] * n
        for node in start_courses:
            time_taken[node] = time[node]
        stk = []
        ans = 0
        stk.extend(start_courses)
        while len(stk) > 0:
            # print(stk)
            new_stk = []
            while len(stk) > 0:
                node = stk.pop()
                ans = max(time_taken[node], ans)
                for nc in next_course[node]:
                    time_taken[nc] = max(time_taken[nc], time_taken[node] + time[nc])
                    prev_course_finished[nc] += 1
                    if prev_course_finished[nc] == len(prev_course[nc]):
                        new_stk.append(nc)
            stk = new_stk
            # ans += max_time
        return ans


data = [
5
, [[1,5],[2,5],[3,5],[1,3],[3,4],[4,5]]
, [1,2,3,4,5]
]
r = Solution().minimumTime(*data)
print(r)


