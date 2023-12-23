from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        bit_cnt = [0] * 31
        for num in nums:
            for i in range(len(bit_cnt)):
                if (num & (1 << i)) >> i == 1:
                    bit_cnt[i] += 1
        for i, cnt in enumerate(bit_cnt):
            bit_cnt[i] = (cnt * len(nums) + (len(nums) - cnt) * cnt) % 2

        result = [0] * 31
        for num in nums:
            for i in range(len(bit_cnt)):
                if bit_cnt[i] == 0:
                    continue
                else:
                    result[i] ^= (num & (1 << i)) >> i
        # print(result)
        ans = 0
        for i in range(len(bit_cnt)):
            ans += result[i] << i
        return ans


data = [1,4]
r = Solution().xorBeauty(data)
print(r)


