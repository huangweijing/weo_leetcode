from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = 0
        min_diff = 10e9
        toppingCosts.sort()
        for base in baseCosts:
            diff = abs(target - base)
            if diff < min_diff:
                ans = base
                min_diff = diff
            elif diff == min_diff:
                ans = min(ans, base)
            dp = set[int]()
            dp.add(base)
            for cost in toppingCosts:
                new_dp = dp.copy()
                for val in dp:
                    new_val = val + cost
                    diff = abs(target - new_val)
                    if diff < min_diff:
                        min_diff = diff
                        ans = new_val
                    elif diff == min_diff:
                        ans = min(ans, new_val)
                    new_dp.add(val + cost)

                    new_val = val + cost * 2
                    diff = abs(target - new_val)
                    if diff < min_diff:
                        min_diff = diff
                        ans = new_val
                    elif diff == min_diff:
                        ans = min(ans, new_val)
                    new_dp.add(val + cost * 2)
                dp = new_dp
            # print(dp)
        return ans
    

data = [
    [3,2]
    , [3]
    , 10
]
r = Solution().closestCost(*data)
print(r)
                
                