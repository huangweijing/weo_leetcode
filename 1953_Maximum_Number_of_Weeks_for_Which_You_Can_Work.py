from typing import List

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort(reverse=True)
        sum_all = sum(milestones)
        if milestones[0] > sum_all - milestones[0]:
            return (sum_all - milestones[0]) * 2 + 1
        else:
            return sum_all



