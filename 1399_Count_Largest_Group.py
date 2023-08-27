from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_cnt = Counter()
        for i in range(1, n + 1):
            group_cnt[sum(map(int, str(i)))] += 1
        max_size = group_cnt.most_common(1).pop()[1]
        return len([val for val in group_cnt.values() if val == max_size])

r = Solution().countLargestGroup(13)
print(r)