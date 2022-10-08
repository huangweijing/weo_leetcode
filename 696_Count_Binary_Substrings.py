class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        arr = []
        while True:
            cnt = 0
            while i < len(s) and s[i] == "0":
                cnt += 1
                i += 1
            arr.append(cnt)
            if i >= len(s):
                break
            cnt = 0
            while i < len(s) and s[i] == "1":
                cnt += 1
                i += 1
            arr.append(cnt)
            if i >= len(s):
                break
        result = 0
        for i in range(1, len(arr)):
            result += min(arr[i - 1], arr[i])
        return result


