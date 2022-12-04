from collections import deque

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        q = deque(pattern)
        num_arr = deque(map(str, range(2, 10)))
        ans = "1"
        while len(q) > 0:
            if ans != "" and q[0] == "I":
                num_arr.appendleft(ans[-1])
                ans = ans[:-1]
                q.appendleft("I")
            while len(q) > 0 and q[0] == "I":
                q.popleft()
                ans += num_arr.popleft()
            tmp_str = ""
            if len(q) == 0:
                break
            if ans != "" and q[0] == "D":
                num_arr.appendleft(ans[-1])
                ans = ans[:-1]
                q.appendleft("D")
            while len(q) > 0 and q[0] == "D":
                q.popleft()
                tmp_str += num_arr.popleft()
            ans += tmp_str[::-1]
        return ans

r = Solution().smallestNumber("DDDIII")
print(r)

