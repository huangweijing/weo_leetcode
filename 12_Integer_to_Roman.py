ch = {
    'I': 1
    , 'IV': 4
    , 'V': 5
    , 'IX': 9
    , 'X': 10
    , 'XL': 40
    , 'L': 50
    , 'XC': 90
    , 'C': 100
    , 'CD': 400
    , 'D': 500
    , 'CM': 900
    , 'M': 1000
}

num_dict = {}
for key in ch.keys():
    num_dict[ch[key]] = key

num_key_list = list(num_dict.keys())
num_key_list.sort(reverse=True)


class Solution:
    def intToRoman(self, num: int) -> str:
        result_str = ""
        while num != 0:
            for maxnum in num_key_list:
                if num < maxnum:
                    continue
                num = num - maxnum
                result_str = result_str + num_dict[maxnum]
                break
        return result_str


sol = Solution()
result = sol.intToRoman(1994)
print(result)