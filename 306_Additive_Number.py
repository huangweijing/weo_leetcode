class Solution:
    def __init__(self):
        self.result = []

    def my_additive(self, n1: int, n2: int, num:str) -> bool:
        if len(num) == 0:
            # self.result = []
            return True
        n = n1 + n2
        nstr = str(n)
        if len(num) >= len(nstr) and num[:len(nstr)] == nstr:
            sub_result = self.my_additive(n2, int(nstr), num[len(nstr):])
            # if sub_result:
            #     print(n1, n2, num)
            return sub_result
        else:
            return False

    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                n1 = num[: i]
                n2 = num[i: j]
                n3 = num[j: ]

                if len(n3) == 0:
                    continue
                if str(int(n1)) != n1 or str(int(n2)) != n2 or str(int(n3)) != n3:
                    continue
                sub_result = self.my_additive(int(n1), int(n2), n3)
                if sub_result:
                    # print(n1, n2, n3)
                    return True
        return False

r = Solution().isAdditiveNumber("199100199")
print(r)


