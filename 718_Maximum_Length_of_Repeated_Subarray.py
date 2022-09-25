from typing import List

class Solution:
    base = 101
    mod = 604610384032273

    def __init__(self):
        self.nums1 = []
        self.nums2 = []
        self.dp = []
        self.hash1 = []
        self.hash2 = []
        self.power_list = []

    def update_hash(self):
        power_list = []
        power = 1
        acc = 0
        for i, num in enumerate(self.nums1):
            if i != 0:
                power = (power * Solution.base) % Solution.mod
            power_list.append(power)
            acc = acc * Solution.base + num
            self.hash1.append(acc % Solution.mod)

        acc = 0
        for i, num in enumerate(self.nums2):
            if i >= len(power_list):
                power = (power * Solution.base) % Solution.mod
                power_list.append(power)
            else:
                power = power_list[i]
            acc = acc * Solution.base + num
            self.hash2.append(acc % Solution.mod)

        self.power_list = power_list

    def calc_hash1(self, left:int, right:int):
        if left == 0:
            return self.hash1[right]
        # 通过mod将计算结果对齐，tm太神奇了
        return (self.hash1[right] - (self.hash1[left - 1] * self.power_list[right - left + 1]) % Solution.mod + Solution.mod) % Solution.mod

    def calc_hash2(self, left: int, right: int):
        if left == 0:
            return self.hash2[right]
        return (self.hash2[right] - (self.hash2[left - 1] * self.power_list[right - left + 1]) % Solution.mod + Solution.mod) % Solution.mod

    def has_subarray(self, size: int) -> bool:
        hash_idx_dict = dict[int, list[int]]()
        for i in range(0, len(self.nums1) - size + 1):
            hash_key = self.calc_hash1(i, i + size - 1)
            # print("nums1", hash_key, self.nums1[i : i+size])
            if hash_key not in hash_idx_dict:
                hash_idx_dict[hash_key] = list[int]()
            hash_idx_dict[hash_key].append(i)
        # print(hash_idx_dict)
        for j in range(0, len(self.nums2) - size + 1):
            hash_key = self.calc_hash2(j, j + size - 1)
            # print("nums2", hash_key, self.nums1[j : j+size])
            if hash_key in hash_idx_dict:
                idx_list = hash_idx_dict[hash_key]
                for idx in idx_list:
                    # print(self.nums1[idx: idx + size], self.nums2[j: j + size])
                    if self.nums1[idx: idx + size] == self.nums2[j: j + size]:
                        return True

        return False

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        self.update_hash()
        left, right = 0, min(len(nums1), len(nums2)) + 1
        mid = right
        old_mid = mid
        while left < right:
            # print(left, right, mid)
            has_sub = self.has_subarray(mid)
            if has_sub:
                left = mid
            else:
                right = mid
            mid = (left + right) >> 1
            if mid == old_mid:
                break
            old_mid = mid

        return mid

# data = [[1,2,3,2,1]
#         , [3,2,1,4,7]]
# data = [[0,0,0,0,0]
#         ,[0,0,0,0,0]]
data = [[1,0,0,0,1,0,0,1,0,0]
        , [0,1,1,1,0,1,1,1,0,0]]

r = Solution().findLength(* data)
print(r)
