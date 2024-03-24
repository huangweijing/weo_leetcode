from typing import List
from collections import defaultdict


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


class WeightedUnionFind:

    def __init__(self, size):
        self.node = dict[int, int]()
        self.size = defaultdict(lambda: 1)
        self.count = size
        pass

    def find(self, p: int):
        while p in self.node:
            p = self.node[p]
        return p

    def union(self, p: int, q: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1


class Solution:
    def __init__(self):
        self.primes = []

    def calc_prime(self, num: int) -> set[int]:
        res = set[int]()
        # print(self.primes)
        for p in self.primes:
            # print(p, num)
            if p > num:
                break
            if num % p == 0:
                num = num // p
                res.add(p)
        return res


    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        self.primes = rwh_primes(max(nums) + 1)
        if len(nums) == 1:
            return True
        total_set = set[int]()
        finished_set = set[int]()
        wuf = WeightedUnionFind(len(self.primes))
        for num in nums:
            if num == 1:
                return False
            if num in finished_set:
                continue
            finished_set.add(num)
            p_set = self.calc_prime(num)
            for p in p_set:
                total_set.add(p)
            if len(p_set) > 1:
                p = p_set.pop()
                for p2 in p_set:
                    wuf.union(p, p2)
        group_set = set[int]()
        for p in total_set:
            group_set.add(wuf.find(p))
            if len(group_set) > 1:
                return False
        return True

data = [42,40,45,42,50,33,30,45,33,45,30,36,44,1,21,10,40,42,42]
r = Solution().canTraverseAllPairs(data)
print(r)

# wuf = WeightedUnionFind(3)
# wuf.union(3, 4)
# wuf.union(4, 7)
# print(wuf.find(7))

# sol = Solution()
# print(sol.calc_prime(10441))

