from typing import List

class Solution:
    def __init__(self):
        self.result = list[int]()

    def replace_stamp(self, stamp: list[str], target: list[str]):
        idx1 = 0
        replaced_char = 0
        while idx1 < len(target) - len(stamp) + 1:
            idx2 = 0
            replace_okay = True
            ch_cnt = 0
            # print(f"idx1={idx1}")
            while idx2 < len(stamp):
                # print(f"idx2={idx2}, target[idx1 + idx2]={target[idx1 + idx2]}, stamp[idx2]={stamp[idx2]}")
                if target[idx1 + idx2] == "*":
                    ch_cnt += 1
                if target[idx1 + idx2] == stamp[idx2] or target[idx1 + idx2] == "*":
                    # print(f"idx2={idx2}, target[idx1 + idx2]={target[idx1 + idx2]}")
                    idx2 += 1
                else:
                    replace_okay = False
                    break
            if replace_okay and ch_cnt != len(stamp):
                # print("replace okay")
                self.result.append(idx1)
                target[idx1:idx1 + len(stamp)] = "*" * len(stamp)
                idx1 += len(stamp)
                replaced_char += len(stamp) - ch_cnt
            else:
                idx1 += 1
        return replaced_char

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        pre_replaced_cnt = -1
        replaced_cnt = 0
        s = list(stamp)
        t = list(target)
        while replaced_cnt != len(target):
            replaced_cnt += self.replace_stamp(s, t)
            if pre_replaced_cnt == replaced_cnt:
                return []
            pre_replaced_cnt = replaced_cnt
        self.result.reverse()
        # print(self.result)
        return self.result


r = Solution().movesToStamp("eye", "eyeeye")
print(r)