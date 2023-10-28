from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = bin(label)[3:]
        ans = [1]
        cur = 1
        for i, ch in enumerate(path):
            row_idx = i + 2
            odd_row = (len(path) - row_idx) % 2 == 0
            row_min = 1 << (row_idx - 1)
            row_max = (1 << row_idx) - 1
            # print(row_idx, odd_row)
            if ch == "0":
                cur = cur * 2
            else:
                cur = cur * 2 + 1
            # print(cur)
            if not odd_row:
                ans.append(cur)
            if odd_row:
                ans.append(row_max - (cur - row_min))
        return ans

data = 26
r = Solution().pathInZigZagTree(data)
print(r)



