import math

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        h1, m1 = int(loginTime[:2]), int(loginTime[3:])
        h2, m2 = int(logoutTime[:2]), int(logoutTime[3:])
        m1 = math.ceil(m1 / 15) * 15
        m2 = (m2 // 15) * 15
        # print(h1, m1, h2, m2)
        if loginTime <= logoutTime:
            return max(0, (h2 * 60 + m2 - (h1 * 60 + m1)) // 15)
        else:
            return max(0, (24 * 60 + h2 * 60 + m2 - (h1 * 60 + m1)) // 15)
        
data = [
    "00:00"
    , "23:59"
]
r = Solution().numberOfRounds(*data)
print(r)