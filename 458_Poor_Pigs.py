import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test_cnt = int(minutesToTest / minutesToDie)
        result =  math.ceil(math.log(buckets) / math.log(test_cnt + 1))
        return result

r = Solution().poorPigs(1000, 15, 60)
print(r)

