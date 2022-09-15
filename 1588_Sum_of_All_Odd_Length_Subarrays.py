from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_arr = sum(arr)
        result = 0
        for i in range(1, len(arr) + 1, 2):
            need_minus = 0
            max_size = min(i, len(arr) - i + 1)
            for j in range(1, max_size):
                need_minus += arr[j - 1] * (max_size - j)
                need_minus += arr[-j] * (max_size - j)
            # print(f"need_minus={need_minus}, max_len={max_len}")
            result += max_size * sum_arr - need_minus
        return result

data_arr = [1,2,5,3,2,1]
r = Solution().sumOddLengthSubarrays(data_arr)
print(r)

