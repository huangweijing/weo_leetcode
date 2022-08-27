class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_stack = list[int]()
        num_hash = dict[int, int]()

        for i in range(len(nums2) - 1, -1, -1):
            while len(num_stack) > 0 and num_stack[-1] < nums2[i]:
                num_stack.pop()
            if len(num_stack) > 0:
                num_hash[nums2[i]] = num_stack[-1]
            else:
                num_hash[nums2[i]] = -1
            num_stack.append(nums2[i])

        return list(map(lambda x: num_hash[x], nums1))
