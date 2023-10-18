from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        block_commenting = False
        slash_commenting = False
        cleared_line = ""
        for line in source:
            i = 0
            while i < len(line):
                if not slash_commenting and not block_commenting and i + 1 < len(line) and line[i] == "/" and line[i + 1] == "*":
                    block_commenting = True
                    i = i + 2
                    continue
                elif not slash_commenting and not block_commenting and i + 1 < len(line) and line[i] == "/" and line[i + 1] == "/":
                    slash_commenting = True
                    i = i + 2
                    continue
                elif not slash_commenting and block_commenting and i + 1< len(line) and line[i] == "*" and line[i + 1] == "/":
                    i = i + 2
                    block_commenting = False
                    continue
                if slash_commenting or block_commenting:
                    pass
                else:
                    if i < len(line):
                        cleared_line += line[i]
                # print(f"slash:{slash_commenting}, block:{block_commenting}, cleared_line={cleared_line}")
                i += 1
            slash_commenting = False
            if len(cleared_line) > 0 and not block_commenting:
                ans.append(cleared_line)
                cleared_line = ""
        return ans


data = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
r = Solution().removeComments(data)
print(r)

