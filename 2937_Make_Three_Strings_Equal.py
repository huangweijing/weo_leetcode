class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if len(s1) == len(s2) == len(s3) <= 2 and \
            s1 == s2 == s3:
            return 0
        same_cnt = 0
        for i in range(len(s1)):
            if i >= len(s2) or i >= len(s3):
                break
            if s1[i] == s2[i] == s3[i]:
                same_cnt += 1
            else:
                break
        if same_cnt < 2:
            return -1
        return len(s1) + len(s2) + len(s3) - same_cnt * 3

