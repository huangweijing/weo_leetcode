class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # print(s, k)
        idx = 0
        word_cnt = 0
        while idx < len(s):
            while idx < len(s) and not "2" <= s[idx] <= "9":
                word_cnt += 1
                if word_cnt == k:
                    return s[idx]
                idx += 1
            while idx < len(s) and "2" <= s[idx] <= "9":
                if word_cnt * int(s[idx]) >= k:
                    return self.decodeAtIndex(s[: idx], (k - 1) % word_cnt + 1)
                word_cnt *= int(s[idx])
                idx += 1

data = ["ha22", 5]
r = Solution().decodeAtIndex(*data)
print(r)