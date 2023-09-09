from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        grow_sorted_list = list(reversed(sorted(zip(plantTime, growTime)
                                                , key=lambda x: [x[1], x[0]])))
        ans = 0
        remain_grow_time = 0
        for time in grow_sorted_list:
            ans += time[0]
            remain_grow_time = max(remain_grow_time - time[0], time[1])
        ans += remain_grow_time
        return ans

data = [
      [3,4,4,26]
    , [19,17,18,15]
]
r = Solution().earliestFullBloom(* data)
print(r)