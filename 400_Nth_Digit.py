import bisect
import math


class Solution:
    def findNthDigit(self, n: int) -> int:
        section = []
        section.extend([9 * (10 ** i) * (i + 1) for i in range(31)])
        section2 = [9 * (10 ** i) for i in range(31)]
        prefix_sum_arr = []
        prefix_sum = 0
        for sec in section:
            prefix_sum += sec
            prefix_sum_arr.append(prefix_sum)
        # print(prefix_sum_arr)
        # print(section)

        idx = bisect.bisect_left(prefix_sum_arr, n)
        if idx == 0:
            return n

        threshold = prefix_sum_arr[idx - 1]
        num = math.ceil((n - threshold) / (idx + 1))
        num2 = (n - threshold - 1) % (idx + 1)
        num3 = num + int("9" * idx)
        # print(f"num={num}, num2={num2}, num3={num3}, threshold={threshold}, idx={idx}")

        return int(str(num3)[num2])


r = Solution().findNthDigit(15)
for i in range(1000):
    print(Solution().findNthDigit(i), end="")