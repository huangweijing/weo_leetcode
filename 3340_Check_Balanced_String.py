class Solution:
    def isBalanced(self, num: str) -> bool:
        arr = [0, 0]
        for i, ch in enumerate(num):
            arr[i & 1] += ord(ch) - ord('0')
        return arr[0] == arr[1]