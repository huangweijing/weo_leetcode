class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(sep=" ")
        result = list[str]()
        for word in arr:
            result.append(word[::-1])
        return " ".join(result)

