import bisect


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left_idx = 0
        left_sum, right_sum = [0, 0, 0], [0, 0, 0]
        ans = 0
        for i, ch in enumerate(s):
            if ch == "a":
                right_sum[0] += 1
            elif ch == "b":
                right_sum[1] += 1
            elif ch == "c":
                right_sum[2] += 1
            
            while left_sum[0] <= right_sum[0] - 1 \
                and left_sum[1] <= right_sum[1] - 1 \
                and left_sum[2] <= right_sum[2] - 1:
                if s[left_idx] == "a":
                    left_sum[0] += 1
                elif s[left_idx] == "b":
                    left_sum[1] += 1
                elif s[left_idx] == "c":
                    left_sum[2] += 1
                left_idx += 1

            # print(left_idx, left_sum, right_sum)
            ans += left_idx

        return ans
    

data = "abcaa"
r = Solution().numberOfSubstrings(data)
print(r)
            