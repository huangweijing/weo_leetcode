from typing import List
from collections import deque, defaultdict, Counter


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        pool_dict = defaultdict(lambda: deque())
        dry_queue = []
        dry_request = []
        for i, rain in enumerate(rains):
            if rain == 0:
                dry_queue.append(i)
            else:
                pool_dict[rain].append(i)
                if len(pool_dict[rain]) > 1:
                    pool_no = pool_dict[rain].popleft()
                    dry_request.append([pool_no, pool_dict[rain][0]])
        dry_request.sort()
        dry_queue.sort()
        dry_queue = deque(dry_queue)
        print(dry_queue, dry_request)
        for request in dry_request:
            if len(dry_queue) == 0:
                return []
            while len(dry_queue) > 0 and dry_queue[0] < request[0]:
                dry_queue.popleft()
            print(request, dry_queue)
            if len(dry_queue) > 0 and request[0] < dry_queue[0] < request[1]:
                dry_idx = dry_queue.popleft()
                ans[dry_idx] = rains[request[0]]
            else:
                return []
        while len(dry_queue) > 0:
            ans[dry_queue.pop()] = 1
        return ans
    

data = [1,2,0,2,3,0,1]
r = Solution().avoidFlood(data)
print(r)