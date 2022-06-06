class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        i = 0
        j = 0
        ch_set = set()
        max_len = 0
        while i < str_len and j < str_len:
            while j < str_len and s[j] not in ch_set:
                ch_set.add(s[j])
                # print(ch_set)
                max_len = len(ch_set) if len(ch_set) > max_len else max_len
                j = j + 1
            while j < str_len and s[j] in ch_set:
                ch_set.remove(s[i])
                # print(ch_set)
                max_len = len(ch_set) if len(ch_set) > max_len else max_len
                i = i + 1
        return max_len


# sol = Solution()
# result = sol.lengthOfLongestSubstring("abcdedda")
# print(result)








