from typing import List
from collections import Counter
import math

class Solution:

    MODULUS = 10 ** 9 + 7

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr_cnt = Counter(arr)
        arr = list(arr_cnt.keys())
        arr.sort()
        ans = 0
        for i in range(len(arr)):
            tmp_cnt = Counter()
            tmp_cnt[arr[i]] += 1
            for j in range(i, len(arr)):
                # print(f"i={i}, arr[i]={arr[i]}, j={j}, arr[j]={arr[j]}")
                tmp_cnt[arr[j]] += 1
                if tmp_cnt[arr[j]] > arr_cnt[arr[j]]:
                    tmp_cnt[arr[j]] -= 1
                    if tmp_cnt[arr[j]] == 0:
                        del tmp_cnt[arr[j]]
                    continue
                k = target - arr[i] - arr[j]
                tmp_cnt[k] += 1
                if k >= arr[j] >= arr[i] and k in arr_cnt and tmp_cnt[k] <= arr_cnt[k]:
                    # print(arr[i], arr[j], k)
                    # print(arr_cnt, tmp_cnt, k)
                    to_plus = 1
                    for key, val in tmp_cnt.items():
                        to_plus *= math.comb(arr_cnt[key], tmp_cnt[key])
                        to_plus %= Solution.MODULUS
                    ans += to_plus
                tmp_cnt[arr[j]] -= 1
                tmp_cnt[k] -= 1
                if tmp_cnt[arr[j]] == 0:
                    del tmp_cnt[arr[j]]
                if tmp_cnt[k] == 0:
                    del tmp_cnt[k]

        return ans % Solution.MODULUS



data = [
    [1,1,2,2,3,3,4,4,5,5]
    , 8
]
r = Solution().threeSumMulti(* data)
print(r)