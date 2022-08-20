class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict1 = dict[int, int]()
        num_dict2 = dict[int, int]()
        for num in nums1:
            if num not in num_dict1:
                num_dict1[num] = 0
            num_dict1[num] += 1
        for num in nums2:
            if num not in num_dict2:
                num_dict2[num] = 0
            num_dict2[num] += 1
        result = list[int]()
        for key in num_dict1:
            if key in num_dict2:
                result += [key] * min(num_dict1[key], num_dict2[key])
        return result