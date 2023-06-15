from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        org_bit = 0
        for i in range(len(derived)):
            # o0 ^ o1 = d1 --> o1 = o0 ^ d1
            org_bit = org_bit ^ derived[i]
        if org_bit == 0:
            return True

        org_bit = 1
        for i in range(len(derived)):
            # o0 ^ o1 = d1 --> o1 = o0 ^ d1
            org_bit = org_bit ^ derived[i]
        if org_bit == 1:
            return True

        return False

