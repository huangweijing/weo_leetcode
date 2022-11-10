import random

class Solution:

    def __init__(self, nums: List[int]):
        self.num_dict = dict[int, list[int]]()
        for i, num in enumerate(nums):
            if num not in self.num_dict:
                self.num_dict[num] = list[int]()
            self.num_dict[num].append(i)

    def pick(self, target: int) -> int:
        lis = self.num_dict[target]
        r = random.randint(0, len(lis) - 1)
        return lis[r]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)