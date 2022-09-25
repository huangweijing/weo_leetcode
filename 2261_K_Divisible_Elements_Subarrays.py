from typing import List

base = 211
mod = 10 ** 9 + 7

class Solution:
    def __init__(self):
        self.nums = []
        self.hash = []
        self.power_list = []

    def update_hash(self):
        acc = 0
        power = 1
        for num in self.nums:
            acc = acc * base + num
            self.hash.append(acc % mod)
            self.power_list.append(power)
            power = power * base % mod

    def get_hash(self, left: int, right: int) -> int:
        if left == 0:
            return self.hash[right]
        return (self.hash[right] - self.hash[left - 1] * self.power_list[right - left + 1] % mod + mod) % mod

    def my_count_distinct(self, s: int, n:int, k: int, p: int) -> int:
        pass

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        left = 0
        right = 0
        k_cnt = 1 if nums[0] % p == 0 else 0
        result = 0
        while left <= right < len(nums):
            while k_cnt < k:
                right += 1
                k_cnt += 1 if nums[right] % p == 0 else 0
                if k_cnt == k:
                    result += 1
                    break

            while k_cnt == k and right < len(nums) and nums[right] % p == 0:
                



        # idx = 0
        # k_cnt = 0
        # while idx < len(nums):
        #     if nums[idx] % p == 0:
        #         k_cnt += 1
        #         if k_cnt >= k:
        #             break




data_nums = [1,2,3,4]
r = Solution().countDistinct(data_nums, 4, 1)
print(r)




