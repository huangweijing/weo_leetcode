class Solution:
    def maxProduct(self, words: list[str]) -> int:
        maximum = 0
        words_len = len(words)
        for i in range(words_len):
            for j in range(i+1, words_len):
                if set(words[i]).isdisjoint(words[j]):
                    mul = len(words[i]) * len(words[j])
                    if maximum < mul:
                        maximum = mul
        return maximum

