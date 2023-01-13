from typing import List
from collections import Counter

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_total_views = Counter()
        creator_best_film = dict[str, str]()
        creator_best_view = Counter()
        for i in range(len(creators)):
            creator = creators[i]
            film_id = ids[i]
            view_cnt = views[i]

            creator_total_views[creator] += view_cnt
            if creator not in creator_best_view or creator_best_view[creator] < view_cnt\
                    or (creator_best_view[creator] == view_cnt and film_id < creator_best_film[creator]):
                creator_best_view[creator] = view_cnt
                creator_best_film[creator] = film_id

        creator_views_list = list(creator_total_views.items())
        creator_views_list.sort(key=lambda x: x[1], reverse=True)
        largest_view_cnt = creator_views_list[0][1]
        # print(creator_views_list)
        ans = []
        for creator_view in creator_views_list:
            if creator_view[1] == largest_view_cnt:
                ans.append([ creator_view[0], creator_best_film[creator_view[0]] ])
            else:
                break
        return ans


    # ["alice","bob","alice","chris"]
    # , ["one","two","three","four"]
    # , [5,10,5,4]
data = [
    ["a", "a"], ["aa", "a"], [5, 5]
]
r = Solution().mostPopularCreator(* data)
print(r)

