from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        visited = set[int]()
        group_idx = 0
        rem_dict = dict[int, int]()
        for i in range(k):
            if i in visited:
                continue
            rem_set = set[int]()
            val = i
            while val not in rem_set:
                rem_set.add(val)
                visited.add(val)
                val = (len(arr) + val) % k
                rem_dict[val] = group_idx
            group_idx += 1

        group_arr = [list[int]() for _ in range(group_idx)]
        ans = 0
        for i, num in enumerate(arr):
            group_arr[rem_dict[i % k]].append(num)
        # print(group_arr)
        for num_list in group_arr:
            num_list.sort()
            ans += sum(map(lambda x: abs(x - num_list[len(num_list) >> 1]), num_list))
        return ans


data = [
    [1, 4, 1, 3, 4, 7, 8, 12, 10, 5]
    , 2
]
r = Solution().makeSubKSumEqual(*data)
print(r)
