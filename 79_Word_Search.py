from typing import List

class Solution:
    def __init__(self):
        self.board: list[list[str]] = []
        self.m = 0
        self.n = 0
        self.alp_pos = dict[str, list[tuple[int]]]()
        self.pos_found = set[tuple[int]]()
        self.found = False

    def record_alp_pos(self):
        self.m = len(self.board)
        self.n = len(self.board[0])
        for row in range(self.m):
            for col in range(self.n):
                if self.board[row][col] not in self.alp_pos.keys():
                    self.alp_pos[self.board[row][col]] = list[tuple[int, int]]()
                self.alp_pos[self.board[row][col]].append((row, col))

    def find_next_alp(self, ch: str, row:int, col:int):
        if ch not in self.alp_pos.keys():
            return []
        pos_list = self.alp_pos[ch]
        next_pos_list: list[tuple[int, int]] = list[tuple[int, int]]()
        for pos in pos_list:
            if pos[0] == row and (pos[1] == col - 1 or pos[1] == col + 1):
                next_pos_list.append((pos[0], pos[1]))
            if pos[1] == col and (pos[0] == row - 1 or pos[0] == row + 1):
                next_pos_list.append((pos[0], pos[1]))
        return next_pos_list

    def find_word(self, word: str, n: int) -> list[list[tuple[int, int]]]:
        if n == 0:
            if word[0] not in self.alp_pos.keys():
                return []
            else:
                return [[p] for p in self.alp_pos[word[0]]]

        path_list = self.find_word(word, n - 1)
        # print(path_list)
        result = []
        for path in path_list:
            # print(path)
            last_pos = path[-1]
            states = self.find_next_alp(word[n], last_pos[0], last_pos[1])
            for state in states:
                if state in path:
                    continue
                else:
                    current_path = path.copy()
                    current_path.append(state)
                    result.append(current_path)
                    # break
        return result

    def find_word2(self, word: str, row: int, col: int) -> list[tuple[int, int]]:
        if self.found:
            return None
        if len(word) == 0:
            return []
        if len(word) == 1:
            self.found = True
            return [(row, col)]
        next_pos_list = self.find_next_alp(word[1], row, col)
        for pos in next_pos_list:
            path = self.find_word2(word[1:], pos[0], pos[1])
            if path is not None and (row, col) not in path:
                result = [(row, col)]
                result.extend(path)
                print(f"word={word}, result={result}")
                # return result
        return None

    def find_word3(self, word: str, path: list[tuple[int, int]]):
        # print(word, path)

        if self.found:
            return

        if len(word) == 0:
            self.found = True
            # print(path)
            return

        next_step = self.find_next_alp(word[0], path[-1][0], path[-1][1])
        for step in next_step:
            if step not in path:
                new_path = path.copy()
                new_path.append(step)
                self.find_word3(word[1:], new_path)

    def check_alp_cnt(self, board: list[list[str]], word) -> bool:
        alp_table = dict[str, int]()
        alp_table2 = dict[str, int]()
        for row in board:
            for cell in row:
                if cell not in alp_table:
                    alp_table[cell] = 1
                else:
                    alp_table[cell] += 1
        for ch in word:
            if ch not in alp_table2:
                alp_table2[ch] = 1
            else:
                alp_table2[ch] += 1
        for key in alp_table2.keys():
            if key not in alp_table.keys():
                return False
            else:
                if alp_table2[key] > alp_table[key]:
                    return False
        return True


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.record_alp_pos()

        if len(word) > self.m * self.n:
            return False
        # print(self.check_alp_cnt(self.board, word))
        if not self.check_alp_cnt(self.board, word):
            return False

        # result = self.find_word(word, len(word) - 1)
        if word[0] in self.alp_pos.keys():
            pos_list = self.alp_pos[word[0]]
        else:
            return False

        for pos in pos_list:
            self.find_word3(word[1:], [pos])
            if self.found:
                return True
        return False


        # print(f"result={result}")
        # if len(result) == 0:
        #     return False
        # else:
        #     return True



sol = Solution()
# r = sol.exist([["A"]], "CD")
# r = sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE")
# r = sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
# r = sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB")
r = sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAA")

# sol.find_next_alp("E", 1, 3)
print(r)

