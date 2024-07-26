class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        ms = "122"
        ptr, last_num = 2, 2
        while len(ms) < n:
            num = 3 - last_num
            ms += int(ms[ptr]) * str(num)
            last_num = num
            ptr += 1
        print(ms)
        ans = 0
        for ch in ms[:n]:
            if ch == "1":
                ans += 1
        return ans
    
r = Solution().magicalString(4)
print(r)
        