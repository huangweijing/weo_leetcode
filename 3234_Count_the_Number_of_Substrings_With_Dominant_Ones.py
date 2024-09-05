from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = Counter()
        zo = 0
        for ch in s:
            if ch == "1":
                zo += 1
            else:
                zo -= 1
            cnt[zo] += 1
        prefix_sum_arr = []
        prefix_sum = 0
        for i, key in enumerate(reversed(sorted(cnt.keys()))):
            prefix_sum += cnt[key]
            prefix_sum_arr.append([len(cnt) - 1 - i, prefix_sum])
        prefix_sum_arr.reverse()
        

        

            