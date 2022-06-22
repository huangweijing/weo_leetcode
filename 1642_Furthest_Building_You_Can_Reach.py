import heapq
from typing import List

class Solution:
    def find_idx(self, bricks_needed_sum: list[int], bricks: int):
        left_wall = 0
        right_wall = len(bricks_needed_sum)
        idx = (left_wall + right_wall) >> 1
        while left_wall < right_wall:
            # print(idx, left_wall, right_wall, bricks_needed_sum, bricks)
            if bricks_needed_sum[idx] > bricks:
                right_wall = idx
                idx = (left_wall + right_wall) >> 1
            else:
                if (idx == len(bricks_needed_sum) - 1 and bricks_needed_sum[idx] <= bricks) \
                    or bricks_needed_sum[idx] <= bricks < bricks_needed_sum[idx + 1]:
                    return idx
                else:
                    left_wall = idx
                    idx = (left_wall + right_wall) >> 1


    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_height_heap = []
        heapq.heapify(max_height_heap)

        bricks_needed_sum = [0] * len(heights)
        bricks_needed = [0] * len(heights)
        bricks_needed[0] = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                bricks_needed[i] = heights[i] - heights[i - 1]
            bricks_needed_sum[i] = bricks_needed[i] + bricks_needed_sum[i - 1]
        print(bricks_needed)
        print(bricks_needed_sum)

        # find idx where player can go only using bricks
        idx = self.find_idx(bricks_needed_sum, bricks)
        if idx >= len(bricks_needed_sum) - 1:
            return idx
        for i in range(idx + 2):
            heapq.heappush(max_height_heap, -bricks_needed[i])

        while ladders > 0 and idx < len(bricks_needed_sum):
            # use a ladder to replace a jump of the highest cost of bricks
            ladders -= 1
            cur_heighest = - heapq.heappop(max_height_heap)
            # print(f"idx={idx}, cur_heighest={cur_heighest}, bricks={bricks}, max_height_heap={max_height_heap}")
            bricks += cur_heighest
            # see where the player can go
            new_idx = self.find_idx(bricks_needed_sum, bricks)
            # put new cost info into heap
            if new_idx >= len(bricks_needed_sum) - 1:
                return new_idx
            for i in range(idx + 2, new_idx + 2):
                heapq.heappush(max_height_heap, -bricks_needed[i])
            idx = new_idx

        return idx

sol = Solution()
r = sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 0, 8)
print(r)

