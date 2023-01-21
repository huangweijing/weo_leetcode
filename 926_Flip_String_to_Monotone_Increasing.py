class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        i = len(s) - 1
        zeros_to_handle, ones_to_handle = 0, 0
        while i >= 0:
            zeros, ones = 0, 0
            while i >= 0 and s[i] == "0":
                zeros += 1
                i -= 1
            while i >= 0 and s[i] == "1":
                ones += 1
                i -= 1
            # final block with only zeros
            if i < 0 and ones == 0:
                break
            zeros_to_handle += zeros
            ones_to_handle += ones
            # print(i, zeros, ones, zeros_to_handle, ones_to_handle)
            if zeros_to_handle > ones_to_handle:
                # ans += ones
                continue
            else:
                ans += zeros_to_handle
                zeros_to_handle, ones_to_handle = 0, 0

        if zeros_to_handle > ones_to_handle:
            ans += ones_to_handle
        else:
            ans += zeros_to_handle
        return ans

r = Solution().minFlipsMonoIncr("111011100100100")
print(r)