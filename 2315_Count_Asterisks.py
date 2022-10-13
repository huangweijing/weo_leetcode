class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0
        pair_started = False
        for ch in s:
            if ch == "|":
                if not pair_started:
                    pair_started = True
                else:
                    pair_started = False
            elif ch == "*":
                if not pair_started:
                    result += 1
        return result
