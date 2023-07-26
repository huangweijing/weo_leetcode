class Solution:
    def isFascinating(self, n: int) -> bool:
        num_str = str(n) + str(n * 2) + str(n * 3)
        num_set = set(num_str)
        return len(num_set) == len(num_str) == 9 and "0" not in num_set


r = Solution().isFascinating(192)
print(r)