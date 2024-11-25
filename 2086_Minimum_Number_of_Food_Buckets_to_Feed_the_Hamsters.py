class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        ans = 0
        arr = list(hamsters)
        for i, ch in enumerate(arr):
            last, next = "", ""
            if i > 0:
                last = arr[i - 1]
            if i < len(arr) - 1:
                next = arr[i + 1]
            if ch == "H":
                if last == "B":
                    continue
                if next == ".":
                    arr[i + 1] = "B"
                    ans += 1
                    continue
                if last == ".":
                    arr[i - 1] = "B"
                    ans += 1
                    continue
                else:
                    return -1
        return ans
    

data = "..H.HH.H.."
r = Solution().minimumBuckets(data)
print(r)