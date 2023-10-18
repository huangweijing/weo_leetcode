from functools import cache

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
       return self.arr[index]

    def length(self) -> int:
       return len(self.arr)

class Solution:
    def __init__(self):
        self.mountain_arr = []

    @cache
    def get(self, index: int):
        return self.mountain_arr.get(index)

    @cache
    def get_top_idx(self) -> int:
        left, right = 1, self.mountain_arr.length() - 2
        top_idx = left + right >> 1
        while left <= right:
            v1 = self.get(top_idx - 1)
            v2 = self.get(top_idx)
            v3 = self.get(top_idx + 1)
            if v1 < v2 and v3 < v2:
                return top_idx
            elif v1 < v2 < v3:
                left = top_idx + 1
            elif v1 > v2 > v3:
                right = top_idx - 1
            top_idx = left + right >> 1
            print(left, top_idx, right)
        if self.get(top_idx - 1) < self.get(top_idx) < self.get(top_idx + 1):
            return top_idx + 1
        if self.get(top_idx - 1) > self.get(top_idx) > self.get(top_idx + 1):
            return top_idx - 1
        return top_idx

    def find_target_asc(self, target: int):
        left, right = 0, self.get_top_idx()
        mid = left + right >> 1
        while left <= right:
            if self.get(mid) == target:
                return mid
            elif self.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = left + right >> 1
        return -1


    def find_target_desc(self, target: int):
        left, right = self.get_top_idx(), self.mountain_arr.length() - 1
        mid = left + right >> 1
        while left <= right:
            # print(left, right, mid)
            if self.get(mid) == target:
                return mid
            elif self.get(mid) > target:
                left = mid + 1
            else:
                right = mid - 1
            mid = left + right >> 1
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.mountain_arr = mountain_arr
        ans = self.find_target_asc(target)
        if ans == -1:
            ans = self.find_target_desc(target)
        return ans


# mta = MountainArray([1,2,3,4,5,6,8])
mta = MountainArray([1,5,2])
s = Solution()
s.findInMountainArray(0, mta)
r = s.get_top_idx()
# print(r)
print(s.find_target_desc(4))