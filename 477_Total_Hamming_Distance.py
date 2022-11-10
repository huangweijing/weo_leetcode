from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bit_cnt = [0] * 32
        for num in nums:
            for i in range(len(bit_cnt)):
                bit_cnt[i] += (num >> i & 1)
        ans = 0
        for cnt in bit_cnt:
            ans += cnt * (len(nums) - cnt)
        return ans

data = [4,14,4]
r = Solution().totalHammingDistance(data)
print(r)


