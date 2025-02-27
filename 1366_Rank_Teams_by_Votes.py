from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank = [[0] * len(votes[0]) for _ in range(26)]
        for vote in votes:
            for i, ch in enumerate(vote):
                rank[ord(ch) - ord('A')][i] += 1
        # print(rank)
        return "".join([rec[2] for rec in sorted([[rank[ord(ch) - ord('A')], -ord(ch), ch] for ch in votes[0]], reverse=True)])
            


data = ["BCA","CAB","CBA","ABC","ACB","BAC"]
r = Solution().rankTeams(data)
print(r)