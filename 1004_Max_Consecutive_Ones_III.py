from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, 0
        zero_cnt, seq_len = 0, 0
        ans = 0
        while p1 < len(nums) and p2 < len(nums):
            if nums[p2] == 1:
                seq_len += 1
                p2 += 1
                ans = max(ans, seq_len)
                # print(f"ans={ans}, zero={zero_cnt}, seq={seq_len}, p1={p1}, p2={p2}")
            else:
                if zero_cnt + 1 <= k:
                    zero_cnt += 1
                    seq_len += 1
                    p2 += 1
                    ans = max(ans, seq_len)
                    # print(f"ans={ans}, zero={zero_cnt}, seq={seq_len}, p1={p1}, p2={p2}")
                else:
                    if nums[p1] == 0:
                        zero_cnt -= 1
                    p1 += 1
                    seq_len -= 1
        return ans

data = [
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18]
    , 0
]
r = Solution().longestOnes(* data)
print(r)