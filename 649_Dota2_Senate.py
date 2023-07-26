from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_queue = deque(senate)
        dire_score = 0
        while len(senate_queue) > 0:
            # print(senate_queue, dire_score)
            s = senate_queue.popleft()
            if dire_score > 0:
                if s == "D":
                    dire_score += 1
                elif s == "R":
                    dire_score -= 1
                    senate_queue.append("D")
            elif dire_score < 0:
                if s == "R":
                    dire_score -= 1
                elif s == "D":
                    dire_score += 1
                    senate_queue.append("R")
            else:
                if s == "R":
                    dire_score -= 1
                elif s == "D":
                    dire_score += 1

        if dire_score > 0:
            return "Dire"
        else:
            return "Radiant"


data = "DDDRRRR"
r = Solution().predictPartyVictory(data)
print(r)