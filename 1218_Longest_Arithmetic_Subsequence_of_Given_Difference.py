from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int]
                           , difference: int) -> int:
        longest_seq_dict = dict[int, int]()
        ans = 1
        for num in arr:
            length = 1
            if num - difference in longest_seq_dict:
                length = longest_seq_dict[num - difference] + 1
            if num in longest_seq_dict:
                length = max(length, longest_seq_dict[num])
            longest_seq_dict[num] = length
            ans = max(length, ans)
        return ans

data = [
    [1, 3, 5, 7]
    , 1
]
r = Solution().longestSubsequence(* data)
print(r)