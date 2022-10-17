class Solution:
    alp_table = [
        [int(i / 5), (i % 5)] for i in range(26)
    ]

    def get_idx(self, alp: str) -> list[int]:
        return Solution.alp_table[ord(alp) - ord("a")]

    def move_to(self, pos: list[int], dest_pos: list[int]):
        path = ""
        if dest_pos == [5, 0]:
            path += self.move_to(pos, [4, 0])
            pos = [4, 0]
        rows = dest_pos[0] - pos[0]
        cols = dest_pos[1] - pos[1]
        if rows < 0:
            path += "U" * abs(rows)
        if rows > 0:
            path += "D" * abs(rows)
        if cols < 0:
            path += "L" * abs(cols)
        if cols > 0:
            path += "R" * abs(cols)
        return path


    def alphabetBoardPath(self, target: str) -> str:
        pos = [0, 0]
        path = ""
        for ch in target:
            dest_pos = self.get_idx(ch)
            if pos != dest_pos:
                path += self.move_to(pos, dest_pos)
            path += "!"
            pos = dest_pos

        return path

r = Solution().alphabetBoardPath("zyz")
# RR!DDRR!UUL!R!
# RR!DDRRRR!RRR!RRRR!
print(r)
