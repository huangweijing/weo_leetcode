from functools import cache
import heapq

class Solution:
    @cache
    def is_ugly_num(self, n) -> bool:
        if n == 1:
            return True
        if n % 2 == 0:
            return self.is_ugly_num(int(n / 2))
        elif n % 3 == 0:
            return self.is_ugly_num(int(n / 3))
        elif n % 5 == 0:
            return self.is_ugly_num(int(n / 5))

    def nthUglyNumber2(self, n: int) -> int:
        i = 1
        un = 0
        while True:
            if self.is_ugly_num(i):
                print(i, un)
                un += 1
                if un == n:
                    return i
            i += 1

    def nthUglyNumber(self, n: int) -> int:
        ugly_number = [1]
        un_set = set[int]()
        t = 0
        while t < n:
            un = heapq.heappop(ugly_number)
            if un not in un_set:
                un_set.add(un)
                t += 1
                if t == n:
                    return un
                heapq.heappush(ugly_number, un * 2)
                heapq.heappush(ugly_number, un * 3)
                heapq.heappush(ugly_number, un * 5)

r = Solution().nthUglyNumber(10000)
print(r)