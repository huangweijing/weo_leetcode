from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_content_dict = dict[str, list[int]]()
        for path in paths:
            path_arr = path.split(" ")
            directory = path_arr[0]
            for i in range(1, len(path_arr)):
                idx = path_arr[i].find("(")
                filename = path_arr[i][: idx]
                content = path_arr[i][idx + 1:-1]
                if content not in file_content_dict:
                    file_content_dict[content] = list[int]()
                file_content_dict[content].append(directory + "/" + filename)

        result = []
        for key, val in file_content_dict.items():
            if len(val) > 1:
                result.append(val)
        return result
