class Solution:
    def simplifyPath(self, path: str) -> str:
        seg_list = path.split("/")
        path_stack = []
        for seg in seg_list:
            if seg == "." or len(seg) == 0:
                continue
            elif seg == "..":
                if len(path_stack) > 0:
                    path_stack.pop()
            else:
                path_stack.append(seg)

        if len(path_stack) == 0:
            return "/"

        result = ""
        for seg in path_stack:
            result += "/" + seg
        return result

sol = Solution()
r = sol.simplifyPath("/home/../hello/./ticket/")
print(r)
