from sortedcontainers import SortedList

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = SortedList(range(1, n + 1))
        cur_idx = 0
        while len(people) > 1:
            # k = k % len(people)
            cur_idx += k - 1
            if cur_idx >= len(people):
                # print("round", cur_idx, cur_idx % len(people))
                cur_idx %= len(people)
            # print(people, cur_idx, people[cur_idx])
            del people[cur_idx]
        return people[0]

r = Solution().findTheWinner(6, 5)
print(r)

