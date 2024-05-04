class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ch_set = set[str]()
        for ch in word:
            ch_set.add(ch)
        ans = 0
        for ch in range(ord('a'), ord('z') + 1):
            if chr(ch) in ch_set and chr(ch).upper() in ch_set:
                ans += 1
        return ans