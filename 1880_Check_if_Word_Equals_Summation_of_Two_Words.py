class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1, num2, num_tar = 0, 0, 0
        for ch in firstWord:
            num1 = num1 * 10 + ord(ch) - ord('a')
        for ch in secondWord:
            num2 = num2 * 10 + ord(ch) - ord('a')
        for ch in targetWord:
            num_tar = num_tar * 10 + ord(ch) - ord('a')
        return num1 + num2 == num_tar
