from typing import List

class Solution:
    def floodFill(self, image: List[List[int]]
                  , sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        s = []
        visited = set[int]()
        visited.add(n * sr + sc)
        org_color = image[sr][sc]
        s.append((sr, sc))
        while len(s) > 0:
            # print(f"stack={s}")
            node = s.pop()
            # print(f"node={node}")
            image[node[0]][node[1]] = color
            up_node = (node[0] - 1, node[1])
            down_node = (node[0] + 1, node[1])
            left_node = (node[0], node[1] - 1)
            right_node = (node[0], node[1] + 1)
            # print(f"up_node={up_node}, val={image[up_node[0]][up_node[1]]}, visited={visited}")
            if up_node[0] >= 0 and image[up_node[0]][up_node[1]] == org_color \
                and up_node[0] * n + up_node[1] not in visited:
                s.append((up_node[0], up_node[1]))
                visited.add(up_node[0] * n + up_node[1])

            if down_node[0] < m and image[down_node[0]][down_node[1]] == org_color \
                and down_node[0] * n + down_node[1] not in visited:
                s.append((down_node[0], down_node[1]))
                visited.add(down_node[0] * n + down_node[1])

            if left_node[1] >= 0 and image[left_node[0]][left_node[1]] == org_color \
                and left_node[0] * n + left_node[1] not in visited:
                s.append((left_node[0], left_node[1]))
                visited.add(left_node[0] * n + left_node[1])

            if right_node[1] < n and image[right_node[0]][right_node[1]] == org_color \
                and right_node[0] * n + right_node[1] not in visited:
                s.append((right_node[0], right_node[1]))
                visited.add(right_node[0] * n + right_node[1])

        return image

data = [[[0,0,0],[0,0,0]], 1, 0, 2]
r = Solution().floodFill(* data)
print(r)
