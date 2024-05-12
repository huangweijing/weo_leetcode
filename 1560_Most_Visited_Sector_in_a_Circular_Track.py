from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        arr = [0] * n
        arr[rounds[0] - 1] = 1
        for i, rnd in enumerate(rounds[1:], start=1):
            start, end = rounds[i - 1], rounds[i] - 1
            if end < start:
                for j in range(end + 1):
                    arr[j] += 1
                for j in range(start, n):
                    arr[j] += 1
            else:
                for j in range(start, end + 1):
                    arr[j] += 1
        arr = [[i + 1, cnt] for i, cnt in enumerate(arr)]
        arr.sort(key=lambda x: [x[1], -x[0]], reverse=True)
        return [x[0] for x in arr if x[1] == arr[0][1]]

data = [
    4
    , [1,3,1,2]
    ]
r = Solution().mostVisited(* data)
print(r)
