class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1] * n
        for _ in range(k):
            sum_val = 0
            for j in range(n):
                sum_val = (sum_val + arr[j]) % (10 ** 9 + 7)
                arr[j] = sum_val
        return arr[n - 1]
    

data = [4, 5]
r = Solution().valueAfterKSeconds(*data)
print(r)