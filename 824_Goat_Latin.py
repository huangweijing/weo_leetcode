class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new_sentence = []
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word[0] in "auieoAUIEO":
                new_sentence.append(word + "m" + "a" * (i + 2))
            else:
                new_sentence.append(word[1:] + word[0] + "m" + "a" * (i + 2))
        return " ".join(new_sentence)
