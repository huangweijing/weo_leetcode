from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = Counter()
        for i in range(lowLimit, highLimit + 1):
            box = sum([int(n) for n in str(i)])
            cnt[box] += 1
        return cnt.most_common(1)[0][1]


r = Solution().countBalls(1, 123)
print(r)
