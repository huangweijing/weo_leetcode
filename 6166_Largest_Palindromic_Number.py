from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        num_dict = Counter(num)
        palindrom_dict = dict[str, int]()
        largest_num = -1
        for i in range(10):
            cnt = num_dict[str(i)]
            if cnt % 2 == 0:
                palindrom_dict[str(i)] = cnt
            else:
                largest_num = i
                palindrom_dict[str(i)] = cnt - 1
        # print(largest_num)
        result = ""
        for i in range(9, -1, -1):
            result += str(i) * (palindrom_dict[str(i)] >> 1)
            if i == largest_num:
                continue
        if largest_num != -1:
            if result == "" or int(result) == 0:
                result = str(largest_num)
            else:
                result = result + str(largest_num) + result[::-1]
        else:
            result = result + result[::-1]
        # print(result)
        return str(int(result))

r = Solution().largestPalindromic("99999000")
print(r)