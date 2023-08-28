class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ng_set = set[int]()
        ans, cnt, num = 0, 0, 1
        while cnt < n:
            if num not in ng_set:
                if target - num > 0:
                    ng_set.add(target - num)
                ans += num
                cnt += 1
            num += 1
        return ans

r = Solution().minimumPossibleSum(3, 3)
print(r)