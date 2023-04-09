from typing import List


class Solution:
    def count_success(self, spell: int, potions: list[int], success: int) -> int:
        left, right = 0, len(potions) - 1
        if potions[left] * spell >= success:
            return len(potions)
        if potions[right] * spell < success:
            return 0
        mid = left + right >> 1
        while left <= right:
            val_mid = potions[mid] * spell
            val_mid_m1 = potions[mid - 1] * spell
            # print(val_mid_m1, val_mid)
            if val_mid_m1 < success <= val_mid:
                return len(potions) - mid
            elif val_mid >= success:
                right = mid - 1
            else:
                left = mid + 1
            mid = left + right >> 1
        return len(potions) - mid


    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            res = self.count_success(spell, potions, success)
            ans.append(res)
        return ans


data = [
    [3, 1, 2]
    , [8, 5, 8]
    , 16
]
r = Solution().successfulPairs(* data)
print(r)

