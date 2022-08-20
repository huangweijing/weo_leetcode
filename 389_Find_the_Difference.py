class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch_dict = dict[str, int]()
        ch_dict2 = dict[str, int]()
        for ch in s:
            if ch not in ch_dict:
                ch_dict[ch] = 0
            ch_dict[ch] += 1
        for ch in t:
            if ch not in ch_dict2:
                ch_dict2[ch] = 0
            ch_dict2[ch] += 1
        for key in ch_dict2:
            if key not in ch_dict:
                return key
            elif ch_dict[key] < ch_dict2[key]:
                return key
        return ""
