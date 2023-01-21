class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        arr = [a, b, c]
        arr.sort()
        ans = [0, 0]
        if arr[0] + 2 == arr[2]:
            return ans
        ans[1] = (arr[1] - arr[0] - 1) + (arr[2] - arr[1] - 1)
        if arr[0] + 1 == arr[1] or arr[1] + 1 == arr[2]\
                or arr[1] + 2 == arr[2] or arr[0] + 2 == arr[1]:
            ans[0] = 1
        else:
            ans[0] = 2
        return ans