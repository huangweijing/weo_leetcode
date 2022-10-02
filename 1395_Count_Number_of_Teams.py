from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        np1 = [0] * (len(rating))
        np2 = [0] * (len(rating))

        result = 0
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    np1[i] += 1
                if rating[j] > rating[i]:
                    np2[i] += 1

        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    result += np1[j]
                if rating[j] > rating[i]:
                    result += np2[j]

        return result

data_rating = [8,5,3,4,2,1]
r = Solution().numTeams(data_rating)
print(r)