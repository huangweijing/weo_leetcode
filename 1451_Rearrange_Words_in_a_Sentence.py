class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(sep=" ")
        words[0] = words[0].lower()
        new_words = [[len(word), i, word] for i, word in enumerate(words)]
        new_words.sort()
        ans_arr = [word[2] for word in new_words]
        ans_arr[0] = ans_arr[0][0].upper() + ans_arr[0][1: ]
        return " ".join(ans_arr)

