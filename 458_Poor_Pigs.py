import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test_cnt = int(minutesToTest / minutesToDie)
        # result =  math.ceil(math.log(buckets) / math.log(test_cnt + 1))
        result = math.ceil(round(math.log(buckets, test_cnt + 1), 10))
        return result

r = Solution().poorPigs(125, 1, 4)
print(r)

