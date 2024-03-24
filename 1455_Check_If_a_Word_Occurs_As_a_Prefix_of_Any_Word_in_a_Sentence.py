class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = 1
        idx = 0
        while idx < len(sentence):
            i = 0
            while idx < len(sentence) and i < len(searchWord) \
                    and sentence[idx] == searchWord[i]:
                idx += 1
                i += 1
            if i == len(searchWord):
                return ans
            while idx < len(sentence) and sentence[idx] != " ":
                idx += 1
            idx += 1
            ans += 1
        return -1

r = Solution().isPrefixOfWord("hey jude", "jud")
print(r)
