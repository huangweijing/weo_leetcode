from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 1:
            if not "0" <= s[0] <= "9":
                return [s[0].lower(), s[0].upper()]
            else:
                return [s[0]]
        sub_result = self.letterCasePermutation(s[1:])
        result = list[str]()
        for i in range(len(sub_result)):
            if not "0" <= s[0] <= "9":
                result.append(s[0].lower() + sub_result[i])
                result.append(s[0].upper() + sub_result[i])
            else:
                result.append(s[0] + sub_result[i])
        # print(s, result)
        return result

r = Solution().letterCasePermutation("a4b7c")
print(r)

