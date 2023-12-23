class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        first_zero_idx = -1
        zero_cnt = 0
        one_cnt = 0
        zero_from_start = 0
        for i, ch in enumerate(s):
            if ch == "0" and first_zero_idx == -1:
                first_zero_idx = i
            if ch == "0":
                zero_cnt += 1
                if one_cnt == 0:
                    zero_from_start += 1
            else:
                one_cnt += 1
        if zero_cnt == 0:
            return 0
        return len(s) - zero_cnt - first_zero_idx + max(0, zero_from_start - 1)


data = "001000011"
r = Solution().secondsToRemoveOccurrences(data)
print(r)