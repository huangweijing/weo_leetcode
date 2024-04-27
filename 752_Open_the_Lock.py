from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        visited = set[str](["0000"])
        node_list = ["0000"]
        step = 0
        while len(node_list) > 0:
            step += 1
            new_node_list = []
            while len(node_list) > 0:
                node = node_list.pop()
                for i in range(4):
                    if int(node[i: i + 1]) < 9:
                        new_node = node[: i] + str(int(node[i: i + 1]) + 1) + node[i + 1:]
                    else:
                        new_node = node[: i] + "0" + node[i + 1:]
                    if new_node not in deadends:
                        if new_node == target:
                            return step
                        if new_node not in visited:
                            visited.add(new_node)
                            new_node_list.append(new_node)
                    if int(node[i: i + 1]) > 0:
                        new_node = node[: i] + str(int(node[i: i + 1]) - 1) + node[i + 1:]
                    else:
                        new_node = node[: i] + "9" + node[i + 1:]
                    if new_node not in deadends:
                        if new_node == target:
                            return step
                        if new_node not in visited:
                            visited.add(new_node)
                            new_node_list.append(new_node)
            node_list = new_node_list
            # print(node_list)
        return -1


data = [
    ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    , "8888"
]
r = Solution().openLock(* data)
print(r)