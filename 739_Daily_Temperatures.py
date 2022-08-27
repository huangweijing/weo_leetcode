from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = [] # idx, temperature
        result = []
        for i in range(len(temperatures) - 1, -1, -1):
            while len(temp_stack) > 0 and temp_stack[-1][1] <= temperatures[i]:
                temp_stack.pop()
            if len(temp_stack) > 0:
                result.append(temp_stack[-1][0] - i)
            else:
                result.append(0)
            temp_stack.append((i, temperatures[i]))
        result.reverse()
        return result

data = [73,74,75,71,69,72,76,73]
r = Solution().dailyTemperatures(data)
print(r)
