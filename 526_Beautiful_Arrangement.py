from functools import cache

class Solution:
    @cache
    def my_sol(self, positions: int, numbers: int) -> int:
        # represent positions and numbers with bits, so we can cache the results
        if positions == numbers == 0:
            return 1
        ans = 0
        for i in range(numbers.bit_length()):
            if numbers & (1 << i) == 1 << i:
                for j in range(positions.bit_length()):
                    if positions & (1 << j) == 1 << j:
                        if (i + 1) % (j + 1) == 0 or (j + 1) % (i + 1) == 0:
                            ans += self.my_sol(positions ^ (1 << j),
                                        numbers ^ (1 << i))
                break
        return ans

    def countArrangement(self, n: int) -> int:
        return self.my_sol((1 << n) - 1, (1 << n) - 1)

r = Solution().countArrangement(5)
print(r)