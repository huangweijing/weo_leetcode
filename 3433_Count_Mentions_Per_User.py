from typing import List
from collections import deque


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0] * numberOfUsers
        total = 0
        events.sort(key=lambda x: [int(x[1]), -ord(x[0][0])])
        offline = deque()
        for event in events:
            event[1] = int(event[1])
            while len(offline) > 0 and offline[0][0] + 60 <= event[1]:
                offline.popleft()
            if event[0] == "OFFLINE":
                offline.append([event[1], int(event[2])])
            elif event[0] == "MESSAGE":
                if event[2] == "ALL":
                    total += 1
                elif event[2] == "HERE":
                    total += 1
                    for offuser in offline:
                        ans[offuser[1]] -= 1
                else:
                    arr = event[2].split(sep=" ")
                    for token in arr:
                        ans[int(token[2:])] += 1
        return [cnt + total for cnt in ans]


data = [
    3
    , [["MESSAGE","5","HERE"],["OFFLINE","10","0"],["MESSAGE","15","HERE"],["OFFLINE","18","2"],["MESSAGE","20","HERE"]]
]
r = Solution().countMentions(*data)
print(r)