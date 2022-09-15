class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver_arr1 = version1.split(".")
        ver_arr2 = version2.split(".")
        len1, len2 = len(ver_arr1), len(ver_arr2)

        for i in range(max(len1, len2)):
            if i >= len2:
                if int(ver_arr1[i]) != 0:
                    return 1
                else:
                    continue
            if i >= len1:
                if int(ver_arr2[i]) != 0:
                    return -1
                else:
                    continue
            if int(ver_arr1[i]) > int(ver_arr2[i]):
                return 1
            if int(ver_arr1[i]) < int(ver_arr2[i]):
                return -1
        return 0

r = Solution().compareVersion("100.2.3.42.2.0.0.0", "100.002.3.00042.2")
print(r)