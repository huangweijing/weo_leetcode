from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        if len(bits) == 1:
            return True
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                i += 1
            if i == len(bits) - 1:
                return True
        return False
