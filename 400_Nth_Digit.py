class Solution:
    def findNthDigit(self, n: int) -> int:
        threshold_arr = [0]
        stage = 0
        stage_arr = [0]
        for i in range(1, 30):
            threshold = 9 * (10 ** (i - 1)) * i
            threshold_arr.append(threshold)
            stage += threshold
            stage_arr.append(stage)
            if stage > 2 ** 31 - 1:
                break
        i = 0
        while n > stage_arr[i]:
            i += 1
        print(i)
        t = (n - stage_arr[i - 1]) / i
        s = str(10 ** (i - 1) + int(t))
        remainder = t - int(t)
        remainder = 1 if remainder == 0 else remainder
        # print(remainder)
        result = s[int(len(s) * remainder) - 1]
        print(t)
        print(s)
        print(int(len(s)))
        print(result)

        print(stage_arr)
        print(threshold_arr)
        return int(result)

r = Solution().findNthDigit(11)
print(r)