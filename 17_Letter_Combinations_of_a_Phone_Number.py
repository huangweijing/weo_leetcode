class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_map = dict[str, list[str]]()
        digit_map["2"] = ["a", "b", "c"]
        digit_map["3"] = ["d", "e", "f"]
        digit_map["4"] = ["g", "h", "i"]
        digit_map["5"] = ["j", "k", "l"]
        digit_map["6"] = ["m", "n", "o"]
        digit_map["7"] = ["p", "q", "r", "s"]
        digit_map["8"] = ["t", "u", "v"]
        digit_map["9"] = ["w", "x", "y", "z"]

        result = list[str]()
        input_list = list[list[str]]()
        for dig in digits:
            input_list.append(digit_map[dig])

        for i in range(len(input_list)):
            ch_list = input_list[i]
            tmp_result = []
            if len(result) == 0:
                tmp_result = list(ch_list)
            else:
                for e1 in result:
                    for e2 in ch_list:
                        tmp_result.append(e1 + e2)
            result = tmp_result
        return result

    # def comb(self, ch: list[list[str]]):

sol = Solution()
r = sol.letterCombinations("239")
print(r)