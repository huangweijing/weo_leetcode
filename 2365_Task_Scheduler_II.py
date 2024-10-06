from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        task_dict = dict[int, int]()
        day = 1
        ans = 0
        for t in tasks:
            # print(day, t, task_dict)
            if t not in task_dict:
                task_dict[t] = day
            else:
                task_dict[t] = max(task_dict[t] + space + 1, day)
                day = task_dict[t]
            ans = max(ans, task_dict[t])
            day += 1
        return ans
    

data = [
    [5,8,8,5]
    , 2
]
r = Solution().taskSchedulerII(* data)
print(r)
