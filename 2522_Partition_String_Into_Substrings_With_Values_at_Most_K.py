class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans, num, i = 0, 0, 0
        while i < len(s):
            num = 0
            while num <= k and i < len(s):
                dig = int(ord(s[i]) - ord("0"))
                if dig > k:
                    return -1
                elif num * 10 + dig > k:
                    num = 0
                    ans += 1
                    break
                else:
                    num = num * 10 + dig
                    i += 1
        if num > 0:
            ans += 1
        return ans

data = ["1", 1]
r = Solution().minimumPartition(*data)
print(r)
