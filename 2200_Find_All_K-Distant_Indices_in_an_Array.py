from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_pos = []
        for i, num in enumerate(nums):
            if num == key:
                if len(key_pos) > 0 and key_pos[-1][1] >= max(i - k, 0):
                    key_pos[-1][1] = min(i + k, len(nums) - 1)
                else:
                    key_pos.append([max(i - k, 0), min(i + k, len(nums) - 1)])
        ans = []
        for span in key_pos:
            for i in range(span[0], span[1] + 1):
                ans.append(i)
        return ans





