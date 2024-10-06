from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for num in nums:
            step_cnt = 0
            while len(stk) > 0 and num >= stk[-1][0]:
                item = stk.pop()
                step_cnt = max(item[1], step_cnt)
            if len(stk) > 0:
                ans = max(ans, step_cnt + 1)
            else:
                step_cnt = 0
            stk.append([num, step_cnt + 1])
            # print(stk)
        return ans


data = [5,3,4,4,7,3,6,11,8,5,11]   
r = Solution().totalSteps(data)
print(r)
