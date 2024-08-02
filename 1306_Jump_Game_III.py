from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set[int]()
        cur_node = set[int]([start])
        while len(cur_node) > 0:
            node = cur_node.pop()
            visited.add(node)
            if 0 <= node + arr[node] < len(arr) and node + arr[node] not in visited:
                cur_node.add(node + arr[node])
            if 0 <= node - arr[node] < len(arr) and node - arr[node] not in visited:
                cur_node.add(node - arr[node])
            # print(visited, cur_node)
        return sum(1 for i in visited if arr[i] == 0) > 0
            

data = [
    [0,3,0,6,3,3,4]
    , 6
]
r = Solution().canReach(*data)
print(r)