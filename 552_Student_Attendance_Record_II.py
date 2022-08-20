class Solution:

    MODULO = 10 ** 9 + 7

    def __init__(self):
        self.np = None

    def my_check_record(self, absent_cnt: int, n: int) -> int:
        if self.np[absent_cnt][n] != -1:
            return self.np[absent_cnt][n]
        rec = 0
        # ~P
        if n > 1:
            rec += self.my_check_record(absent_cnt, n - 1)
        # ~PL
        if n > 2:
            rec += self.my_check_record(absent_cnt, n - 2)
        # ~PLL
        if n > 3:
            rec += self.my_check_record(absent_cnt, n - 3)
        if absent_cnt == 1:
            # ~A
            if n > 1:
                rec += self.my_check_record(0, n - 1)
            # ~AL
            if n > 2:
                rec += self.my_check_record(0, n - 2)
            # ~ALL
            if n > 3:
                rec += self.my_check_record(0, n - 3)

        self.np[absent_cnt][n] = rec % Solution.MODULO
        return rec


    def checkRecord(self, n: int) -> int:
        self.np = [[-1] * (n + 4), [-1] * (n + 4)]
        self.np[0][1] = 2
        self.np[1][1] = 1
        self.np[0][2] = 4
        self.np[1][2] = 4
        self.np[0][3] = 7
        self.np[1][3] = 12
        for i in range(1, n):
            self.my_check_record(0, i)
            self.my_check_record(1, i)
        result = self.my_check_record(0, n) + self.my_check_record(1, n)
        return result % Solution.MODULO

r = Solution().checkRecord(99996)
print(r)


