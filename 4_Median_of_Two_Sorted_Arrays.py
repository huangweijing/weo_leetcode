class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # q1 = queue
        #
        # for num in nums1:
        nums3 = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
            if i < len(nums1) and j < len(nums2) and nums1[i] >= nums2[j]:
                nums3.append(nums2[j])
                j = j + 1
        while i < len(nums1):
            nums3.append(nums1[i])
            i = i + 1
        while j < len(nums2):
            nums3.append(nums2[j])
            j = j + 1
        # print(nums3)
        if len(nums3) % 2 == 1:
            return nums3[int(len(nums3) / 2)]
        else:
            return (nums3[int(len(nums3) / 2) - 1] + nums3[int(len(nums3) / 2)]) / 2



sol = Solution()
print(sol.findMedianSortedArrays([1, 2], [3, 4]))


