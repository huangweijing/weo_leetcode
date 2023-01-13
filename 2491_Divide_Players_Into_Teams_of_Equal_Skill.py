from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        skill_val = skill[0] + skill[len(skill) - 1]
        for i in range(len(skill) >> 1):
            if skill_val != skill[i] + skill[len(skill) - 1 - i]:
                return -1
            ans += skill[i] * skill[len(skill) - 1 - i]
        return ans
