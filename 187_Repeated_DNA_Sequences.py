from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = list[str]()
        occured_set = set[str]()
        added_set = set[str]()
        for i in range(len(s) - 9):
            dna_seg = s[i: i + 10]
            # print(dna_seg)
            if dna_seg in occured_set and dna_seg not in added_set:
                result.append(dna_seg)
                added_set.add(dna_seg)
            else:
                occured_set.add(dna_seg)
        return result

r = Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
print(r)