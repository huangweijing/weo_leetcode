class Solution:
    def minDeletions(self, s: str) -> int:
        frequency_table = dict[s, int]()
        for ch in s:
            if ch not in frequency_table:
                frequency_table[ch] = 1
            else:
                frequency_table[ch] += 1
        fre_table = dict[int, int]()
        for fre in frequency_table.values():
            if fre not in fre_table:
                fre_table[fre] = 1
            else:
                fre_table[fre] += 1
        step = 0

        for key in list(fre_table.keys()):
            while fre_table[key] > 1:
                # print(fre_table, key, step)
                search = key - 1
                while search > 0:
                    if search in fre_table.keys():
                        search -= 1
                    else:
                        step += (key - search)
                        fre_table[search] = 1
                        fre_table[key] -= 1
                        break
                if search == 0:
                    step += key
                    fre_table[key] -= 1
        return step

sol = Solution()
r = sol.minDeletions("ceabaacb")
print(r)
