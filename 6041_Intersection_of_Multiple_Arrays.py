class Solution:
    def intersection(self, nums: list) -> list:
        r_dict = dict()
        for num_arr in nums:
            for num in num_arr:
                if num in r_dict:
                    r_dict[num] = r_dict[num] + 1
                else:
                    r_dict[num] = 1
        keys = list(r_dict.keys())
        keys.sort()
        nums_len = len(nums)
        result = []
        for key in keys:
            v = r_dict[key]
            if nums_len == v:
                result.append(key)
        return result

sol = Solution()
r = sol.intersection([[1,2,3],[4,5,6,3], [3, 8, 9]])
print(r)
