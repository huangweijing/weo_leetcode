from typing import List
import bisect


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        max_pop = 0
        ans = 0
        ages = sorted(set(log[0] for log in logs))
        for i in ages:
            population = 0
            for log in logs:
                if log[0] <= i < log[1]:
                    population += 1
                    if population > max_pop:
                        max_pop = population
                        ans = i
        return ans

