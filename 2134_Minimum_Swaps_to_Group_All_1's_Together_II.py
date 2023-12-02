from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        zero_cnt = 0
        prefix_arr = [0]
        for num in nums:
            zero_cnt += 1 if num == 0 else 0
            prefix_arr.append(zero_cnt)
        ans = len(nums)
        for i, num in enumerate(nums):
            if i + zero_cnt <= len(nums):
                ans = min(ans, zero_cnt - (prefix_arr[i + zero_cnt] - prefix_arr[i]))
            else:
                # print(f"tmp: {i}, zero={zero_cnt}", prefix_arr[len(nums)] - prefix_arr[i],
                #       zero_cnt - (len(nums) - i))
                ans = min(ans, zero_cnt - (prefix_arr[len(nums)] - prefix_arr[i] +
                          prefix_arr[zero_cnt - (len(nums) - i)] - prefix_arr[0]))
            # print(i, ans)
        return ans

data = [0,1,0,1,1,0,0]
r = Solution().minSwaps(data)
print(r)
