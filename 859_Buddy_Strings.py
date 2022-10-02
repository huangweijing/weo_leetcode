from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s_diff = []
        goal_diff = []
        s_cnt = Counter(s)
        for i in range(len(s)):
            if s[i] != goal[i]:
                s_diff.append(s[i])
                goal_diff.append(goal[i])
            if len(s_diff) > 2:
                return False
        if len(s_diff) == 0:
            if len(s_cnt) != len(s):
                # exists one letter with 2 or more occurrence
                return True
            else:
                return False
        if len(s_diff) == 1:
            return False
        if s_diff[0] != goal_diff[1] or s_diff[1] != goal_diff[0]:
            return False
        return True
