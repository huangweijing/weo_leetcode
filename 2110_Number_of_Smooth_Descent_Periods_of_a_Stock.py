from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        last_info = { "last_val": 0, "period": 1}
        for p in prices:
            info = { "last_val": 0, "period": 1}
            if p == last_info["last_val"] - 1:
                info["period"] = last_info["period"] + 1
            info["last_val"] = p
            ans += info["period"]
            last_info = info
        return ans
    
r = Solution().getDescentPeriods([12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7])
print(r)
                

            
        