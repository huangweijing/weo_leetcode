from typing import List
from functools import cache


class Solution:
    @cache
    def get_cnt(self, int_len: int) -> int:
        if int_len <= 2:
            return 10
        else:
            return self.get_cnt(int_len - 2) * 10

    @cache
    def my_sol(self, query: int, int_len: int) -> str:
        """
        count 0
        """
        if int_len == 1:
            if query <= 10:
                return str(query)
            else:
                return "-1"
        if int_len == 2 and query <= 10:
            if query == 0:
                return "00"
            elif query <= 10:
                return str(query * 11)
            else:
                return "-1"
        cnt = self.get_cnt(int_len - 2)
        dig = query // cnt
        # print(f"cnt={cnt}, query={query}, dig={dig}, query % cnt={query % cnt}, int_len={int_len}")
        if dig > 9:
            return "-1"
        val = self.my_sol(query % cnt, int_len - 2)
        if val == "-1":
            return "-1"
        return str(dig) + val + str(dig)
    
    @cache
    def my_sol2(self, query: int, int_len: int) -> str:
        
        if int_len == 1:
            if query < 9:
                return str(query + 1)
            else:
                return "-1"
        if int_len == 2:
            if query < 9:
                return str((query + 1) * 11)
            else:
                return "-1"
        cnt = self.get_cnt(int_len - 2)
        # print("cnt", cnt)
        dig = query // cnt
        if dig >= 9:
            return "-1"
        # print(f"cnt={cnt}, query={query}, dig={dig}, query % cnt={query % cnt}, int_len={int_len}")
        val = self.my_sol(query % cnt, int_len - 2)
        if val == "-1":
            return "-1"
        return str(dig + 1) + val + str(dig + 1)

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans = []
        for query in queries:
            res = self.my_sol2(query - 1, intLength)
            # print(query, res)
            ans.append(int(res))
        return ans
    
data = [
    [96]
    # [1]
    # [1,2,3,4,5,90]
    # [90]
    , 5
]
r = Solution().kthPalindrome(*data)
print(r)
