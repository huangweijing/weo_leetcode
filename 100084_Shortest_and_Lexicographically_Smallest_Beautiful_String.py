from collections import Counter


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt = Counter()
        one_cnt = 0
        ans = ""
        for i, ch in enumerate(s):
            if ch == "1":
                one_cnt += 1
                cnt[one_cnt] = i
            # print(cnt)
            want_cnt = one_cnt - k + 1
            if want_cnt not in cnt:
                continue
            else:
                # print(s[: i + 1], want_cnt, cnt)
                if ans == "":
                    ans = s[cnt[want_cnt]: i + 1]
                elif len(ans) > i + 1 - cnt[want_cnt]:
                    ans = s[cnt[want_cnt]: i + 1]
                elif len(ans) == i + 1 - cnt[want_cnt]:
                    seg = s[cnt[want_cnt]: i + 1]
                    if seg < ans:
                        ans = seg
        return ans


data = [
    "100111001"
    , 5
]
r = Solution().shortestBeautifulSubstring(* data)
print(r)

