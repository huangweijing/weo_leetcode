class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return -1 if (n ^ (n | k)) > 0 else (k ^ n).bit_count()


data = [13, 4]
r = Solution().minChanges(* data)
print(r)