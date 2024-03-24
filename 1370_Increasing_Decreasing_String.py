from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        alp_list = list(range(ord("a"), ord("a") + 26))
        ans = ""
        rev = False
        while len(cnt) > 0:
            # print(cnt, alp_list)
            tra_list = reversed(alp_list) if rev else alp_list
            rev = not rev
            to_rem = set[int]()
            for i in tra_list:
                if cnt[chr(i)] == 0:
                    del cnt[chr(i)]
                    to_rem.add(i)
                else:
                    ans += chr(i)
                    cnt[chr(i)] -= 1
            # print(to_rem)
            for i in to_rem:
                alp_list.remove(i)
        return ans


r = Solution().sortString("aaaabbbbcccc")
print(r)


