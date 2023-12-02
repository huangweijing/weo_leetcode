class Solution:
    MOD = 10 ** 9 + 7
    def numberOfWays(self, corridor: str) -> int:
        idx = 0
        ans = 1
        p_arr = []
        while idx < len(corridor):
            s_cnt, p_cnt = 0, 0
            while idx < len(corridor) and s_cnt < 2:
                if corridor[idx] == "S":
                    s_cnt += 1
                idx += 1
            while idx < len(corridor) and corridor[idx] == "P":
                p_cnt += 1
                idx += 1
            if s_cnt == 2:
                p_arr.append(p_cnt)
            if s_cnt == 1:
                return 0
        if len(p_arr) == 0:
            return 0
        for p_cnt in p_arr[:-1]:
            ans = ans * (p_cnt + 1) % Solution.MOD
        return ans

r = Solution().numberOfWays("SSPPSS")
print(r)



