class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans_set = set[int]()
        fail_set = set[int]()
        num = 1
        while len(ans_set) < n:
            if num not in fail_set:
                ans_set.add(num)
                fail_set.add(k - num)
            num += 1
        return sum(ans_set)