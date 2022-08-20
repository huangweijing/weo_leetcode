from typing import List
from functools import cache

def is_palindrome(s: str) -> bool:
    for i in range(len(s) >> 1):
        if s[i] != s[-1 - i]:
            return False
    return True

# def isPal(self, s):
#     return s == s[::-1]

class Solution:

    @cache
    def my_partition(self, s: str) -> list[list[str]]:
        result = list[list[str]]()
        result_set = set[int]()
        if is_palindrome(s):
            result.append([s])
        for i in range(1, len(s)):
            # print(s[:i], s[i:])
            sub1 = self.my_partition(s[: i])
            sub2 = self.my_partition(s[i: ])
            for r1 in sub1:
                for r2 in sub2:
                    r = r1.copy()
                    r.extend(r2)
                    key = ".".join(r)
                    if key not in result_set:
                        result_set.add(key)
                        result.append(r)
        return result

    def partition(self, s: str) -> List[List[str]]:
        my_result = self.my_partition(s)
        # result_set = set[int]()
        # result = list[list[str]]()
        # for r in my_result:
        #     key = ".".join(r)
        #     if key not in result_set:
        #         result_set.add(key)
        #         result.append(r)
        return my_result

r = Solution().partition("fffffffffffffffffff")
print(len(r))