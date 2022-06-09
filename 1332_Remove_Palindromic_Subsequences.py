class Solution:
    def is_palindrome(self, s):
        idx1 = 0
        idx2 = len(s) - 1
        while idx1 != idx2 and idx1 - 1 != idx2:
            if s[idx1] != s[idx2]:
                return False
            idx1 += 1
            idx2 -= 1
        return True

    def removePalindromeSub2(self, s: str) -> int:
        start_idx = 0
        cnt = 0
        while start_idx <= len(s) - 1:
            end_idx = len(s) - 1
            # print(start_idx, end_idx)
            while end_idx >= start_idx:
                if self.is_palindrome(s[start_idx: end_idx + 1]):
                    start_idx = end_idx + 1
                    break
                end_idx -= 1
            cnt += 1
        return cnt

    def removePalindromeSub(self, s: str) -> int:
        return 1 if self.is_palindrome(s) else 2

sol = Solution()
c = sol.removePalindromeSub("bbaabaaa")
print(c)



