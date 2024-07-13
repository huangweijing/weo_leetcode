from typing import List


class Solution:
    def my_sol(self, nums: List[int], k: int) -> int:
        flip_arr = [0] * len(nums)
        flip_cnt = 0
        ans = 0
        for i, num in enumerate(nums):
            if flip_cnt > 0 and flip_arr[i] > 0:
                flip_arr[i + flip_arr[i]] = flip_cnt - flip_arr[i]
                flip_arr[i] = 0
                flip_cnt = 0
            else:
                flip_cnt = max(flip_cnt, flip_arr[i])
                flip_arr[i] = 0

            if (flip_cnt > 0 and num == 0) or (flip_cnt == 0 and num == 1):
                flip_cnt = flip_cnt - 1
            else:
                if i + k - 1 > len(nums) - 1:
                    # print(i, k, i + k - 1)
                    return -1
                ans += 1
                # print(f"i={i}, flip_cnt={flip_cnt}, num={num}")
                if flip_cnt == 0 and num == 0:
                    flip_cnt = k - 1
                elif flip_cnt > 0 and num == 1:
                    # print(f"flip_arr[{i + flip_cnt}] = {k - flip_cnt}")
                    flip_arr[i + flip_cnt] = k - flip_cnt
                    flip_cnt = 0
            # print(f"i={i}, flip_cnt={flip_cnt}, flip_arr={flip_arr}")
        return ans

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        return self.my_sol(nums, k)
        # sol1 = self.my_sol(nums, k)
        # print("---")
        # sol2 = self.my_sol(list(reversed(nums)), k)
        # print(sol1, sol2)
        # if max(sol1, sol2) == -1:
        #     return -1
        # elif min(sol1, sol2) == -1:
        #     return max(sol1, sol2)
        # else:
        #     return min(sol1, sol2)



data = [
    [0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0]
    , 8
]
r = Solution().minKBitFlips(* data)
print(r)








