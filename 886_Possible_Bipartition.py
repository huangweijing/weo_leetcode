from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_set_arr = [set() for _ in range(n)]
        dislike_color = [0] * n

        for dislike in dislikes:
            dislike_set_arr[dislike[0] - 1].add(dislike[1] - 1)
            dislike_set_arr[dislike[1] - 1].add(dislike[0] - 1)

        # print(dislike_set_arr)

        for i in range(n):
            # print("paint " + str(i))
            dislike_set = dislike_set_arr[i]
            if len(dislike_set) == 0:
                continue
            elif dislike_color[i] != 0:
                continue
            else:
                dislike_color[i] = 1
                color = 1
                adj_nodes = dislike_set_arr[i]
                while len(adj_nodes) > 0:
                    # print("round " + str(color), adj_nodes)
                    next_node = set()
                    while len(adj_nodes) > 0:
                        node = adj_nodes.pop()
                        # print(node)
                        if dislike_color[node] == 0:
                            dislike_color[node] = 3 - color
                            next_node = next_node.union(dislike_set_arr[node])
                            # print(node, next_node)
                        elif dislike_color[node] == color:
                            # print(dislike_color, i, node)
                            return False
                        else:
                            continue
                    color = 3 - color
                    adj_nodes = next_node
            # print(dislike_color)
        return True

data = [
    10,
    [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]
]
r = Solution().possibleBipartition(* data)
print(r)