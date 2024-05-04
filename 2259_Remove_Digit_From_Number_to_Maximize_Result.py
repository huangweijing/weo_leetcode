class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        dig_arr = []
        for i, ch in enumerate(number):
            if ch != digit:
                continue
            change = 0
            if i < len(number) - 1:
                change = int(number[i + 1]) - int(ch)
            dig_arr.append([(len(number) - i) * (1 if change > 0 else -1), i])
        dig_arr.sort(key=lambda x: x[0])
        pos = dig_arr[-1][1]
        if pos == len(number) - 1:
            ans = number[: pos]
        else:
            ans = number[: pos] + number[pos + 1:]
        print(dig_arr)
        return ans

r = Solution().removeDigit("1312321111", "3")
print(r)

