class Solution:
    def find_closest(self, nums: list[int], start: int, end: int, target:int):
        # print(nums, start, end, target)
        if start == end:
            return nums[start]

        if start + 1 == end:
            if target - nums[start] < nums[end] - target:
                return nums[start]
            else:
                return nums[end]

        idx = int((start + end + 1) / 2)
        if nums[idx] == target:
            return target
        if nums[idx] < target:
            return self.find_closest(nums, idx, end, target)
        if nums[idx] > target:
            return self.find_closest(nums, start, idx, target)

        # if nums[idx] > target

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)
        min_distance = 100000
        result = target
        for i in range(nums_len - 2):
            for j in range(i + 1, nums_len - 1):
                best_num = target - (nums[i] + nums[j])
                closet_num = self.find_closest(nums, j + 1, len(nums)-1, best_num)
                # print(nums, nums[i], nums[j], best_num, closet_num, target)
                my_num = best_num - closet_num
                if my_num < 0:
                    my_num = -my_num
                if my_num < min_distance:
                    min_distance = my_num
                    result = nums[i] + nums[j] + closet_num
        return result

sol = Solution()
l = [5, 10, 11]
r = sol.find_closest(l, 0, len(l) - 1, 9)
print(r)
print("--------")
r = sol.threeSumClosest([1,2,5,10,11], 12)
print(r)