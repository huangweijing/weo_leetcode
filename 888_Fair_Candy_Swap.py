from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum, bob_sum = sum(aliceSizes), sum(bobSizes)
        diff = (alice_sum - bob_sum) // 2
        bob_set = set(bobSizes)
        for alice_item in aliceSizes:
            if alice_item - diff in bob_set:
                return [alice_item, alice_item - diff]

data = [[1, 1], [2, 2]]
r = Solution().fairCandySwap(* data)
print(r)
