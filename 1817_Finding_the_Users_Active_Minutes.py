from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_min = dict[int, set[int]]()
        for log in logs:
            if log[0] not in user_min:
                user_min[log[0]] = set[int]()
            user_min[log[0]].add(log[1])
        result = [0] * k
        for key, val in user_min.items():
            result[len(val) - 1] += 1
        return result
