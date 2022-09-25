from types import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[-1])
        return result

