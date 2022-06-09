from typing import List

class Solution:
    def calc_hash(self, s: str):
        alph_tbl = [0] * 26
        for ch in s:
            alph_tbl[ord(ch) - ord('a')] += 1
        hash_code = ""
        for i, cnt in enumerate(alph_tbl):
            hash_code += chr(ord('a') + i) + str(cnt)
        return  hash_code

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = dict[str, list[str]]()
        for s in strs:
            hc = self.calc_hash(s)
            if hc not in anagram.keys():
                anagram[hc] = []
            anagram[hc].append(s)
        result: list[list[str]] = list[list[str]]()
        for group in anagram.values():
            result.append(group)
        # print(result)
        return result

sol = Solution()
r = sol.groupAnagrams(["abc", "cba", "aaa", "bbb"])
print(r)
