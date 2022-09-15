class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        str_num = str(num)
        for i in range(len(str_num) - k + 1):
            divisor = int(str_num[i: i + k])
            if divisor == 0:
                continue
            if num % divisor == 0:
                result += 1
        return result

