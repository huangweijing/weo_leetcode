class Solution:
    def stringHash(self, s: str, k: int) -> str:
        idx = 0
        ans = ""
        while idx < len(s):
            hash_cd = 0
            for _ in range(k):
                hash_cd += ord(s[idx]) - ord('a')
                idx += 1
            hash_cd %= 26
            ans += chr(hash_cd + ord("a"))
        return ans