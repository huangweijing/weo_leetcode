from collections import Counter


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        prev_map = { key: val for key, val in zip("croak", " croa") }
        frog_cnt = Counter()
        for ch in croakOfFrogs:
            prev_ch = prev_map[ch] 
            if prev_ch == " ":
                frog_cnt[ch] += 1
            else:
                if frog_cnt[prev_ch] > 0:
                    frog_cnt[prev_ch] -= 1
                    frog_cnt[ch] += 1
                else:
                    return -1
                ans = max(ans, sum([val for key, val in frog_cnt.items()]))
            frog_cnt["k"] = 0
        for ch, cnt in frog_cnt.items():
            if cnt > 0:
                return -1
        return ans

        
data = "croackroak"
r = Solution().minNumberOfFrogs(data)
print(r)