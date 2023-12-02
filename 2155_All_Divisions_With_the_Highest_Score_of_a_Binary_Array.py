from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_cnt, one_cnt = [], []
        ones, zeros = sum(nums), 0
        for i, num in enumerate(nums):
            zero_cnt.append(zeros)
            one_cnt.append(ones)
            if num == 1:
                ones -= 1
            else:
                zeros += 1
        zero_cnt.append(zeros)
        one_cnt.append(ones)

        max_cnt, ans = 0, []
        for i in range(len(nums) + 1):
            if zero_cnt[i] + one_cnt[i] > max_cnt:
                ans = [i]
                max_cnt = zero_cnt[i] + one_cnt[i]
            elif zero_cnt[i] + one_cnt[i] == max_cnt:
                ans.append(i)
        return ans




