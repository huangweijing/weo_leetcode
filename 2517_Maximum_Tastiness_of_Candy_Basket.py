from typing import List
import math

class Solution:
    def check_min(self, price: List[int], k: int, min_diff: int) -> bool:
        count, i, last = 0, 1, price[0]
        while count + 1 < k:
            diff = 0
            while i < len(price) and diff < min_diff:
                diff = price[i] - last
                i += 1
            if diff < min_diff:
                return False
            else:
                count += 1
                # print(f"price={price}, k={k}, count={count}, i={i}, diff={diff}, last={last}")
                last = price[i - 1]
        return True

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        low, high = 0, 10 ** 9
        mid = (low + high) >> 1
        while low < mid < high:
            chk = self.check_min(price, k, mid)
            # print(low, mid, high, chk)
            if chk:
                low = mid
            else:
                high = mid
            mid = (low + high) >> 1
        return mid

data = [
    [34,116,83,15,150,56,69,42,26]
    , 6
]
# data[0].sort()
# r = Solution().check_min(*data, 20)
r = Solution().maximumTastiness(* data)
print(r)
