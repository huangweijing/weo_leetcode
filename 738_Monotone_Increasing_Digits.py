class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        ans = ""
        nstr = str(n)
        if len(nstr) == 1:
            return n
        eq_arr = []
        for i, ch in enumerate(nstr[1:], start=1):
            if nstr[i - 1] > ch:
                if len(eq_arr) == 0:
                    new_int = int(nstr[i - 1]) - 1
                else:
                    new_int = int(eq_arr[0]) - 1
                if new_int != 0:
                    ans += str(new_int)
                ans += "9" * (len(nstr) - i + len(eq_arr))
                eq_arr = []
                break
            elif nstr[i - 1] == ch:
                eq_arr.append(nstr[i - 1])
            else:
                if len(eq_arr) > 0:
                    ans += eq_arr[0] * len(eq_arr)
                ans += nstr[i - 1]
                if i == len(nstr) - 1:
                    ans += ch
                eq_arr = []
        if len(eq_arr) > 0:
            ans = eq_arr[0] * (len(eq_arr) + 1)
        return int(ans)
                

r = Solution().monotoneIncreasingDigits(0)
print(r)