from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        change_tbl = [0] * 1000001
        from_tbl = [0] * 1000001
        for op in operations:
            if from_tbl[op[0]] == 0:
                change_tbl[op[0]] = op[1]
                from_tbl[op[1]] = op[0]
            else:
                from_tbl[op[1]] = from_tbl[op[0]]
                change_tbl[from_tbl[op[0]]] = op[1]
                from_tbl[op[0]] = 0

        for i in range(len(nums)):
            if change_tbl[nums[i]] != 0:
                nums[i] = change_tbl[nums[i]]
        return nums

sol = Solution()
_nums = [1]
_op = [[1,2],[2,3],[3,1000000],[1000000,1]]
r = sol.arrayChange(_nums, _op)
print(r)