from sortedcontainers import SortedList


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        dig_arr = [[int(val), i] for i, val in enumerate(num)]
        idx = 0
        ans = ""
        sl = SortedList(dig_arr[: k + 1])
        # print(dig_arr)
        while len(ans) != len(num) - k:
            # print(idx, sl, ans)
            ans += str(sl[0][0])
            new_idx = sl[0][1] + 1
            for i in range(idx, sl[0][1] + 1):
                # print("remove ", [int(num[i]), i])
                sl.remove([int(num[i]), i])
            if k + len(ans) < len(num):
                # print("add ", dig_arr[k + len(ans)])
                sl.add(dig_arr[k + len(ans)])
            idx = new_idx
        ans = ans.lstrip("0")
        if ans == "":
            ans = "0"
        return ans

data = [
    "10200"
    , 1
]
r = Solution().removeKdigits(*data)
print(r)
# print("00012030".lstrip("0"))
