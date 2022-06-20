class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        fact_n = [1] * (n + 1)
        for i in range(1, n + 1, 1):
            fact_n[i] = fact_n[i - 1] * i
        dig_dic = list(range(1, n + 1))
        result = ""
        idx = n
        while idx >= 1:
            dig = int(k / fact_n[idx - 1])
            k = k % fact_n[idx - 1]
            num_cur_loop = dig_dic[dig]
            result += str(num_cur_loop)
            dig_dic.remove(num_cur_loop)
            idx -= 1

        return result



sol = Solution()
r = sol.getPermutation(3, 1)
print(r)


