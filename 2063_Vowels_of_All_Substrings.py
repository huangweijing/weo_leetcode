class Solution:
    VOWS = set[str](['a', 'e', 'i', 'o', 'u'])

    def countVowels(self, word: str) -> int:
        vow_cnt = 0
        ans = 0
        for i, ch in enumerate(word):
            if ch in Solution.VOWS:
                vow_cnt += i + 1
            ans += vow_cnt
        return ans

r = Solution().countVowels("baca")
print(r)


