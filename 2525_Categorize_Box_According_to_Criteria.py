class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky, is_heavy, is_both = False, False, False
        ans = "Neither"
        for dimension in [length, width, height]:
            if dimension >= 10 ** 4:
                is_bulky = True
        if length * width * height >= 10 ** 9:
            is_bulky = True
        if mass >= 100:
            is_heavy = True
        if is_heavy and is_bulky:
            ans = "Both"
        elif is_heavy and not is_bulky:
            ans = "Heavy"
        elif not is_heavy and is_bulky:
            ans = "Bulky"
        return ans


