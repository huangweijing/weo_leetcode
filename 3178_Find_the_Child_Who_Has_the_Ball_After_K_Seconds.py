class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        remain = k
        direction = 1
        while remain > 0:
            if remain > n - 1:
                remain -= n - 1
                if direction == 1:
                    direction = -1
                else:
                    direction = 1
            else:
                if direction == 1:
                    return remain
                else:
                    return n - 1 - remain


data = [2, 1]
r = Solution().numberOfChild(* data)
print(r)
