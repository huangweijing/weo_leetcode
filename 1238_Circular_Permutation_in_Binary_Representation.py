from typing import List


class Solution:
    def perm(self, n: int) -> list[int]:
        if n == 1:
            return [0, 1]
        ret = []
        sub_ret = self.perm(n - 1)
        ret.extend(sub_ret)
        for val in reversed(sub_ret):
            ret.append((1 << (n - 1)) + val)
        return ret

    def circularPermutation(self, n: int, start: int) -> List[int]:
        arr = self.perm(n)
        for i, n in enumerate(arr):
            if n == start:
                return arr[i: ] + arr[: i]
        return arr

print(Solution().circularPermutation(3, 2))