from functools import cache

class Solution:
    @cache
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        if money < 0 or children < 0:
            return -1
        if children == 0 and money > 0:
            return -1
        if children == 1:
            if money == 4:
                return -1
            elif money == 8:
                return 1
            else:
                return 0
        sub_ans = self.distMoney(money - 8, children - 1)
        if sub_ans != -1:
            return sub_ans + 1
        else:
            for i in range(1, 9):
                if i == 0:
                    continue
                sub_ans = self.distMoney(money - i, children - 1)
                if sub_ans != -1:
                    return sub_ans
        return -1

data = [
    20
    , 3
]
r = Solution().distMoney(* data)
print(r)