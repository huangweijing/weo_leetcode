class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ""
        status = ""
        dot_cnt = 0
        for do in dominoes:
            if do == "R":
                if status == "" or status == "L":
                    result += dot_cnt * "."
                elif status == "R":
                    result += dot_cnt * "R"
                dot_cnt = 0
                result += "R"
                status = "R"

            elif do == "L":
                if status == "" or status == "L":
                    result += dot_cnt * "L"
                elif status == "R":
                    result += (dot_cnt >> 1) * "R"
                    if dot_cnt & 1 == 1:
                        result += "."
                    result += (dot_cnt >> 1) * "L"
                dot_cnt = 0
                result += "L"
                status = "L"

            elif do == ".":
                dot_cnt += 1

        if status == "R":
            result += "R" * dot_cnt
        elif status == "" or status == "L":
            result += "." * dot_cnt
        return result

data_dominoes = ".L.R...LR..L.."
r = Solution().pushDominoes(data_dominoes)
print(r)
