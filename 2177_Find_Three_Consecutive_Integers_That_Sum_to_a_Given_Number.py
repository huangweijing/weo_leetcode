class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        val = num // 3
        return [val - 1, val, val + 1]
