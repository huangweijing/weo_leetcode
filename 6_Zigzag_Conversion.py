class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        s_len = len(s)

        if numRows == 1:
            return s

        # 頂点
        k = 0
        while 2 * k * (numRows - 1) < s_len:
            result.append(s[2 * k * (numRows - 1)])
            k = k + 1

        i = 1
        while i < numRows - 1:

            # 真ん中
            k = 0
            while True:
                left_idx = 2 * k * (numRows - 1) - i
                if left_idx >= s_len:
                    break
                elif left_idx > 0:
                    result.append(s[left_idx])

                right_idx = 2 * k * (numRows - 1) + i
                if right_idx >= s_len:
                    break
                else:
                    result.append(s[right_idx])
                k = k + 1
            i = i + 1

        # 足場
        k = 0
        while (2 * k + 1) * (numRows - 1) < s_len:
            result.append(s[(2 * k + 1) * (numRows - 1)])
            k = k + 1

        return "".join(result)


sol = Solution()
r = sol.convert("abcde", 4)
print(r)
# t = [[None] * 4] * 3
# print(t)