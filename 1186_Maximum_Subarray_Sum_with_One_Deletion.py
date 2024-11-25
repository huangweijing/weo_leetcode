from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # print(arr)
        start_idx = 0
        prefix_sum = 0
        min_prefix_sum = 0
        min_val = 0
        min_minus = 0
        ans = arr[0]
        for i, num in enumerate(arr):
            prefix_sum += num
            # minimum num of this subarray
            min_val = min(min_val, num)

            # deletion is available only after subarray starting idx 
            if i > start_idx:
                min_minus = min(min_minus, min_prefix_sum + min_val)
            else:
                min_minus = min(min_minus, min_prefix_sum)

            # update answer
            ans = max(ans, prefix_sum - min_minus)
            print(f"num={num}\t prefix_sum={prefix_sum}\t min_prefix_sum={min_prefix_sum}\t min_val={min_val}\t res={prefix_sum - min_minus}")

            # update minimum prefix sum
            if prefix_sum < min_prefix_sum:
                min_prefix_sum = prefix_sum
                # reset the minimum number from starting point
                min_val = 0
                min_minus = 0
                # subarray starting idx
                start_idx = i + 1
        return ans
    

data = [1,-2,0,3]
r = Solution().maximumSum(data)
print(r)
                


        