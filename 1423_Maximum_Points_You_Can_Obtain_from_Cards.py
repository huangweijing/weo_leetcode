from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        point_sum_left = [0] * len(cardPoints)
        point_sum_right = [0] * len(cardPoints)
        sum_left = 0
        sum_right = 0
        for i in range(len(cardPoints)):
            sum_left += cardPoints[i]
            point_sum_left[i] = sum_left
            sum_right += cardPoints[len(cardPoints) - 1 - i]
            point_sum_right[i] = sum_right

        max_point = 0
        if max_point < point_sum_left[k - 1]:
            max_point = point_sum_left[k - 1]
        if max_point < point_sum_right[k - 1]:
            max_point = point_sum_right[k - 1]
        for i in range(1, k):
            point_sum = point_sum_left[i - 1] + point_sum_right[k - i - 1]
            # print(i, k-i, point_sum, point_sum_left, point_sum_right)
            if max_point < point_sum:
                max_point = point_sum
        return max_point

r = Solution().maxScore([11,49,100,20,86,29,72], 4)
print(r)