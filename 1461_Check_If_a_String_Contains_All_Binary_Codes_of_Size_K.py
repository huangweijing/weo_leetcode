class Solution:
    def build_tree_array(k):
        tree_arr_size = 2 ** (k+1) - 1
        tree_arr = ["0"] * tree_arr_size
        for i in range(tree_arr_size):
            if i & 1 == 1:
                tree_arr[i] = "1"
        return tree_arr

    def build_has_visited_arr(k):
        visited_arr_size = 2 ** (k+1) - 1
        visited_arr = [0] * visited_arr_size
        return visited_arr

    def update_has_visited(visisted_arr, tree_idx):
        if visisted_arr[tree_idx] == 1:
            return
        visisted_arr[tree_idx] = 1
        if tree_idx & 1 == 1:
            if visisted_arr[tree_idx + 1] == 0:
                return
            else:
                Solution.update_has_visited(visisted_arr, (tree_idx - 1) >> 1)
        else:
            if visisted_arr[tree_idx - 1] == 0:
                return
            else:
                Solution.update_has_visited(visisted_arr, (tree_idx - 2) >> 1)

    def hasAllCodes(self, s: str, k: int) -> bool:
        tree_arr = Solution.build_tree_array(k)
        has_visited_arr = Solution.build_has_visited_arr(k)

        idx = 0
        new_found = 0
        while idx < len(s) - k + 1:
            sub_str_idx = 0
            tree_idx = 0
            while sub_str_idx < k:
                left_node = tree_arr[tree_idx * 2 + 1]
                right_node = tree_arr[tree_idx * 2 + 2]
                # print(s[idx + sub_str_idx], tree_idx, left_node, right_node)
                if left_node == s[idx + sub_str_idx]:
                    tree_idx = tree_idx * 2 + 1
                if right_node == s[idx + sub_str_idx]:
                    tree_idx = tree_idx * 2 + 2
                sub_str_idx += 1
                if has_visited_arr[tree_idx] == 1:
                    break

            # end of the tree and found new pattern
            if sub_str_idx == k and has_visited_arr[tree_idx] == 0:
                new_found += 1
                Solution.update_has_visited(has_visited_arr, tree_idx)
                # print(s[idx: idx + k])
            # has_visited_arr[tree_idx] = 1
            idx += 1

        if new_found == 2 ** k:
            return True
        else:
            return False

class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code_set = set()
        idx = 0
        while idx < len(s) - k + 1:
            code_set.add(s[idx: idx + k])
            idx += 1

        return len(code_set) == 2 ** k

sol = Solution()
r = sol.hasAllCodes("100101010101101010101010", k=3)
print(r)

sol2 = Solution2()
r = sol2.hasAllCodes("100101010101101010101010", k=3)
print(r)

# print( 8 >> 1)