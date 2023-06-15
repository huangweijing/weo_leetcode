from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            if int(detail[-4: -2]) > 60:
                ans += 1
        return ans