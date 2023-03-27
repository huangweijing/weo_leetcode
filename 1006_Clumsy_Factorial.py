class Solution:
    def clumsy(self, n: int, first_minus: bool = False) -> int:
        ans = 0
        if n == 0:
            ans = 0
        elif n == 1:
            ans = (-1 if first_minus else 1) * 1
        elif n == 2:
            ans = (-1 if first_minus else 1) * 2 * 1
        elif n == 3:
            ans = (-1 if first_minus else 1) * 3 * 2 // 1
        elif n == 4:
            ans = (-1 if first_minus else 1) * 4 * 3 // 2 + 1
        else:
            # print(f"{-1 if first_minus else 1} * {n} * {n - 1} // {n - 2} + {n - 3}")
            # print(f"ans={(-1 if first_minus else 1) * n * (n - 1) // (n - 2) + (n - 3)}")
            ans = (-1 if first_minus else 1) * (n * (n - 1) // (n - 2)) + (n - 3) \
                  + self.clumsy(n - 4, True)
        return ans

r = Solution().clumsy(10, False)
print(r)
# print(-1 * (6 * 5 // 4))