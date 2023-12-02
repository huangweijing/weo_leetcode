class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        if n.bit_count() == 1:
            return (1 << n.bit_length()) - 1
        base = 1 << (n.bit_length() - 1)
        return self.minimumOneBitOperations(base) - \
               self.minimumOneBitOperations(n - base)


data = 9
r = Solution().minimumOneBitOperations(data)
print(r)