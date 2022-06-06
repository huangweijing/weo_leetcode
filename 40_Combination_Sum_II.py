from typing import List

class Solution:
    def __init__(self):
        self.solution = []

    def add_to_solution(self, result: List[int]):
        if result not in self.solution:
            self.solution.append(result)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # print(candidates)
        cand_table = [True] * len(candidates)
        self.solve(candidates, cand_table, [], None, target)
        return self.solution

    def solve(self, candidates: List[int], cand_table: List[bool], result: List[int], last_try: int, target: int):
        print(target)
        if target == 0:
            # print(result)
            self.add_to_solution(result.copy())
        if target < 0:
            return
        for idx in range(len(candidates)):
            if not cand_table[idx]:
                continue
            if candidates[idx] > target:
                continue
            if last_try is not None and candidates[idx] < last_try:
                continue
            result.append(candidates[idx])
            cand_table[idx] = False
            self.solve(candidates, cand_table, result, candidates[idx], target - candidates[idx])
            result.pop()
            cand_table[idx] = True




sol = Solution()
_candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
_target = 27
r = sol.combinationSum2(_candidates, _target)
print(r)
