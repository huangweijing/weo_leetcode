class Solution:
    def my_happy(self, n: int, appeared_nums:set[int]) -> bool:
        if n == 1:
            return True
        nstr = str(n)
        nsum = 0
        for ch in nstr:
            num = ord(ch) - ord("0")
            nsum += num * num
        if nsum != 1 and nsum in appeared_nums:
            return False
        appeared_nums.add(nsum)
        return self.my_happy(nsum, appeared_nums)


    def isHappy(self, n: int) -> bool:
        return self.my_happy(n, set[int]())

r = Solution().isHappy(2 ** 31 - 1)
print(r)