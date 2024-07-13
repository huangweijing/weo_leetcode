class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur = int(current[:2]) * 60 + int(current[3:])
        cor = int(correct[:2]) * 60 + int(correct[3:])
        diff = abs(cur - cor)
        ans = 0
        for i in [60, 15, 5, 1]:
            if diff >= i:
                ans += diff // i
                diff %= i
        return ans
