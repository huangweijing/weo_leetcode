class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split("-")
        p1 = bin(int(arr[0]))[2:]
        p2 = bin(int(arr[1]))[2:]
        p3 = bin(int(arr[2]))[2:]
        return f"{p1}-{p2}-{p3}"
        