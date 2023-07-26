class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sent_arr = sentence.split(sep=" ")
        for i, word in enumerate(sent_arr[1:], start=1):
            if sent_arr[i - 1][-1] != word[0]:
                return False
        if sent_arr[-1][-1] != sent_arr[0][0]:
            return False
        return True