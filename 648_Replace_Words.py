from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_set = set(dictionary)
        word_list = sentence.split()
        for i in range(len(word_list)):
            word = ""
            for ch in word_list[i]:
                word += ch
                if word in word_set:
                    word_list[i] = word
                    break
        return " ".join(word_list)
