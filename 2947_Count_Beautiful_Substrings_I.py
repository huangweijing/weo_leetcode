class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowel_set = set[str](["a", "e", "i", "o", "u"])
        pre_vowel, pre_conso = [0], [0]
        vowel_cnt, conso_cnt = 0, 0
        for i, ch in enumerate(s):
            if ch in vowel_set:
                vowel_cnt += 1
            else:
                conso_cnt += 1
            pre_vowel.append(vowel_cnt)
            pre_conso.append(conso_cnt)
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                vc = pre_vowel[j + 1] - pre_vowel[i]
                cc = pre_conso[j + 1] - pre_conso[i]
                if vc * cc % k == 0 and vc == cc:
                    ans += 1
        return ans
