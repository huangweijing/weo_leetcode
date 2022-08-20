from typing import List

class Solution:
    MORSE_CODE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        word_set = set[str]()

        for word in words:
            word_code = ""
            for ch in word:
                idx = ord(ch) - ord("a")
                word_code += Solution.MORSE_CODE[idx]
            word_set.add(word_code)

        return len(word_set)
