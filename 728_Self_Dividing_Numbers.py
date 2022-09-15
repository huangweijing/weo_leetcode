from typing import List

class Solution:
    def is_self_dividing(self, num) -> bool:
        i = num
        while i > 0:
            remainder = i % 10
            if remainder == 0:
                return False
            if num % remainder != 0:
                return False
            i = int(i / 10)
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if self.is_self_dividing(i)]



r = Solution().selfDividingNumbers(1, 100)
print(r)
