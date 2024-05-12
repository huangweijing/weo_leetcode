import bisect

class Solution:
    def balancedString(self, s: str) -> int:
        ans = len(s)
        right_part = []
        qwer = (0, 0, 0, 0)
        for i, ch in enumerate(reversed(s)):
            if ch == "Q":
                qwer = (qwer[0] + 1, qwer[1], qwer[2], qwer[3])
            elif ch == "W":
                qwer = (qwer[0], qwer[1] + 1, qwer[2], qwer[3])
            elif ch == "E":
                qwer = (qwer[0], qwer[1], qwer[2] + 1, qwer[3])
            elif ch == "R":
                qwer = (qwer[0], qwer[1], qwer[2], qwer[3] + 1)
            right_part.append(qwer)
        right_idx = 0
        cnt = len(s) // 4
        qwer = (0, 0, 0, 0)
        for i, ch in enumerate(s):
            if ch == "Q":
                qwer = (qwer[0] + 1, qwer[1], qwer[2], qwer[3])
            elif ch == "W":
                qwer = (qwer[0], qwer[1] + 1, qwer[2], qwer[3])
            elif ch == "E":
                qwer = (qwer[0], qwer[1], qwer[2] + 1, qwer[3])
            elif ch == "R":
                qwer = (qwer[0], qwer[1], qwer[2], qwer[3] + 1)

            bisect.bisect_left(right_part, cnt - qwer[0], lambda x: x[0])

        return ans


# data = "QWER"
# r = Solution().balancedString(data)
# print(r)

# arr = [[1, 2], [2, 1]]
# print(bisect.bisect_left(arr, 2, key=lambda x: x[0]))