class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        idx1 = 0
        idx2 = len(s) - 1
        while idx1 < idx2:
            while idx1 < len(s) and not "a" <= s[idx1] <= "z" and not "0" <= s[idx1] <= "9":
                idx1 += 1
            while idx2 >= 0 and not "a" <= s[idx2] <= "z" and not "0" <= s[idx2] <= "9":
                idx2 -= 1

            if not idx1 < idx2:
                break

            if s[idx1] != s[idx2]:
                return False

            idx1 += 1
            idx2 -= 1

        return True