class Solution:
    modulo = 10 ** 9 + 7
    num_table: list[list[int]]() = [
        [4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]
    ]

    def next_stage(self, num_cnt: list[int]) -> list[int]:
        new_cnt = [0] * 10
        for i, cnt in enumerate(num_cnt):
            for next_step in Solution.num_table[i]:
                new_cnt[next_step] += cnt
                new_cnt[next_step] %= Solution.modulo
        return new_cnt

    def knightDialer(self, n: int) -> int:
        pos = [1] * 10
        for i in range(n - 1):
            # print(pos)
            pos = self.next_stage(pos)
        return sum(pos) % Solution.modulo

r = Solution().knightDialer(5000)
print(r)