from functools import reduce

class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = str(num)
        ch_list = list(sorted(enumerate(str_num), key=lambda x: [x[1], -x[0]]))
        ans = []
        for i, ch in enumerate(str_num):
            if ch == ch_list[-1][1]:
                entry = ch_list.pop()
                ans.append(entry[1])
                continue
            else:
                entry = ch_list[-1]
                idx = len(ch_list) - 1
                to_exchange = idx
                while idx >= 0 and entry[1] == ch_list[idx][1]:
                    to_exchange = idx
                    idx -= 1
                ans.append(ch_list[to_exchange][1])
                ans.extend(str_num[i + 1: ])
                ans[ch_list[to_exchange][0]] = ch
                break
        return int(reduce(lambda a, b: int(a) * 10 + int(b), ans))


r = Solution().maximumSwap(1)
print(r)