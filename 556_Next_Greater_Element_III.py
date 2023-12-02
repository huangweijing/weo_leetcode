class Solution:
    def nextGreaterElement(self, n: int) -> int:
        dig_arr = list(str(n))
        stk = []
        while len(dig_arr) > 0:
            ch = dig_arr.pop()
            if len(stk) == 0 or ch >= stk[-1]:
                stk.append(ch)
            else:
                stk.sort()
                dig = ""
                for i in range(len(stk)):
                    if stk[i] > ch:
                        dig, stk[i] = stk[i], ch
                        break
                stk.sort()
                ans = int("".join(dig_arr) + dig + "".join(stk))
                if ans > (1 << 31) - 1:
                    return -1
                return ans
        return -1

r = Solution().nextGreaterElement(2147483486)
print(r)
