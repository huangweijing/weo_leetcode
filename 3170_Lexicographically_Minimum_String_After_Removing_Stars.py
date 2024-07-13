from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        idx_dict = defaultdict(lambda : list[int]())
        for i, ch in enumerate(s):
            if ch == "*":
                for alp in range(ord("a"), ord("z") + 1):
                    if len(idx_dict[chr(alp)]) > 0:
                        idx_dict[chr(alp)].pop()
                        break
            else:
                idx_dict[ch].append(i)
            # print(idx_dict)
        lst = []
        for key, idx_list in idx_dict.items():
            for idx in idx_list:
                lst.append([key, idx])
        lst.sort(key=lambda x: [x[1], x[0]])
        ans = ""
        for ch, idx in lst:
            ans += ch
        return ans


r = Solution().clearStars("aaba*")
print(r)