class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1 == 1:
            return False
        left_cnt, right_cnt, nd_cnt = 0, 0, 0
        for i, ch in enumerate(s):
            if locked[i] == "0":
                nd_cnt += 1
            elif ch == "(":
                left_cnt += 1
            elif ch == ")":
                right_cnt += 1
            if left_cnt + nd_cnt < right_cnt:
                return False
            elif left_cnt + nd_cnt == right_cnt:
                left_cnt, right_cnt, nd_cnt == 0
        left_cnt, right_cnt, nd_cnt = 0, 0, 0
        for j, ch in enumerate(reversed(s)):
            i = len(s) - j - 1
            if locked[i] == "0":
                nd_cnt += 1
            elif ch == "(":
                left_cnt += 1
            elif ch == ")":
                right_cnt += 1
            if right_cnt + nd_cnt < left_cnt:
                return False
            elif right_cnt + nd_cnt == left_cnt:
                left_cnt, right_cnt, nd_cnt == 0
        return True
