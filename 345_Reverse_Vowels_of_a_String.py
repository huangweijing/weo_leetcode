class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        p1 = 0
        p2 = len(s) - 1
        list_s = list(s)
        while p1 < p2:
            while p1 < len(s) and s[p1] not in vowels:
                p1 += 1
            while p2 >= 0 and s[p2] not in vowels:
                p2 -= 1
            if p1 < p2:
                tmp = list_s[p1]
                list_s[p1] = list_s[p2]
                list_s[p2] = tmp
                p1 += 1
                p2 -= 1
            else:
                break
        return "".join(list_s)


r = Solution().reverseVowels(".,")
print(r)