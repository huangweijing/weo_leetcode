import bisect
import math

class Solution:

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)
        min_distance = math.inf
        result = target
        for i in range(nums_len - 2):
            for j in range(i + 1, nums_len - 1):
                if nums[i] + nums[j] + nums[j + 1] - target > min_distance:
                    break
                best_num = target - (nums[i] + nums[j])
                idx = bisect.bisect_left(nums, best_num, lo=j + 1)
                distance1, distance2 = math.inf, math.inf
                if idx < len(nums):
                    distance1 = abs(best_num - nums[idx])
                if idx > j + 1:
                    distance2 = abs(best_num - nums[idx - 1])
                if distance1 < distance2:
                    closet_num = nums[idx]
                else:
                    closet_num = nums[idx - 1]

                my_num = abs(best_num - closet_num)
                if my_num == 0:
                    return target
                if my_num < min_distance:
                    min_distance = my_num
                    result = nums[i] + nums[j] + closet_num
        return result

data_nums = [-1,2,1,-4]
# data = [-987, -981, -968, -959, -950, -943, -942, -941, -935, -931, -897, -882, -854, -852, -848, -844, -840, -826, -825, -816, -793, -792, -781, -763, -742, -740, -734, -728, -726, -721, -714, -711, -709, -695, -692, -689, -667, -665, -664, -658, -647, -636, -632, -631, -627, -617, -609, -603, -602, -600, -592, -581, -565, -541, -531, -524, -522, -519, -518, -511, -509, -503, -497, -458, -453, -441, -431, -405, -397, -390, -342, -314, -311, -307, -304, -294, -290, -289, -282, -269, -243, -241, -235, -225, -219, -217, -208, -184, -182, -177, -164, -162, -151, -149, -148, -143, -129, -128, -116, -112, -101, -91, -87, -76, -75, -74, -62, -36, -35, -19, -13, -10, -8, -7, -5, -4, -2, 7, 13, 70, 113, 123, 127, 128, 134, 149, 151, 154, 167, 181, 196, 211, 221, 222, 233, 237, 252, 256, 273, 275, 307, 308, 318, 332, 346, 360, 375, 381, 384, 385, 387, 394, 404, 420, 436, 453, 466, 472, 478, 483, 484, 501, 502, 508, 522, 524, 538, 542, 543, 544, 569, 572, 590, 597, 599, 602, 610, 611, 616, 617, 620, 623, 630, 658, 663, 672, 673, 683, 708, 715, 761, 766, 779, 789, 792, 795, 802, 827, 839, 855, 857, 903, 906, 919, 925, 933, 939, 953, 960, 984, 990]

data_target = 1
# print(len(data_nums))
# # [1,2,5,10,11], 12
sol = Solution()
# print("--------")
r = sol.threeSumClosest(data_nums, data_target)
print(r)