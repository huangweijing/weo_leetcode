from typing import List


class Solution:
    def __init__(self):
        self.composition = []
        self.stock = []
        self.cost = []
        self.budget = 0

    def can_produce(self, machine_idx: int, test_cnt: int) -> bool:
        comp = self.composition[machine_idx]
        total_budget = 0
        for i, c in enumerate(comp):
            # print(c * test_cnt - self.stock[i])
            need_budget = max(c * test_cnt - self.stock[i], 0) * self.cost[i]
            total_budget += need_budget
            if total_budget > self.budget:
                return False
        return True

    def get_best_cnt(self, machine_idx: int) -> int:
        left, right = 0, 10 ** 9
        mid = left + right >> 1
        while left <= right:
            sub1 = self.can_produce(machine_idx, mid)
            sub2 = self.can_produce(machine_idx, mid + 1)
            if sub1 and not sub2:
                return mid
            elif sub1 and sub2:
                left = mid + 1
            elif not sub1 and not sub2:
                right = mid - 1
            mid = left + right >> 1
        return mid

    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        self.budget, self.composition, self.stock, self.cost = budget, composition, stock, cost
        ans = 0
        for i, comp in enumerate(composition):
            ans = max(ans, self.get_best_cnt(i))
        return ans


data = [
3
, 2
, 15
, [[1,1,1],[1,1,10]]
, [0,0,100]
, [1,2,3]
]
r = Solution().maxNumberOfAlloys(* data)
print(r)