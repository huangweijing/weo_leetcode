from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one_flg = True
        result = []
        for idx in range(len(digits) - 1, -1, -1):
            if plus_one_flg:
                digit = digits[idx] + 1
            else:
                digit = digits[idx]
            if digit == 10:
                plus_one_flg = 1
                digit = 0
            else:
                plus_one_flg = 0
            result.append(digit)

        if plus_one_flg:
            result.append(1)

        result.reverse()
        return result

sol = Solution()
r = sol.plusOne([9, 9, 9])
print(r)
