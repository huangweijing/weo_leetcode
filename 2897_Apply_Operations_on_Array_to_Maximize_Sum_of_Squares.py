from typing import List


class Solution:
    MOD = 10 ** 9 + 7

    def maxSum(self, nums: List[int], k: int) -> int:
        bit_cnt = [0] * 31
        for num in nums:
            for i in range(len(bit_cnt)):
                bit_cnt[i] += (num & 1 << i) >> i
        # print(bit_cnt)
        ans = 0
        for i in range(1, k + 1):
            val = 0
            for j in reversed(range(len(bit_cnt))):
                if i <= bit_cnt[j]:
                    val = (val << 1) + 1
                else:
                    val <<= 1
            ans = (ans + val ** 2) % Solution.MOD
        return ans

data = [
    [2,6,5,8]
    , 2
]
r = Solution().maxSum(* data)
print(r)