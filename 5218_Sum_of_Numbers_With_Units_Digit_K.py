class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, 11):
            if num - i * k >= 0 and (num - i * k) % 10 == 0:
                return i
        return -1

sol = Solution()
r = sol.minimumNumbers(1, 1)
print(r)