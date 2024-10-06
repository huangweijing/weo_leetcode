from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = [[i, num] for i, num in enumerate(nums2)]
        nums2.sort(key=lambda x: [x[1], x[0]])
        nums1.sort()
        ans = [0] * len(nums1)
        to_add = []
        while len(nums1) > 0 and len(nums2) > 0:
            num1 = nums1[-1]
            while len(nums2) > 0 and nums2[-1][1] >= num1:
                to_add.append(nums2.pop()[0])
            if len(nums2) > 0 and num1 > nums2[-1][1]:
                ans[nums2[-1][0]] = num1
                nums2.pop()
            nums1.pop()
        for v in nums1:
            ta = to_add.pop()
            ans[ta] = v
        return ans


data = [
    [12, 24, 8, 32]
    , [13, 25, 32, 11]
]
r = Solution().advantageCount(*data)
print(r)

