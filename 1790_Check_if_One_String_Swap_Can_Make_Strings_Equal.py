class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        error = False
        exchanged = False
        ch_pair = []
        for i, ch in enumerate(s1):
            if s2[i] == ch:
                continue
            else:
                if exchanged:
                    return False
                if not error:
                    ch_pair = [ch, s2[i]]
                    error = True
                else:
                    if ch_pair != [s2[i], ch]:
                        return False
                    else:
                        error = False
                        exchanged = True
        if error:
            return False
        return True
    

data = [
    "bank"
    , "knab"
]
r = Solution().areAlmostEqual(*data)
print(r)