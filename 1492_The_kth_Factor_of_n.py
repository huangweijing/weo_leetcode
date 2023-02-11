class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact_set = set()
        fact_set.add(1)
        fact_set.add(n)
        for i in range(2, n):
            if n % i == 0:
                fact_set.add(i)

        fact_list = list(fact_set)
        fact_list.sort()
        if k > len(fact_list):
            return -1
        else:
            return fact_list[k - 1]

data = [4, 4]
r = Solution().kthFactor(* data)
print(r)