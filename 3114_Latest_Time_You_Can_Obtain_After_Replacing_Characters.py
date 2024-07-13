class Solution:
    def findLatestTime(self, s: str) -> str:
        str_arr = list(s)
        if str_arr[0] == "?":
            if str_arr[1] in ("?", "0", "1"):
                str_arr[0] = "1"
            else:
                str_arr[0] = "0"
        if str_arr[1] == "?":
            if str_arr[0] == "1":
                str_arr[1] = "1"
            else:
                str_arr[1] = "9"
        if str_arr[3] == "?":
            str_arr[3] = "5"
        if str_arr[4] == "?":
            str_arr[4] = "9"
        return "".join(str_arr)
