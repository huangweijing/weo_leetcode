class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_hash = dict[str, int]()
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for i, row in enumerate(rows):
            for ch in row:
                row_hash[ch] = i
        result = list[str]()
        for word in words:
            row_set = set[str]()
            okay_flg = True
            for ch in word.lower():
                row_set.add(row_hash[ch])
                if len(row_set) > 1:
                    okay_flg = False
                    break
            if okay_flg:
                result.append(word)
        return result



