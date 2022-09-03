class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ch_set = set[str]()
        for ch in s:
            if ch in ch_set:
                return ch
            ch_set.add(ch)

