from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        idx = 0
        vally_list = []
        candy_cnt = [None] * len(ratings)

        # find vally point
        while idx < len(ratings):
            if idx == 0 and idx < len(ratings) - 1 and ratings[idx] <= ratings[idx + 1]:
                vally_list.append(idx)
            elif idx > 0 and idx == len(ratings) - 1 and ratings[idx - 1] >= ratings[idx]:
                vally_list.append(idx)
            elif ratings[idx] <= ratings[idx - 1] and ratings[idx] <= ratings[idx + 1]:
                vally_list.append(idx)
            idx += 1

        for vally in vally_list:
            idx = 1
            candy_cnt[vally] = 1
            while vally - idx >= 0 and ratings[vally - idx] > ratings[vally - idx + 1]:
                cnt = idx + 1
                # print(candy_cnt[vally - idx], vally - idx)
                if candy_cnt[vally - idx] is None or cnt > candy_cnt[vally - idx]:
                    candy_cnt[vally - idx] = idx + 1

                idx += 1

            idx = 1
            while vally + idx < len(ratings) and ratings[vally + idx - 1] < ratings[vally + idx]:
                cnt = idx + 1
                if candy_cnt[vally + idx] is None or cnt > candy_cnt[vally + idx]:
                    candy_cnt[vally + idx] = idx + 1
                idx += 1

        # print(ratings)
        # print(candy_cnt)
        return sum(candy_cnt)

sol = Solution()
ratings = [0, 2]
# ratings = [6,5,3,2,4,4,2,6,6,6,1,2]
# ratings = [6, 5, 4, 1, 7, 2, 2, 8, 8, 8, 5, 4, 7, 6, 3, 1]
r = sol.candy(ratings)
print(r)

