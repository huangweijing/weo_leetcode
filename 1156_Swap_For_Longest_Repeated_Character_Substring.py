from collections import Counter, deque


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt_arr, cnt_rev_arr = deque(), deque()
        cnt = Counter()
        for ch in text:
            cnt[ch] += 1
            cnt_arr.append(cnt.copy())
        cnt = Counter()
        for ch in reversed(text):
            cnt[ch] += 1
            cnt_rev_arr.appendleft(cnt.copy())
        
        seq_cnt, seq_rev_cnt = deque(), deque()
        
        last_ch = ""
        for i, ch in enumerate(text):
            if ch == last_ch:
                seq_cnt.append(seq_cnt[i - 1] + 1)
            else:
                seq_cnt.append(1)
            last_ch = ch
        last_ch = ""
        for i, ch in enumerate(reversed(text)):
            if ch == last_ch:
                seq_rev_cnt.appendleft(seq_rev_cnt[0] + 1)
            else:
                seq_rev_cnt.appendleft(1)
            last_ch = ch
        # print(cnt_arr)
        # print(text)
        # print(seq_cnt)
        # print(seq_rev_cnt)
        ans = 0
        for i, ch in enumerate(text):
            #x.....xx(x)....x
            ans = max(seq_cnt[i], ans)
            other_ch = False
            if i - seq_cnt[i] >= 0:
                if cnt_arr[i - seq_cnt[i]][text[i]] > 0:
                    other_ch = True
            if i + seq_rev_cnt[i] + 1 < len(text):
                if cnt_rev_arr[i + seq_rev_cnt[i] + 1][text[i]] > 0:
                    other_ch = True
            if other_ch:
                ans = max(seq_cnt[i] + 1, ans)

            #..x....xxxxx(.)xxx.....x
            if 0 < i < len(text) - 1:
                if text[i - 1] == text[i + 1] and ch != text[i - 1]:
                    ans = max(seq_cnt[i - 1] + seq_rev_cnt[i + 1], ans)
                    other_ch = False
                    if i - seq_cnt[i - 1] - 1 >= 0:
                        if cnt_arr[i - seq_cnt[i - 1] - 1][text[i - 1]] > 0:
                            other_ch = True
                    if i + seq_rev_cnt[i + 1] + 1 < len(text):
                        if cnt_rev_arr[i + seq_rev_cnt[i + 1] + 1][text[i - 1]] > 0:
                            other_ch = True
                    if other_ch:
                        ans = max(seq_cnt[i - 1] + seq_rev_cnt[i + 1] + 1, ans)
        return ans
    

data = "bbababaaaa"
r = Solution().maxRepOpt1(data)
print(r)