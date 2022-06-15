bbb = "abcdadf"

# def m(t:str):
#     for i in t:
#         print(t.count(i))
#         if t.count(i) == 1:
#             return i
#         else:
#             return "no"
# print(m(bbb))

class Solution:
    def __init__(self):
        self.largest_tbl: list[int] = []
        self.cache = [None] * 10000

    def lis(self, arr: list[int], arr_len) -> list[int]:
        if arr_len in self.cache:
            return self.cache[arr_len]
        if arr_len == 1:
            return [arr[0]]

        # print(arr, self.largest_tbl, arr_len - 1)
        if arr[arr_len - 1] == self.largest_tbl[arr_len - 1]:
            n_1_result = self.lis(arr, arr_len - 1)
            result = n_1_result.copy()
            result.append(arr[arr_len - 1])
        else:
            result = self.lis(arr, arr_len - 1).copy()

        self.cache[arr_len] = result
        return result

    def get_list(self, arr: list[int]):
        maximum = -1
        for i in arr:
            if i > maximum:
                maximum = i
            self.largest_tbl.append(maximum)
        # print(self.largest_tbl)
        # print(self.lis(arr, len(arr)))
        return self.lis(arr, len(arr))

sol = Solution()
r = sol.get_list([1, 4, 2, 7, 8, 9, 2, 1, 3, 8, 6, 5])
print(r)
