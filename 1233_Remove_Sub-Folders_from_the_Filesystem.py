from typing import List


class TrieNode:
    def __init__(self):
        self.node = dict[str, TrieNode]()
        self.has_val = False

    def add_node(self, path: list[str]):
        if len(path) == 0:
            self.has_val = True
            return
        if path[0] in self.node:
            self.node[path[0]].add_node(path[1: ])
        else:
            new_node = TrieNode()
            new_node.add_node(path[1: ])
            self.node[path[0]] = new_node


    def get_parent_folder(self, parent_path: str) -> list[str]:
        # print(parent_path, self.node.keys())
        res = []
        if self.has_val:
            return [parent_path]
        else:
            for key in self.node:
                sub_res = self.node[key].get_parent_folder(
                    parent_path + "/" + key)
                res.extend(sub_res)
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for f in folder:
            path = f[1:].split("/")
            # print(path)
            root.add_node(path)
        ans = root.get_parent_folder("")
        return ans

# print([2, 3][2:])
data = ["/a/b/c","/a/b/ca","/a/b/d"]
r = Solution().removeSubfolders(data)
print(r)