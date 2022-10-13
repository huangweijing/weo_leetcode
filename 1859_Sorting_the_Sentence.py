class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        ans = [""] * len(arr)
        for word in arr:
            ans[ord(word[-1]) - ord("0") - 1] = word[:-1]
        return " ".join(ans)
