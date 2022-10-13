from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            image[i] = [0 if cell == 1 else 1 for cell in image[i]]
        return image

# print([1, 2, 3][:: -1])
