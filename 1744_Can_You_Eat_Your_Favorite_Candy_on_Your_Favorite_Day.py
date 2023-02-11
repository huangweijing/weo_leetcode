from typing import List
import bisect

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        max_sum_arr = []
        max_sum = 0
        for candy in candiesCount:
            max_sum += candy
            max_sum_arr.append(max_sum)
        # print(list(zip(range(len(max_sum_arr)), max_sum_arr)))
        ans = []
        for query in queries:
            favorite_type = query[0]
            favorite_day = query[1]
            favorite_cap = query[2]
            min_candy = favorite_day + 1
            max_candy = favorite_cap * (favorite_day + 1)
            min_type = bisect.bisect_left(max_sum_arr, min_candy)
            max_type = bisect.bisect_left(max_sum_arr, max_candy)
            # if min_type < len(max_sum_arr) and max_sum_arr[min_type] == min_candy:
            #     min_type += 1
            # if max_type < len(max_sum_arr) and max_sum_arr[max_type] == max_candy:
            #     max_type += 1
            # print(min_candy, max_candy, min_type, max_type)
            ans.append(min_type <= favorite_type <= max_type)

        return ans

data = [
    [7,11,5,3,8]
    , [[2,2,6]]
]
r = Solution().canEat(* data)
print(r)

# print(bisect.bisect_left([1, 2, 3, 4], 3))