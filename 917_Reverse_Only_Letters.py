class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ptr1, ptr2 = 0, len(s) - 1
        s = list(s)
        while ptr1 < ptr2:
            while ptr1 < ptr2 and not ("a" <= s[ptr1] <= "z" or "A" <= s[ptr1] <= "Z"):
                ptr1 += 1
            while ptr1 < ptr2 and not ("a" <= s[ptr2] <= "z" or "A" <= s[ptr2] <= "Z"):
                ptr2 -= 1
            if not ptr1 < ptr2:
                break
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1
        return "".join(s)
