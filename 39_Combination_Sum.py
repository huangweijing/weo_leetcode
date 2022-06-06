from typing import List

class Solution:
    def __init__(self):
        self.solution = []
        self.cache = dict[int, List[int]]()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.solve(candidates, target, [], None)
        return self.solution

    def solve(self, candidates: List[int], target: int, result: List[int], last_try: int):
        if target == 0:
            self.solution.append(result.copy())
        elif target < 0:
            return

        for num in candidates:
            if last_try is not None and num < last_try:
                continue

            result.append(num)
            self.solve(candidates, target - num, result, num)
            result.pop()


sol = Solution()
r = sol.combinationSum([2,3,5], target=8)
print(r)