class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = dict[s, int]()
        for ch in s:
            if ch not in dic.keys():
                dic[ch] = 0
            dic[ch] += 1

        for ch in t:
            if ch not in dic.keys():
                return False
            else:
                dic[ch] -= 1
                if dic[ch] == 0:
                    del dic[ch]
        return True


