class Solution:
    def minPartitions(self, n: str) -> int:
        max_ord = 0
        for s in n:
            if ord(s) > max_ord:
                max_ord = ord(s)
        return int(chr(max_ord))

r = Solution().minPartitions("31231241")
print(r)
