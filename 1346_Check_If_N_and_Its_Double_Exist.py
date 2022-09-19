from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[j] & 1 == 0 and arr[i] == arr[j] >> 1) or \
                    (arr[i] & 1 == 0 and arr[j] == arr[i] >> 1):
                    return True
        return False