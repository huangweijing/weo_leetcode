class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        str_len = len(palindrome)
        if str_len <= 1:
            return ""
        if str_len & 1 == 0:
            if palindrome[:str_len >> 1] == palindrome[str_len >> 1:] == "a" * (str_len >> 1):
                return palindrome[:str_len - 1] + "b"
            else:
                for i, ch in enumerate(palindrome):
                    if ch != "a":
                        return palindrome[:i] + "a" + palindrome[i + 1:]
        else:
            if palindrome[:str_len >> 1] == palindrome[1 + (str_len >> 1):] == "a" * (str_len >> 1):
                return palindrome[:str_len - 1] + "b"

        for i, ch in enumerate(palindrome):
            if i == (str_len >> 1):
                continue
            if ch != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        return ""


