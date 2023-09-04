import math

class Solution:
    def minimumOperations(self, num: str) -> int:
        cost1, cost2 = math.inf, math.inf # cost1 for 5, cost2 for 0
        for i in range(1, len(num)):
            if num[-i] == "5":
                cost1 = i - 1
                break
        for i in range(1, len(num)):
            if num[-i] == "0":
                cost2 = i - 1
                break
        if cost1 == cost2 == math.inf: # no answer
            return len(num) # delete all numbers
        # print(cost1, cost2)
        ans1, ans2 = math.inf, math.inf
        if cost1 != math.inf:
            for i in range(cost1 + 2, len(num) + 1):
                if num[-i] == "2" or num[-i] == "7":
                    ans1 = i - 2
                    break
            if ans1 == math.inf:
                ans1 = len(num)
        if cost2 != math.inf:
            for i in range(cost2 + 2, len(num) + 1):
                if num[-i] == "5" or num[-i] == "0":
                    ans2 = i - 2
                    break
            if ans2 == math.inf:
                ans2 = len(num) - 1
        # print(ans1, ans2)
        return min(ans1, ans2)


data = [
    "275"
]
r = Solution().minimumOperations(* data)
print(r)