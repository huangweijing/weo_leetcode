from typing import List
from collections import defaultdict
from functools import cache


def longest_path(edges: list[list[int]]) -> int:
    if len(edges) == 0:
        return 0
    adj_node = defaultdict(lambda: set[int]())
    for edge in edges:
        adj_node[edge[0]].add(edge[1])
        adj_node[edge[1]].add(edge[0])

    @cache
    def get_height_of_node(parent: int, n: int) -> int:
        ret_val = 1
        for adj in adj_node[n]:
            if adj == parent:
                continue
            height = get_height_of_node(n, adj)
            ret_val = max(ret_val, height + 1)
        return ret_val
    # print(f"get_height_of_node(None, 0)={get_height_of_node(None, 0)}")
    # print(f"get_height_of_node(0, 1)={get_height_of_node(0, 1)}")
    # print(f"get_height_of_node(0, 2)={get_height_of_node(0, 2)}")
    @cache
    def longest_path_at_node(parent: int, node_at: int) -> int:
        max1, max2 = 0, 0
        for adjacent in adj_node[node_at]:
            if adjacent == parent:
                continue
            path = get_height_of_node(node_at, adjacent)
            # print(node_at, adjacent, path)
            max2 = max(path, max2)
            max1, max2 = max(max2, max1), min(max2, max1)
        # return max1 + max2 + (1 if max1 == 0 else 0) + (1 if max2 == 0 else 0)
        return max1 + max2
    # print(f"longest_path_at_node(None, 0)={longest_path_at_node(None, 0)}")

    ret = longest_path_at_node(None, 0)
    visited = set[int]([0])
    node_list = set[int]([0])
    while len(node_list) > 0:
        new_node_list = set[int]()
        while len(node_list) > 0:
            node = node_list.pop()
            for adj in adj_node[node]:
                if adj not in visited:
                    visited.add(adj)
                    ret = max(ret, longest_path_at_node(node, adj))
                    new_node_list.add(adj)
        node_list = new_node_list
    return ret


def min_height(edges: list[list[int]]) -> int:
    if len(edges) == 0:
        return 0
    adj_node = defaultdict(lambda: set[int]())
    for edge in edges:
        adj_node[edge[0]].add(edge[1])
        adj_node[edge[1]].add(edge[0])
    node_list = set[int]()
    for node in adj_node:
        if len(adj_node[node]) == 1:
            node_list.add(node)
    height = 0
    while len(adj_node) > 0:
        if len(adj_node) == 2:
            height += 2
            break
        # print(node_list)
        new_node_list = set[int]()
        for node in node_list:
            for adj in adj_node[node]:
                adj_node[adj].remove(node)
                if len(adj_node[adj]) == 1:
                    new_node_list.add(adj)
            del adj_node[node]
        height += 1
        node_list = new_node_list
    return height - 1


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # t1, t2 = list2Tree(edges1), list2Tree(edges2)
        # print(min_height(edges1), min_height(edges2))
        h1, h2 = min_height(edges1), min_height(edges2)
        p1, p2 = longest_path(edges1), longest_path(edges2)
        # print(h1, h2, p1, p2)
        return max(h1 + h2 + 1, p1, p2)


data = [
    # [[0,1],[0,2],[0,3]]
    # , [[0,1]]
    # []
    # , [[0,1],[1,2]]
    [[0, 1], [2, 0], [3, 2], [3, 6], [8, 7], [4, 8], [5, 4], [3, 5], [3, 9]]
    , [[0, 1], [0, 2], [0, 3]]
]
r = Solution().minimumDiameterAfterMerge(* data)
print(r)