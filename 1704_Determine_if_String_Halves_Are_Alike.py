class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        len_s = len(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return len(list(filter(lambda x: x in vowel, s[:len_s >> 1]))) \
               == len(list(filter(lambda x: x in vowel, s[len_s >> 1:])))
