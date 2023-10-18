class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        for i in range(0, len(s), (b - 1) % 2 + 1):
            next_idx = (i + 1) % len(s)
            min_dig, min_a = 10, a
            for j in range(10):
                dig = (int(s[next_idx]) + j * a) % 10
                # print(dig)
                if dig < min_dig:
                    min_dig = dig
                    min_a = a * j

            min_dig, min_a2 = 10, a
            if b % 2 == 1:
                for j in range(10):
                    dig = (int(s[i]) + j * a) % 10
                    # print(dig)
                    if dig < min_dig:
                        min_dig = dig
                        min_a2 = a * j
            else:
                min_a2 = 0

            one_choice = ""
            for idx in range(i, len(s)):
                if idx % 2 == 1:
                    dig = (int(s[idx]) + min_a) % 10
                    one_choice += str(dig)
                else:
                    dig = (int(s[idx]) + min_a2) % 10
                    one_choice += str(dig)
            for idx in range(i):
                if (i + idx) % 2 == 1:
                    dig = (int(s[idx]) + min_a) % 10
                    one_choice += str(dig)
                else:
                    dig = (int(s[idx]) + min_a2) % 10
                    one_choice += str(dig)
            # print(one_choice, min_a)
            ans = min(ans, one_choice)

        return ans

data = [
    "74", 5, 1
]
r = Solution().findLexSmallestString(* data)
print(r)

