from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k > 0:
            ans = []
            sum_k = sum(code[: k])
            for i in range(len(code)):
                sum_k += code[(i + k) % len(code)] - code[i]
                ans.append(sum_k)
            return ans
        elif k == 0:
            return [0] * len(code)
        elif k < 0:
            sum_k = sum(code[k:])
            ans = [sum_k]
            for i in range(len(code)):
                if i == 0:
                    continue
                sum_k += code[i - 1] - code[i + k - 1]
                ans.append(sum_k)
            return ans


data = [
    [2, 4, 9, 3]
    , -2
]
r = Solution().decrypt(* data)
print(r)


