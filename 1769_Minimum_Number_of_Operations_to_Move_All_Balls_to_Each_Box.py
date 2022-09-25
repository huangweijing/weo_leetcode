from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_ball_cnt = [0] * len(boxes)
        right_ball_cnt = [0] * len(boxes)
        sum_left_ball_cnt = 0
        sum_right_ball_cnt = 0
        left_result = [0] * len(boxes)
        right_result = [0] * len(boxes)
        for i in range(1, len(boxes)):
            if boxes[i - 1] == "1":
                sum_left_ball_cnt += 1
            left_ball_cnt[i] = sum_left_ball_cnt
            if i > 0:
                left_result[i] = left_result[i - 1] + left_ball_cnt[i]

            if boxes[-(i - 1) - 1] == "1":
                sum_right_ball_cnt += 1
            right_ball_cnt[-i - 1] = sum_right_ball_cnt
            if i > 0:
                right_result[-1 - i] = right_result[-1 - (i - 1)] + right_ball_cnt[-1 - i]

        result = []
        for i in range(0, len(boxes)):
            result.append(left_result[i] + right_result[i])
        return result

data_boxes = "1"
r = Solution().minOperations(data_boxes)
print(r)

