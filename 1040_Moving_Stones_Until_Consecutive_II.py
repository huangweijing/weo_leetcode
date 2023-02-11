from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        ans = [len(stones), 0]
        if stones[0] + 1 != stones[1] and stones[-2] + 1 != stones[-1]:
            ans[1] = max(stones[-1] - stones[1], stones[-2] - stones[0]) + 1 + 1 - len(stones)
        else:
            ans[1] = stones[-1] - stones[0] + 1 - len(stones)

        if stones[0] + len(stones) == stones[-1]:
            ans[0] = 1
        elif (stones[0] + len(stones) - 2 == stones[-2] and stones[-2] + 1 != stones[-1]) \
            or (stones[0] + 1 != stones[1] and stones[1] + len(stones) - 2 == stones[-1]):
            ans[0] = 2
        else:
            idx, right = 0, 0
            cnt = len(stones)
            while idx < len(stones):
                while right < len(stones) and stones[idx] + len(stones) - 1 >= stones[right]:
                    cnt = right - idx + 1
                    right += 1
                # print(stones[idx], stones[idx] + len(stones) - 1, cnt)
                ans[0] = min(ans[0], len(stones) - cnt)
                idx += 1
                cnt -= 1
        return ans

data = [8,7,6,5,10]
data.sort()
print(data)
r = Solution().numMovesStonesII(data)
print(r)