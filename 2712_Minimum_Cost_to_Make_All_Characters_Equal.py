from collections import deque


class Solution:
    def minimumCost(self, s: str) -> int:
        q = deque()
        i = 0
        while i < len(s):
            cnt = 0
            while i < len(s) and s[i] == "0":
                cnt += 1
                i += 1
            if cnt > 0:
                q.append(cnt)
            cnt = 0
            while i < len(s) and s[i] == "1":
                cnt += 1
                i += 1
            if cnt > 0:
                q.append(cnt)

        ans = 0
        while len(q) > 1:
            if q[0] > q[-1]:
                val = q.pop()
                q[-1] += val
            else:
                val = q.popleft()
                q[0] += val
            ans += val
        return ans

r = Solution().minimumCost("11001")
print(r)


