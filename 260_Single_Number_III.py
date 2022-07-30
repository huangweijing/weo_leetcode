class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        xor_dig = 0
        for i in range(32):
            dig = (xor_sum & (1 << i)) >> i
            if dig == 1:
                xor_dig = i
                break

        num1 = 0
        num2 = 0
        for num in nums:
            if (num & (1 << xor_dig)) >> xor_dig:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

r = Solution().singleNumber([1,2,1,-8,2,5])
print(r)