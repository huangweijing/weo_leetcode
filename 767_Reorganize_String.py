from collections import Counter
from sortedcontainers import SortedList


class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        sorted_list = SortedList([[key, val] for key, val in cnt.items()],
                        key=lambda x: [x[1], x[0]])
        ans = ""
        while len(sorted_list) > 0:
            val = sorted_list.pop()
            if ans == "" or ans[-1] != val[0]:
                ans += val[0]
                val[1] -= 1
            else:
                if len(sorted_list) == 0:
                    return ""
                val2 = sorted_list.pop()
                ans += val2[0]
                val2[1] -= 1
                if val2[1] > 0:
                    sorted_list.add(val2)
            if val[1] > 0:
                sorted_list.add(val)
        return ans

r = Solution().reorganizeString("aab")
print(r)
