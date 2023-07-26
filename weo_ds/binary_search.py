from typing import List

class BinarySearchable:
    def get(self, idx: int):
        raise Error("Not Implemented")

    def len(self):
        raise Error("Not Implemented")


class BinaryArray(BinarySearchable):
    def __init__(self, arr: list):
        self.arr = arr

    def get(self, idx: int):
        return self.arr[idx]

    def len(self):
        return len(self.arr)


class BinarySearch:
    def __init__(self, arr: BinarySearchable):
        self.arr = arr

    def search(self, func1, func2) -> int:
        arr = self.arr
        left, right = 0, arr.len() - 1
        mid = right >> 1
        while left <= right:
            if mid == arr.len() - 1:
                if func1(arr.get(mid - 1), arr.get(mid)):
                    return mid
                else:
                    right = mid - 1
            elif mid == 0:
                if not func2(arr.get(mid), arr.get(mid + 1)):
                    return -1
                else:
                    left = mid + 1
            else:
                func1_res = func1(arr.get(mid - 1), arr.get(mid))
                func2_res = func2(arr.get(mid), arr.get(mid + 1))
                if func1_res and not func2_res:
                    return mid
                elif func1_res and func2_res:
                    left = mid + 1
                else:
                    right = mid - 1
            mid = left + right >> 1
            print(left, right, mid)
        return mid



class Solution:
    def searchGreaterEqualThan(self, arr: list[int], val: int) -> int:
        bs = BinarySearch(BinaryArray(arr))
        idx = bs.search(lambda x1, x2: val > x1
                  , lambda x1, x2: val >= x2)
        return idx

    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def func_comp1(v1: int, v2: int):
            return v1 < v2
        def func_comp2(v1: int, v2: int):
            return v1 < v2
        bs = BinarySearch(BinaryArray(arr))
        return bs.search(func_comp1, func_comp2)
        # return mid

data = [0,1,4,5,7,10]
r = Solution().searchGreaterEqualThan(data, 0)
print(r)
# data = [0,1,2,3,0]
# r = Solution().peakIndexInMountainArray(data)
# print(r)