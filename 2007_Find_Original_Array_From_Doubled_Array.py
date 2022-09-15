from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1 == 1:
            return []
        changed_counter = Counter(changed)
        keys = list(changed_counter.keys())
        keys.sort()
        result = list[int]()
        while len(keys) > 0:
            key = keys.pop()
            cnt = changed_counter[key]
            # print(key, cnt)
            if cnt == 0:
                continue
            if key & 1 == 1 and cnt > 0:
                return []
            if key == 0:
                result = result + [0] * (cnt >> 1)
                return result
            if key >> 1 in changed_counter and changed_counter[key >> 1] >= cnt:
                changed_counter[key >> 1] -= cnt
                result = result + [key >> 1] * cnt
            else:
                return []
        return result

r = Solution().findOriginalArray([0])
print(r)





