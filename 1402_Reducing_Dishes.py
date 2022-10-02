from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        sum_all = sum(satisfaction)
        total_score = 0
        for i in range(1, len(satisfaction) + 1):
            total_score += satisfaction[i - 1] * i

        result = total_score
        for i in range(1, len(satisfaction) + 1):
            # print(total_score, sum_all)
            new_total_score = total_score - sum_all
            sum_all -= satisfaction[i - 1]
            result = max(result, new_total_score)
            total_score = new_total_score
        return result

data_satisfaction = [-1,-4,-5]
r = Solution().maxSatisfaction(data_satisfaction)
print(r)