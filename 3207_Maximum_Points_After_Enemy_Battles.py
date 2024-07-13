from typing import List
from collections import deque


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # sum_energies = sum(enemyEnergies)
        # if sum_energies <= currentEnergy:
        #     return len(enemyEnergies)
        enemy_queue = deque(sorted(enemyEnergies))
        ans = 0
        while len(enemy_queue) > 0:
            if currentEnergy >= enemy_queue[0]:
                if ans == 0:
                    currentEnergy -= enemy_queue[0]
                    ans += 1
                else:
                    # print(ans, currentEnergy // enemy_queue[0])
                    ans += currentEnergy // enemy_queue[0]
                    currentEnergy %= enemy_queue[0]
            elif ans >= 1:
                currentEnergy += enemy_queue.pop()
            else:
                break
            # print(ans, currentEnergy, enemy_queue)
        return ans



data = [
    [3,2,2]
    , 2
]
r = Solution().maximumPoints(* data)
print(r)

