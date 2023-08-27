class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_right = (n * (n + 1)) >> 1
        sum_left = 0
        for i in range(1, n + 1):
            sum_left += i
            if sum_left == sum_right:
                return i
            sum_right -= i
        return -1

r = Solution().pivotInteger(8)
print(r)