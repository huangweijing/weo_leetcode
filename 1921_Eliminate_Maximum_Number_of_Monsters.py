from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_arr = []
        for i in range(len(dist)):
            time = dist[i] / speed[i]
            time_arr.append(time)
        time_arr.sort()
        ans = 0
        for i in range(len(dist)):
            if time_arr[i] > i:
                ans += 1
            else:
                break
        return ans