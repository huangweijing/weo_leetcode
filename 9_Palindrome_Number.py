class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        i = 0
        while i < len(x_str) - 1 - i:
            if x_str[i] != x_str[len(x_str) - 1 - i]:
                return False
            i = i + 1
        return True
