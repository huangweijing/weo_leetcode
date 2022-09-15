from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        points = 0
        tokens.sort()
        # print(tokens)
        left = 0
        right = len(tokens) - 1
        while left <= right:
            # print(power, points)
            while power > 0:
                if left <= right and power >= tokens[left]:
                    power -= tokens[left]
                    points += 1
                    left += 1
                    # print(power, points, left, right, tokens[left])
                else:
                    break
            # print(power, points)
            if left < right and points > 0:
                power += tokens[right]
                points -= 1
                right -= 1
                # print(points)
            else:
                break
            # print()
        # print(left, right)
        return points

data_tokens = [100,200,300,400]
r = Solution().bagOfTokensScore(data_tokens, 200)
print(r)
