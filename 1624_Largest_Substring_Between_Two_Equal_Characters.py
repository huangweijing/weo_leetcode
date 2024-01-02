class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pair = dict[str, int]()
        ans = -1
        for i, ch in enumerate(s):
            if ch not in pair:
                pair[ch] = i
            else:
                ans = max(ans, i - pair[ch] - 1)
        return ans
