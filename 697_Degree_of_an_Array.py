from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_dict = dict[int, list[int]]()
        rank_dict = dict[int, int]()
        rank_rev_dict = dict[int, list[int]]()
        for i, num in enumerate(nums):
            if num not in freq_dict:
                freq_dict[num] = [i, i]
            else:
                freq_dict[num][1] = i

            if num not in rank_dict:
                rank_dict[num] = 1
            else:
                rank_dict[num] += 1

        for num in rank_dict.keys():
            rank = rank_dict[num]
            if rank not in rank_rev_dict:
                rank_rev_dict[rank] = list[int]()
            rank_rev_dict[rank].append(num)

        rank = list(rank_rev_dict.keys())
        rank.sort(reverse=True)
        min_size = len(nums)
        for num in rank_rev_dict[rank[0]]:
            if freq_dict[num][1] - freq_dict[num][0] + 1 < min_size:
                min_size = freq_dict[num][1] - freq_dict[num][0] + 1
        return min_size
