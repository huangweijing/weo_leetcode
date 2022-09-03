import bisect
from typing import List
from sortedcontainers import SortedList


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        num_sum = 0
        sum_arr = list[int]()
        for num in nums:
            num_sum += num
            sum_arr.append(num_sum)

        result = []
        for query in queries:
            idx = bisect.bisect_left(sum_arr, query)
            if idx < len(sum_arr) and sum_arr[idx] == query:
                result.append(idx + 1)
            else:
                result.append(idx)
        return result

data_num = [2,3,4,5,8,9,1]
data_q = [6]
r = Solution().answerQueries(data_num, data_q)
print(r)



