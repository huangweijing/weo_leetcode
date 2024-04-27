class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = 0
        words = s.split()
        for word in words:
            if word.isdigit():
                num = int(word)
                if num <= last:
                    return False
                else:
                    last = num
        return True
