class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ranking = set[int]()
        for num in nums:
            ranking.add(num)
            if len(ranking) > 3:
                ranking_list = list(ranking)
                ranking_list.sort(reverse=True)
                ranking_list.pop()
                ranking = set(ranking_list)

        ranking_list = list(ranking)
        ranking_list.sort(reverse=True)
        if len(ranking_list) < 3:
            return ranking_list[0]
        else:
            return ranking_list[-1]

