class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(ord('Z'), ord('A') - 1, -1):
            if s.find(chr(i)) != -1 and s.find(chr(i + 32)) != -1:
                return chr(i)
        return ""

sol = Solution()
r = sol.greatestLetter("arRAzFif")
print(r)
