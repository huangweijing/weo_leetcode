class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = list[str]()
        for word in words:
            if len(word) != len(pattern):
                continue
            pro_dict = dict[str, str]()
            rev_dict = dict[str, str]()
            found_flg = True
            for i, ch in enumerate(word):
                if ch not in pro_dict.keys():
                    pro_dict[ch] = pattern[i]
                else:
                    if pro_dict[ch] != pattern[i]:
                        found_flg = False
                        break
                if pattern[i] not in rev_dict:
                    rev_dict[pattern[i]] = ch
                else:
                    if rev_dict[pattern[i]] != ch:
                        found_flg = False
                        break

            if found_flg:
                result.append(word)
        return result


