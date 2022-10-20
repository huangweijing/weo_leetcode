from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_sum_arr, prefix_sum, ans = [], 0, 0
        for num in arr:
            prefix_sum ^= num
            prefix_sum_arr.append(prefix_sum)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if i == 0:
                    a = prefix_sum_arr[j - 1]
                else:
                    a = prefix_sum_arr[j - 1] ^ prefix_sum_arr[i - 1]
                for k in range(j, len(arr)):
                    b = prefix_sum_arr[j - 1] ^ prefix_sum_arr[k]
                    if a == b:
                        ans += 1
        return ans
