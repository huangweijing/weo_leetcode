from typing import List
from collections import Counter, deque


class Solution:
    def arr_is_okay(self, bit_arr:List[int]) -> bool:
        for bit in arr:
            if bit > 1:
                return False
        return True

    def substract_arr(self, bit_arr1:List[int], bit_arr2:List[int]) -> bool:
        result = True
        for i in range(len(bit_arr1)):
            bit_arr1[i] -= bit_arr2[i]
            if bit_arr1[i] > 1:
                result = False
        return result


    def longestNiceSubarray(self, nums: List[int]) -> int:
        bit_sum = [0] * 32
        mask = [ 1 << i for i in range(32)]
        # print(mask)
        max_len = 0
        num_que = deque()
        for num in nums:
            bit_arr = [0] * 32
            can_be_add = True
            for i, m in enumerate(mask):
                bit_arr[i] = 0 if (mask[i] & num) == 0 else 1
                bit_sum[i] += bit_arr[i]
                if bit_sum[i] > 1:
                    can_be_add = False
            # print(f"can_be_add={can_be_add}, bit_sum[i]={bit_sum}")
            num_que.append(bit_arr)

            if can_be_add:
                max_len = max(max_len, len(num_que))
            else:
                need_del = num_que.popleft()
                while not self.substract_arr(bit_sum, need_del):
                    need_del = num_que.popleft()
        return max_len


r = Solution().longestNiceSubarray([1,2,4,2,8,16])
print(r)
# print(bin(48))
