class Solution:
    def calc_sum(self, n: int, idx: int, val: int) -> int:
        if val <= idx + 1:
            v1 = ((1 + val) * val) >> 1
            v1 += idx + 1 - val
        else:
            v1 = ((val + val - idx) * (idx + 1)) >> 1

        if val <= n - idx:
            v2 = ((1 + val) * val) >> 1
            v2 += n - idx - val
        else:
            v2 = ((val + val - (n - idx) + 1) * (n - idx)) >> 1

        return v1 + v2 - val


    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, 10 ** 9
        mid = (left + right) >> 1
        while left <= right:
            v1 = self.calc_sum(n, index, mid)
            v2 = self.calc_sum(n, index, mid + 1)
            # print(f"mid={mid}, v1={v1}, mid+1={mid+1}, v2={v2}")
            # print(f"left={left}, right={right}")
            if v1 <= maxSum < v2:
                return mid
            if v1 > maxSum:
                right = mid - 1
            elif v2 <= maxSum:
                left = mid + 1
            # print(f"new_left={left}, new_right={right}")
            mid = (left + right) >> 1

        return mid

r = Solution().maxValue(3, 2, 18)
print(r)
