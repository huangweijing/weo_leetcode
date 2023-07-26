from collections import Counter


class Solution:
    def splitNum(self, num: int) -> int:
        dig_list = list(str(num))
        dig_list.sort(reverse=True)
        ans = 0
        if len(dig_list) % 2 == 0:
            while len(dig_list) > 0:
                d1 = int(dig_list.pop())
                d2 = int(dig_list.pop())
                ans = ans * 10 + d1 + d2
        else:
            ans = int(dig_list.pop())
            while len(dig_list) > 0:
                d1 = int(dig_list.pop())
                d2 = int(dig_list.pop())
                ans = ans * 10 + d1 + d2
        return ans


r = Solution().splitNum(4325)
print(r)