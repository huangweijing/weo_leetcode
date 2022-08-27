class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.upper().split("-"))
        idx = len(s) - k
        result_arr = list[str]()
        while idx >= 0:
            result_arr.append(s[idx: idx + k])
            idx = idx - k
        if -k < idx < 0:
            result_arr.append(s[: idx + k])
        result_arr.reverse()
        # print(result_arr)
        return "-".join(result_arr)

Solution().licenseKeyFormatting("r", 1)

