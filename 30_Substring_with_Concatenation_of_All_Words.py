from typing import List


class DictNode:
    def __init__(self):
        self.data: str = None
        self.children: dict[str, DictNode] = None
        self.word_end: bool = False


class DictTree:
    def __init__(self):
        self.root = DictNode()
        self.word_cnt = dict[str, int]()
        self.size = 0

    def add_new_word(self, word):
        if word in self.word_cnt.keys():
            self.word_cnt[word] += 1
        else:
            self.word_cnt[word] = 1
        self.add_word(self.root, 0, word)

    def add_word(self, node: DictNode, start_idx: int, word: str):
        if node is None:
            return
        if node.children is None:
            node.children = dict[str, DictNode]()
        if word[start_idx] not in node.children.keys():
            new_child = DictNode()
            new_child.data = word[start_idx]
            node.children[word[start_idx]] = new_child
        else:
            new_child = node.children[word[start_idx]]
        if start_idx >= len(word) - 1:
            new_child.word_end = True
            self.size += 1
            return
        else:
            self.add_word(new_child, start_idx + 1, word)

    def contain_all_words(self, s: str):
        cur_node = self.root
        matched_cnt = 0
        check_word_cnt = dict[str, int]()
        tmp_word = ""
        for ch in s:
            tmp_word += ch
            # print(ch)
            if ch in cur_node.children.keys():
                new_node = cur_node.children[ch]
                if new_node.word_end:
                    if tmp_word in check_word_cnt.keys():
                        check_word_cnt[tmp_word] += 1
                    else:
                        check_word_cnt[tmp_word] = 1
                    tmp_word = ""
                    matched_cnt += 1
                    # print("found u")
                    cur_node = self.root
                    continue
                cur_node = new_node
            else:
                return False

        for key in check_word_cnt.keys():
            if check_word_cnt[key] != self.word_cnt[key]:
                return False
        return True

        # if len(word_set) == self.size:
        #     return True
        # else:
        #     return False


    def print_me(self, node: DictNode, layer: int):
        print(f"layer={layer}, node.data={node.data}, node.word_end = {node.word_end}")
        if node.children is not None:
            for child in node.children.keys():
                self.print_me(node.children[child], layer + 1)



class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        tree = DictTree()
        sum_word_len = 0
        result_idx_arr = list[int]()
        # word_checked = dict[str, bool]()

        for word in words:
            tree.add_new_word(word)
            sum_word_len += len(word)
            # word_checked[word] = False

        str_idx = 0
        while str_idx <= len(s) - sum_word_len:
            sub_str = s[str_idx: str_idx + sum_word_len]
            is_contained = tree.contain_all_words(sub_str)
            # print(s[str_idx: str_idx + sum_word_len], is_contained)
            if is_contained:
                result_idx_arr.append(str_idx)
            str_idx += 1

        return result_idx_arr


# t = DictTree()
# t.add_new_word("abc")
# t.add_new_word("accd")
# t.add_new_word("bcd")
# r = t.contain_all_words("accdabbcd")
# print(r)

# t.print_me(t.root, 0)

sol = Solution()
r = sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
print(r)