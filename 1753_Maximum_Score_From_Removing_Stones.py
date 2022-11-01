class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [a, b, c]
        arr.sort()
        if arr[2] > arr[1] + arr[0]:
            return arr[1] + arr[0]
        else:
            return a + b + c >> 1

data = [
3
, 8
, 2
]
r = Solution().maximumScore(* data)
print(r)