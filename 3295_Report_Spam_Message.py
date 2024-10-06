from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        cnt = 0
        for word in message:
            if word in banned:
                cnt += 1
            if cnt >= 2:
                return True
        return False
