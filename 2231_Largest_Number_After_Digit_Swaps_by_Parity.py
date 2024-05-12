class Solution:
    def largestInteger(self, num: int) -> int:
        odd_arr, even_arr = [], []
        n = num
        while n > 0:
            rem = n % 10
            n //= 10
            if rem & 1 == 0:
                even_arr.append(rem)
            else:
                odd_arr.append(rem)
        even_arr.sort()
        odd_arr.sort()
        ans = 0
        for v in str(num):
            if int(v) & 1 == 0:
                ans = ans * 10 + even_arr.pop()
            else:
                ans = ans * 10 + odd_arr.pop()
        return ans
