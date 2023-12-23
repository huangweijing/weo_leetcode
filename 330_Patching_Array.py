from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.sort()
        representable_cnt = 0
        ans = 0
        for num in nums:
            while num > representable_cnt + 1:
                ans += 1
                representable_cnt += representable_cnt + 1
                if representable_cnt >= n:
                    return ans
            representable_cnt += num
            if representable_cnt >= n:
                return ans

        while representable_cnt < n:
            ans += 1
            representable_cnt += representable_cnt + 1

        return ans

data = [
    [1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94]
    , 20
]
r = Solution().minPatches(*data)
print(r)