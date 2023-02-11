from typing import List
import math

class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1_path_set, node2_path_set = set(), set()
        node1_path_arr, node2_path_arr = [], []
        while node1 != -1 and node1 not in node1_path_set:
            node1_path_set.add(node1)
            node1_path_arr.append(node1)
            node1 = edges[node1]
        while node2 != -1 and node2 not in node2_path_set:
            node2_path_set.add(node2)
            node2_path_arr.append(node2)
            node2 = edges[node2]

        node1_path_len, node2_path_len = 0, 0
        ans_node = 0
        ans = math.inf
        for node in node1_path_arr:
            if node in node2_path_set:
                path_length = max(node1_path_len, node2_path_arr.index(node))
                if path_length < ans:
                    ans = path_length
                    ans_node = node
                elif path_length == ans:
                    ans_node = min(node, ans_node)
                break
            node1_path_len += 1
        for node in node2_path_arr:
            if node in node1_path_set:
                path_length = max(node2_path_len, node1_path_arr.index(node))
                if path_length < ans:
                    ans = path_length
                    ans_node = node
                elif path_length == ans:
                    ans_node = min(node, ans_node)
                break
            node2_path_len += 1
        if ans == math.inf:
            return -1
        return ans_node

data = [
    [2, 0, 0]
    , 0
    , 2
]
r = Solution().closestMeetingNode(* data)
print(r)