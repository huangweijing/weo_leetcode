from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[0] * (10 ** 7) + x[1])
        result = [[-1, -1] for i in range(len(people))]
        for p in people:
            # print(p, result)
            idx = 0
            people_cnt = p[1] + 1
            while idx < len(result):
                if result[idx][1] == -1 or result[idx][0] == p[0]:
                    people_cnt -= 1
                else:
                    idx += 1
                    continue

                if people_cnt == 0:
                    result[idx][0] = p[0]
                    result[idx][1] = p[1]
                idx += 1
        return result

sol = Solution()
r = sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])
print(r)
