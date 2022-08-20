class Solution:
    def __init__(self):
        self.s1 = ""
        self.s2 = ""
        # dp[str1][str2] means whether str1, str2 is scramble or not
        self.dp = dict[str, dict[str, bool]]()

    def init_data(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2
        for i in range(0, len(s1)):
            for j in range(i, len(s1)):
                self.dp[s1[i: j + 1]] = dict[str, bool]()

    def check_ch(self, s1:str, s2:str) -> bool:
        ch_cnt1 = dict[str, int]()
        ch_cnt2 = dict[str, int]()
        for idx in range(len(s1)):
            if s1[idx] not in ch_cnt1:
                ch_cnt1[s1[idx]] = 0
            ch_cnt1[s1[idx]] += 1
            if s2[idx] not in ch_cnt2:
                ch_cnt2[s2[idx]] = 0
            ch_cnt2[s2[idx]] += 1
        for key in ch_cnt1:
            if key not in ch_cnt2:
                return False
            if ch_cnt1[key] != ch_cnt2[key]:
                return False
        return True

    def my_is_scramble(self, s1: str, s2: str) -> bool:
        # print(f"check:({s1},{s2})")
        if s2 in self.dp[s1] and self.dp[s1][s2] is not None:
            # print(f"s2 in self.dp[s1] and self.dp[s1][s2] is not None result:{self.dp[s1][s2]}")
            return self.dp[s1][s2]
        result = False

        if s1 == s2:
            self.dp[s1][s2] = True
            # print(f"check if {s1} == {s2} result:False")
            return True

        if not self.check_ch(s1, s2):
            self.dp[s1][s2] = False
            # print(f"check if not self.check_ch({s1}, {s2}) result:False")
            return False

        for idx in range(1, len(s1)):
            # print(f"check:({self.s1[i:idx+1]},{self.s1[idx+1:j+1]}), ({self.s2[i:idx+1]},{self.s2[idx+1:j+1]})")
            r1 = self.my_is_scramble(s1[:idx], s2[-idx:])
            r2 = self.my_is_scramble(s1[idx:], s2[:-idx])
            if r1 & r2:
                result = True
                break

            r1 = self.my_is_scramble(s1[:idx], s2[:idx])
            r2 = self.my_is_scramble(s1[idx:], s2[idx:])
            if r1 & r2:
                result = True
                break

        self.dp[s1][s2] = result
        # print(f"check result:{result}")
        return self.dp[s1][s2]

    def isScramble(self, s1: str, s2: str) -> bool:
        # self.s1 = s1
        # self.s2 = s2
        self.init_data(s1, s2)
        # print(self.dp)
        return self.my_is_scramble(s1, s2)

r = Solution().isScramble("abcde", "caebd")
print(r)