import functools
from typing import List
import functools

def comp(num1: int, num2: int):
    return int(str(num1) + str(num2)) - int(str(num2) + str(num1))

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=functools.cmp_to_key(comp), reverse=True)
        return str(int("".join(map(str, nums))))


r = Solution().largestNumber([3,32,30,34,5,9])
print(r)