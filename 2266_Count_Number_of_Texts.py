from functools import cache


class Solution:
    MOD = 10 ** 9 + 7

    @cache
    def my_sol1(self, cnt: int):
        if cnt < 0:
            return 0
        if cnt == 0:
            return 1
        else:
            return (self.my_sol1(cnt - 1) + self.my_sol1(cnt - 2)
                    + self.my_sol1(cnt - 3))  % Solution.MOD

    @cache
    def my_sol2(self, cnt: int):
        if cnt < 0:
            return 0
        if cnt == 0:
            return 1
        else:
            return (self.my_sol2(cnt - 1) + self.my_sol2(cnt - 2) +
                   self.my_sol2(cnt - 3) + self.my_sol2(cnt - 4)) % Solution.MOD

    def countTexts(self, pressedKeys: str) -> int:
        ans, idx, key_cnt, ch = 1, 0, 0, ""
        while idx < len(pressedKeys):
            while idx < len(pressedKeys) and ch == pressedKeys[idx]:
                key_cnt += 1
                idx += 1
            if ch in ("7", "9"):
                sub_sol = self.my_sol2(key_cnt)
            else:
                sub_sol = self.my_sol1(key_cnt)
            ans = (ans * sub_sol) % Solution.MOD
            if idx < len(pressedKeys):
                key_cnt = 0
                ch = pressedKeys[idx]
        return ans

r = Solution().countTexts("33322")
print(r)

