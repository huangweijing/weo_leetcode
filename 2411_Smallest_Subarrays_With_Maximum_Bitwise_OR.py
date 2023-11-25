from typing import List
from collections import Counter


class Solution:
    BIT_CNT = 32
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        cnt = Counter()
        cnt_arr = []
        for num in nums:
            cnt = cnt.copy()
            for i in range(Solution.BIT_CNT):
                if (num & (1 << i)) >> i == 1:
                    cnt[i] += 1
            cnt_arr.append(cnt)

        max_or_arr = [0] * len(nums)
        max_or = 0
        for i in reversed(range(len(nums))):
            max_or |= nums[i]
            bit_cnt = Counter()
            for j in range(Solution.BIT_CNT):
                if (max_or & (1 << j)) >> j == 1:
                    bit_cnt[j] += 1
            max_or_arr[i] = bit_cnt
        # print(max_or_arr)
        idx = 0
        ans = []
        for i, num in enumerate(nums):
            idx = max(idx, i)
            diff = None
            while diff != max_or_arr[i]:
                # print(diff, max_or_arr[i])
                if i == 0:
                    diff = cnt_arr[idx].copy()
                else:
                    diff = cnt_arr[idx] - cnt_arr[i - 1]
                # print(num, diff)
                for key in diff:
                    if diff[key] > 0:
                        diff[key] = 1
                if diff == max_or_arr[i]:
                    break
                idx += 1
            ans.append(idx - i + 1)
        return ans


data = [1, 0]
r = Solution().smallestSubarrays(data)
print(r)
