import bisect

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        int_list = list(map(int, str(n)))
        prefix_sum, prefix_sum_arr = 0, []
        for i in int_list:
            prefix_sum += i
            prefix_sum_arr.append(prefix_sum)

        if target >= prefix_sum:
            return 0

        idx = bisect.bisect_left(prefix_sum_arr, target - 1)
        if prefix_sum_arr[idx] > target - 1:
            idx -= 1
        amount = 10 ** (len(int_list) - 1 - idx)
        return amount - n % amount

data = [
    467
    , 200
]
r = Solution().makeIntegerBeautiful(* data)
print(r)