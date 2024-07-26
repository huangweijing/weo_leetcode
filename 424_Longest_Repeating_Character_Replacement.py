from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ptr_left, ptr_right = 0, 0
        cnt = Counter()
        ans = 0
        while ptr_right < len(s):
            cnt[s[ptr_right]] += 1
            substr_len = ptr_right - ptr_left + 1
            need_change = substr_len - max(cnt.values())
            if need_change <= k:
                # print(s[ptr_left: ptr_right + 1], need_change, substr_len, cnt)
                ans = max(ans, substr_len)
            else:
                while ptr_left < ptr_right and need_change > k:
                    ptr_left += 1
                    cnt[s[ptr_left - 1]] -= 1
                    substr_len = ptr_right - ptr_left + 1
                    need_change = substr_len - max(cnt.values())
                if need_change <= k:
                    # print(s[ptr_left: ptr_right + 1])
                    ans = max(ans, substr_len)
            ptr_right += 1
        return ans


data = [
    "ABAA"
    , 0
]
r = Solution().characterReplacement(* data)
print(r)

