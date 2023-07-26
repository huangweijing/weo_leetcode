class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        vowel_idx = []
        vowel_list = []
        for i, ch in enumerate(s_list):
            if ch in vowels:
                vowel_idx.append(i)
                vowel_list.append(ch)
        vowel_list.sort()
        for i, idx in enumerate(vowel_idx):
            s_list[idx] = vowel_list[i]
        return "".join(s_list)

r = Solution().sortVowels("lEetcOde")
print(r)