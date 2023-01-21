class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target != startValue:
            if target < startValue:
                ans += startValue - target
                target = startValue
            elif len(bin(target)) >= len(bin(startValue)):
                ans += 1
                if target & 1 == 0:
                    target >>= 1
                else:
                    target += 1
            # print(startValue, target)
        return ans

r = Solution().brokenCalc(3, 124089)
print(r)