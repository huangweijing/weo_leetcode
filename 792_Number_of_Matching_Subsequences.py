from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        alp_idx_hash = dict[str, list[int]]()
        for idx, ch in enumerate(s):
            if ch not in alp_idx_hash.keys():
                alp_idx_hash[ch] = list[int]()
            alp_idx_hash[ch].append(idx)
        result = 0
        for word in words:
            alp_cnt_hash = dict[str, int]()
            last_idx = -1
            is_seq = True
            for ch in word:
                # print(ch, alp_idx_hash, alp_cnt_hash, last_idx)
                if ch not in alp_cnt_hash.keys():
                    alp_cnt_hash[ch] = 0
                if ch not in alp_idx_hash.keys():
                    # print("if ch not in alp_idx_hash.keys()")
                    is_seq = False
                    break
                if alp_cnt_hash[ch] >= len(alp_idx_hash[ch]):
                    # print("alp_cnt_hash[ch] >= len(alp_idx_hash[ch])")
                    is_seq = False
                    break
                # print(alp_cnt_hash[ch])
                idx = alp_idx_hash[ch][alp_cnt_hash[ch]]
                while idx <= last_idx:
                    alp_cnt_hash[ch] += 1
                    if ch not in alp_idx_hash.keys():
                        # print("if ch not in alp_idx_hash.keys()")
                        is_seq = False
                        break
                    if alp_cnt_hash[ch] >= len(alp_idx_hash[ch]):
                        # print("alp_cnt_hash[ch] >= len(alp_idx_hash[ch])")
                        is_seq = False
                        break
                    idx = alp_idx_hash[ch][alp_cnt_hash[ch]]
                if not is_seq:
                    break

                if idx <= last_idx:
                    # print("idx <= last_idx", idx, last_idx)
                    is_seq = False
                    break
                last_idx = idx
                alp_cnt_hash[ch] += 1
            # print(word, is_seq)
            # print()
            if is_seq:
                result += 1
        return result

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
r = Solution().numMatchingSubseq(s, words)
print(r)