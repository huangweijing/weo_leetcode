from typing import List

class Solution:
    def my_valid_square(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        diag_len1 = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        diag_len2 = (p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2
        if diag_len1 == 0 or diag_len2 == 0:
            return False

        cp1_x = p2[0] + p1[0]
        cp1_y = p2[1] + p1[1]
        cp2_x = p3[0] + p4[0]
        cp2_y = p3[1] + p4[1]
        is_perpendicular = (p2[0] - p1[0]) * (p4[0] - p3[0]) + (p2[1] - p1[1]) * (p4[1] - p3[1]) == 0
        return diag_len1 == diag_len2 and cp1_x == cp2_x and cp1_y == cp2_y and is_perpendicular

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return self.my_valid_square(p1, p2, p3, p4) or \
            self.my_valid_square(p1, p3, p2, p4) or \
            self.my_valid_square(p1, p4, p2, p3)