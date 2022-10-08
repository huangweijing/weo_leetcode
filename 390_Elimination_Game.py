class Solution:
    def lastRemaining(self, n: int) -> int:
        l, r = 1, n
        interval, skip = 1, 2
        from_left = True
        while l < r:
            # print(l, r)
            if from_left:
                if (r - l) % skip == 0:
                    r = r - interval
                l = l + interval
            else:
                if (r - l) % skip == 0:
                    l = l + interval
                r = r - interval
            from_left = not from_left
            interval <<= 1
            skip <<= 1
        return l

result = Solution().lastRemaining(7)
print(result)

