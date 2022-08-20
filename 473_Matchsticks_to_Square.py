from typing import List

class Solution:
    def __init__(self):
        self.global_used_idx = set[int]()
        self.found = False
        self.side_len = 0
        self.okay_cnt = 0


    def find_sum2(self, num_list: list[int], num_to_sum: int):
        print(num_list, num_to_sum, self.okay_cnt)
        if self.okay_cnt == 3 and num_to_sum == 0:
            self.found = True
            return
        if num_to_sum == 0:
            num_to_sum = self.side_len
            self.okay_cnt += 1
        tried_num = set[int]()
        for idx, num in enumerate(num_list):
            if num in tried_num:
                continue
            else:
                tried_num.add(num)

            if num > num_to_sum:
                return
            new_num_list = num_list.copy()
            new_num_list.remove(num)
            self.find_sum2(new_num_list, num_to_sum - num)
            if num_to_sum - num == 0:
                self.okay_cnt -= 1

            if self.found:
                return


    def find_sum(self, num_list: list[int], used_idx: set[int], num_to_sum: int):
        # print(num_list, used_idx, num_to_sum, self.okay_cnt)
        if self.okay_cnt == 3 and num_to_sum == 0:
            # if len(used_idx) == len(num_list) and num_to_sum == 0:
            self.found = True
            # print(num_list, used_idx)
            return
        if num_to_sum == 0:
            num_to_sum = self.side_len
            self.okay_cnt += 1

        for idx, num in enumerate(num_list):
            if idx in used_idx:
                continue
            if num > num_to_sum:
                return
            used_idx.add(idx)
            self.find_sum(num_list, used_idx, num_to_sum - num)
            if num_to_sum - num == 0:
                self.okay_cnt -= 1

            if self.found:
                return
            used_idx.remove(idx)

        # if num_to_sum == 0:
        #     self.okay_cnt -= 1

    # def find_sum(self, num_list: list[int], used_idx: set[int], num_to_sum: int):
    #     if num_to_sum == 0:
    #         self.global_used_idx = self.global_used_idx.union(used_idx)
    #         print(used_idx)
    #         self.found = True
    #         return
    #     used_idx = used_idx.copy()
    #     for idx, num in enumerate(num_list):
    #         if idx in used_idx:
    #             continue
    #         if num > num_to_sum:
    #             continue
    #         used_idx.add(idx)
    #         self.find_sum(num_list, used_idx, num_to_sum - num)
    #         if self.found:
    #             return
    #         used_idx.remove(idx)


    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        sum_len = sum(matchsticks)
        if sum_len & 3 != 0:
            return False
        self.side_len = int(sum(matchsticks) / 4)
        for num in matchsticks:
            if num > self.side_len:
                return False

        self.found = False
        # self.find_sum(matchsticks, set[int](), self.side_len)
        self.find_sum2(matchsticks, self.side_len)
        if not self.found:
            return False
        else:
            return True
#
r = Solution().makesquare([4,13,1,1,14,15,1,3,13,1,3,5,2,8,12])
print(r)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s1.union(s2)
# print(s1)