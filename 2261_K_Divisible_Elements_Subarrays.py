from typing import List

class Solution:
    POW = 397
    MODULO = 100000000069
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        arr = list(map(lambda x: 1 if x % p == 0 else 0, nums))
        ans_set = set[int]()
        for i in range(len(arr)):
            cnt_one = 0
            hash1 = 0
            for j in range(i, len(arr)):
                hash1 = (hash1 * Solution.POW + nums[j] + (j + 1 - i)) % Solution.MODULO
                if arr[j] == 1:
                    cnt_one += 1
                if cnt_one <= k:
                    ans_set.add(hash1)
                else:
                    break

        return len(ans_set)

data = [
[76,85,75,16,15,27,49,100,1,14,18,4,41,24,19,80,57,16,61,2,90,63,36,2,76,97,16,84,73,2,7,48,80,40,54,83,19,29,12,35,30,7,86,48,60,34,97,85,20,70,49,76,44,16,24,21,100,24,55,13,40,60,98,43,43,54,59,25,73,96,18,15,99,16,15,22,36,4,26,4,84,78,32,69,82,37,50,2,84,65,18,51,77,66,76,78,25,92,35,32,18,25,82,77,73,46,59,45,75,71,39,37,34,2,55,57,80,55,69,46,18,56,19,31,54,50,38,64,27,55,60,43,53,51,81,25,87,1,80,81,58,78,58,71,84,48,9,94,65,21,25,81,90,48,18,44,30,36,64,55,70,46,56,43,100,93,66,65,96,9,96,57,82,91,25,47,51,90,56,1,74,80,86,58,45,67,26,76,8,81,80,67,45,26,21]
, 22
, 13
]
r = Solution().countDistinct(* data)
print(r)




