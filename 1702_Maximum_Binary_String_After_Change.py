from collections import Counter


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        ans = ""
        idx = 0
        while idx < len(binary) and binary[idx] == "1":
            idx += 1
            ans += "1"
        cnt = Counter(binary[idx: ])
        ans += max(cnt["0"] - 1, 0) * "1"
        ans += "0" if cnt["0"] > 0 else ""
        ans += cnt["1"] * "1"
        return ans


# print("1" * -1)