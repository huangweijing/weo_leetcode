class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        while n >0:
            num = k / n
            k = k % n
            print(num)
            n -= 1

sol = Solution()
sol.getPermutation(3, 3)


