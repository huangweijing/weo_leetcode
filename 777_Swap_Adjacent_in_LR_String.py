class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        ptr_sta = ptr_end = 0
        sta_stk, end_stk = [], []
        while ptr_end < len(end):
            if end[ptr_end] != "X":
                end_stk.append([end[ptr_end], ptr_end])
            ptr_end += 1
        while ptr_sta < len(start):
            if start[ptr_sta] != "X":
                sta_stk.append([start[ptr_sta], ptr_sta])
            ptr_sta += 1
        if len(sta_stk) != len(end_stk):
            return False
        while len(sta_stk) > 0:
            sta_pop, end_pop = sta_stk.pop(), end_stk.pop()
            if sta_pop[0] != end_pop[0]:
                return False
            if sta_pop[0] == "R" and sta_pop[1] > end_pop[1]:
                return False
            if sta_pop[0] == "L" and sta_pop[1] < end_pop[1]:
                return False
        return True

data = [
    "RXL"
    , "XRL"
]
r = Solution().canTransform(* data)
print(r)