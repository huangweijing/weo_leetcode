class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_list = list(s1)
        s2_list = list(s2)
        s1_list.sort()
        s2_list.sort()
        s1breaks2, s2breaks1 = True, True
        for i in range(len(s1_list)):
            if s1_list[i] < s2_list[i]:
                s1breaks2 = False
            if s1_list[i] > s2_list[i]:
                s2breaks1 = False
            if not s1breaks2 and not s2breaks1:
                return False
        return True