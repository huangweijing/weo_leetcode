class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        map_min = { str_num[0] : "0" }
        map_max = dict[str, str]()
        for i in range(len(str_num)):
            if str_num[i] != "9":
                map_max[str_num[i]] = "9"
                break
        # if len(map_max) == 0:
        #     map_max["9"] = "9"
        min_num = int("".join([ch if ch not in map_min else map_min[ch] for ch in str_num]))
        max_num = int("".join([ch if ch not in map_max else map_max[ch] for ch in str_num]))
        # print(max_num, min_num)
        return max_num - min_num

r = Solution().minMaxDifference(990)
print(r)