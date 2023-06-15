from typing import List

class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right, mid = 0, len(letters) - 1, (len(letters) - 1) >> 1
        if target >= letters[right]:
            return letters[0]
        if target < letters[left]:
            return letters[left]
        while left <= right:
            # print(left, mid, right)
            if letters[mid] <= target < letters[mid + 1]:
                return letters[mid + 1]
            if letters[mid + 1] <= target:
                left = mid + 1
            elif target < letters[mid]:
                right = mid - 1
            mid = (left + right) >> 1
        return letters[mid]

data = [
    ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"]
    , "e"
]
r = Solution().nextGreatestLetter(* data)
print(r)
