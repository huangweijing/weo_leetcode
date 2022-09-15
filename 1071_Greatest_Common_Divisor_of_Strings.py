class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        test_gcd = str1 if len(str1) < len(str2) else str2
        gcd_len = len(test_gcd)
        while test_gcd != "":
            if len(str1) % gcd_len == len(str2) % gcd_len == 0:
                if test_gcd * int(len(str1) / gcd_len) == str1 and \
                    test_gcd * int(len(str2) / gcd_len) == str2:
                    return test_gcd
            test_gcd = test_gcd[:-1]
            gcd_len = len(test_gcd)
        return test_gcd

r = Solution().gcdOfStrings("ababab", "abcab")
print(r)
