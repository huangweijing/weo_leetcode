class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ch_set = set[int]()
        for ch in sentence:
            ch_set.add(ch)
            if len(ch_set) == 26:
                return True

        return False
