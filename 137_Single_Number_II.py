class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bin_cnt = [0] * 32

        for num in nums:
            for i in range(len(bin_cnt)):
                bin_cnt[i] += (num & (1 << i)) >> i
            # print(bin_cnt)

        result = 0
        for i, num in enumerate(bin_cnt):
            result += (num % 3) << i
        if result & (1 << 31) != 0:
            result = result - (1 << 32)
        return result

r = Solution().singleNumber([2,2,2 ** 31,2])
# # print(bin(r))
# # print(bin((1 << 32)))
# # print(r & (1 << 32))
# if r & (1 << 31) != 0:
#     r = r - (1 << 32)
print(r)

