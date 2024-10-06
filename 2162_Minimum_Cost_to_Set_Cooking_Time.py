import math


def calc_cost(keys: str, startAt: int, moveCost: int, pushCost: int) -> int:
    keys = keys.lstrip("0")
    ret = 0
    prev = str(startAt)
    for key in keys:
        if prev != key:
            ret += moveCost
            # print("moveCost", key, moveCost, "!")
        ret += pushCost
        prev = key
        # print("pushCost", key, pushCost, "!")
    # print(keys, ret)
    return ret

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minute = targetSeconds // 60
        second = targetSeconds % 60
        # print(str(minute), str(second).rjust(2, "0"))
        ans = math.inf
        if minute <= 99 and second <= 99:
            ans = calc_cost(str(minute) + str(second).rjust(2, "0"), 
                            startAt, moveCost, pushCost)
        if second + 60 <= 99 and minute > 0:
            ans = min(ans, calc_cost(str(minute - 1) + str(second + 60).rjust(2, "0"), 
                        startAt, moveCost, pushCost))
        return ans
            

data = [
    1
    , 9403
    , 9402
    , 6008
]
r = Solution().minCostSetTime(*data)
print(r)