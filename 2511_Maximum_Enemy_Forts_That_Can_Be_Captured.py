from typing import List


class Solution:
    def my_sol(self, forts: list[int]) -> int:
        fort_idx = 0
        ans = 0
        while fort_idx < len(forts):
            if forts[fort_idx] == 1:
                print(forts[:fort_idx+1])
                fort_idx += 1
                enemy_count = 0
                while fort_idx < len(forts) and forts[fort_idx] == 0:
                    fort_idx += 1
                    enemy_count += 1
                if fort_idx < len(forts) and forts[fort_idx] == -1:
                    ans = max(ans, enemy_count)
                continue
            fort_idx += 1
        return ans

    def captureForts(self, forts: List[int]) -> int:
        return max(self.my_sol(forts), self.my_sol(forts[::-1]))


data = [-1,-1,-1,-1,1,-1,0,1,1,-1,1,-1]
r = Solution().captureForts(data)
print(r)


