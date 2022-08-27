from collections import deque

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        idx = len(s) - 1
        scanned_stack = list[str]()
        mirror_queue = deque[str]()
        while idx > 0:
            ch = s[idx]
            if ch == 

            if len(mirror_queue) > 0:


            if len(scanned_stack) > 0:
                pass

            idx -= 1

