from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        del_cnt = 0
        last_num = -1
        for i, num in enumerate(nums):
            if num == last_num and (i + del_cnt) & 1 == 1:
                # print("delete", num, i)
                del_cnt += 1
            else:
                # print("no del", num, i, (i + del_cnt) & 1, last_num)
                last_num = num
        if (len(nums) - del_cnt) & 1 == 1:
            del_cnt += 1
        return del_cnt 
    
data = [1, 1, 2, 2, 3, 3]
r = Solution().minDeletion(data)
print(r)