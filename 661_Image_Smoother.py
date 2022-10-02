from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                avg_list = []
                for k in [i - 1, i, i + 1]:
                    for l in [j - 1, j, j + 1]:
                        if k < 0 or l < 0 or k >= m or l >= n:
                           pass
                        else:
                            avg_list.append(img[k][l])
                result[i][j] = int(sum(avg_list) / len(avg_list))
        return result


