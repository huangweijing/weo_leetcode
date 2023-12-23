class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        status = 1
        for i, num in enumerate(arr[1:-1], start=1):
            if arr[i - 1] < arr[i] < arr[i + 1]:
                if status == 1:
                    status = 1
                else:
                    return False
            elif arr[i - 1] < arr[i] > arr[i + 1]:
                if status == 1:
                    status = 0
                else:
                    return False
            elif arr[i - 1] > arr[i] > arr[i + 1]:
                if status == 0:
                    status = -1
                elif status == -1:
                    status = -1
                else:
                    return False
            else:
                return False
        if status in (-1, 0):
            return True
        else:
            return False
