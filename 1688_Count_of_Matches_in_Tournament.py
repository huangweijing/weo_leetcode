class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        advanced_team = 0
        while n > 1:
            if n & 1 == 1:
                n -= 1
                advanced_team = 1
            else:
                n >>= 1
                matches += n
                n += advanced_team
                advanced_team = 0
        return matches

